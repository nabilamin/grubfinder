<script>
    import {page} from "$app/stores";
    export let data;

    function getSessionUrl() {

        let baseUrl = new URL($page.url.href);
        let sessionLink = `${baseUrl.protocol}//${baseUrl.hostname}`;
        if (baseUrl.port !== "443" && baseUrl.port !== "80")
            sessionLink += `:${baseUrl.port}`;

        sessionLink += `/session/${$page.params.slug}/vote`;
        return sessionLink;
    }
</script>

<h1>Manage your session</h1>
<p>Session ID: {$page.params.slug}</p>
<p>Vote count: {JSON.stringify(data.created_at)}</p>
<p>Session URL: {getSessionUrl()}</p>