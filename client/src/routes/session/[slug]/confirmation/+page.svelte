<script>
    import { goto } from '$app/navigation';
    import {page} from "$app/stores";

    export let data;
    const sessionId = data.params.slug
    const sessionUrl = getSessionUrl();

    /**
     * Gets a URL to vote in a session
     */
    function getSessionUrl() {
        let baseUrl = new URL($page.url.href);
        let sessionLink = `${baseUrl.protocol}//${baseUrl.hostname}`;
        if (baseUrl.port !== "443" && baseUrl.port !== "80")
            sessionLink += `:${baseUrl.port}`;

        sessionLink += `/session/${$page.params.slug}/vote`;
        return sessionLink;
    }

    /**
     * Adds the URL to vote in a session to the users clipboard
     */
    function copySessionUrlToClipboard() {
        const sessionUrl = getSessionUrl();
        navigator.clipboard.writeText(sessionUrl)
            .then(() => {
                alert("Session URL copied to clipboard: " + sessionUrl);
            })
            .catch(err => {
                console.error('Failed to copy: ', err);
            });
    }
</script>

<!--CONTENT TITLE-->
<h1>You're all set up!</h1>

<!--SESSION DETAILS-->
<p>Your session ID is <b>{sessionId}</b>. You'll need it to view your results.</p>
<p>Share this link with others so they can vote on a place to eat: <a href="{sessionUrl}">{sessionUrl}</a></p>

<!--BUTTONS-->
<button class="pill-button" type="button" on:click={copySessionUrlToClipboard}>
    Copy Voting Link
</button>

<button class="pill-button" type="button" on:click={() => goto("/")}>
    {"< Go home"}
</button>

<button class="pill-button" type="button" on:click={() => goto(`/manage`)}>
    Manage session
</button>

<button class="pill-button" type="button" on:click={() => goto(`/session/${sessionId}/vote`)}>
    Vote
</button>

<style>
    h1 {
        font-family: 'Baloo 2 Variable', sans-serif;
        color: #890000;
        font-weight: 700;
        margin-top: 12px;
    }
    .pill-button {
        display: inline-block;
        background-color: #890000;
        color: white;
        margin-top: 15px;
        padding: 10px 20px;
        border-radius: 50px;
        text-decoration: none;
        font-family: 'Baloo 2 Variable', sans-serif;
        font-size: 16px;
        cursor: pointer;
        border: none;
    }
</style>