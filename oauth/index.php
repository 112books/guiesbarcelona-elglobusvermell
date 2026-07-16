<?php
/**
 * OAuth proxy per a Sveltia CMS / Decap CMS + GitHub
 * Fase 1: desplegar a Dinahosting quan el servidor estigui llest.
 *
 * Configuració (fora del webroot o via .user.ini):
 *   GH_CLIENT_ID     = "el teu client id de la GitHub OAuth App"
 *   GH_CLIENT_SECRET = "el teu client secret"
 *   ALLOWED_ORIGIN   = "https://guiesbarcelona.elglobusvermell.org"
 *
 * GitHub OAuth App: Settings → Developer settings → OAuth Apps → New
 *   Homepage URL:     https://guiesbarcelona.elglobusvermell.org
 *   Callback URL:     https://guiesbarcelona.elglobusvermell.org/oauth/
 */

session_start();

$clientId     = $_ENV['GH_CLIENT_ID']     ?? getenv('GH_CLIENT_ID')     ?? '';
$clientSecret = $_ENV['GH_CLIENT_SECRET'] ?? getenv('GH_CLIENT_SECRET') ?? '';
$allowedOrigin = $_ENV['ALLOWED_ORIGIN']  ?? getenv('ALLOWED_ORIGIN')   ?? 'https://guiesbarcelona.elglobusvermell.org';

// ── Validació de configuració ──────────────────────────────────────────────
if (!$clientId || !$clientSecret) {
    http_response_code(500);
    die('OAuth proxy no configurat. Afegeix GH_CLIENT_ID i GH_CLIENT_SECRET.');
}

// ── PAS 1: Redirigeix a GitHub per autoritzar ──────────────────────────────
if (!isset($_GET['code'])) {
    // Genera i desa el token CSRF (state)
    $state = bin2hex(random_bytes(16));
    $_SESSION['oauth_state'] = $state;

    $params = http_build_query([
        'client_id' => $clientId,
        'scope'     => 'public_repo',
        'state'     => $state,
    ]);
    header("Location: https://github.com/login/oauth/authorize?{$params}");
    exit;
}

// ── PAS 2: GitHub ha retornat — valida el token CSRF ──────────────────────
$returnedState = $_GET['state'] ?? '';
$savedState    = $_SESSION['oauth_state'] ?? '';

if (!$returnedState || !hash_equals($savedState, $returnedState)) {
    http_response_code(403);
    die('Error de validació CSRF. Torna a iniciar sessió.');
}
unset($_SESSION['oauth_state']);

// ── PAS 3: Intercanvia el codi per un token d'accés (server-to-server) ────
$ctx = stream_context_create([
    'http' => [
        'method'  => 'POST',
        'header'  => implode("\r\n", [
            'Content-Type: application/x-www-form-urlencoded',
            'Accept: application/json',
            'User-Agent: guiesbarcelona-sveltia-oauth-proxy/1.0',
        ]),
        'content' => http_build_query([
            'client_id'     => $clientId,
            'client_secret' => $clientSecret,
            'code'          => $_GET['code'],
        ]),
        'timeout' => 10,
    ],
]);

$response = @file_get_contents('https://github.com/login/oauth/access_token', false, $ctx);

if ($response === false) {
    http_response_code(502);
    die('Error de connexió amb GitHub. Torna-ho a provar.');
}

$data  = json_decode($response, true);
$token = $data['access_token'] ?? '';
$error = $data['error'] ?? '';

if (!$token) {
    http_response_code(500);
    $msg = $error ? "Error de GitHub: {$error}" : 'No s\'ha rebut cap token de GitHub.';
    die(htmlspecialchars($msg));
}

// ── PAS 4: Retorna el token al CMS via postMessage ────────────────────────
// Limita a l'origen autoritzat per evitar XSS cross-origin
$tokenJson = json_encode($token);
$originJson = json_encode($allowedOrigin);

header('Content-Type: text/html; charset=utf-8');
header('Content-Security-Policy: default-src \'none\'; script-src \'unsafe-inline\'');
header('X-Frame-Options: DENY');
?>
<!doctype html>
<html>
<head><meta charset="utf-8"><title>Autenticació...</title></head>
<body>
<script>
(function () {
  var token  = <?= $tokenJson ?>;
  var origin = <?= $originJson ?>;
  var msg    = 'authorization:github:success:' + JSON.stringify({
    token: token,
    provider: 'github'
  });
  if (window.opener) {
    window.opener.postMessage(msg, origin);
  }
  window.close();
})();
</script>
<p>Autenticació completada. Podeu tancar aquesta finestra.</p>
</body>
</html>
