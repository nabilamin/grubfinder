<script>
    import {page} from "$app/stores";
    import {isLoading} from "../../../../store.js";

    export let data;

    function getSessionUrl() {

        let baseUrl = new URL($page.url.href);
        let sessionLink = `${baseUrl.protocol}//${baseUrl.hostname}`;
        if (baseUrl.port !== "443" && baseUrl.port !== "80")
            sessionLink += `:${baseUrl.port}`;

        sessionLink += `/session/${$page.params.slug}/vote`;
        return sessionLink;
    }

    function goBack() {
        history.back();
    }

    async function endSession() {
        isLoading.set(true);

        try {
            const response = await fetch(`https://api.grubfinder.io/session/${$page.params.slug}/end`, {
                method: "POST",
                body: ""
            });

            const responseBody = await response.json();

            console.log(responseBody);
            isLoading.set(false);
        }
        catch (e) {
            isLoading.set(false);
            console.log("ERR -> " + e);
        }

        isLoading.set(false);
    }
</script>

{#if data.voteCount > -1}
    <h1>Manage your session</h1>
    <p>Session ID: {$page.params.slug}</p>
    <p>Vote count: {JSON.stringify(data.voteCount)}</p>
    <p>Session URL: {getSessionUrl()}</p>

    <button on:click={endSession}>End session</button>
{:else }
    <p>Invalid session id or pin</p>
    <button type="button" class="pill-button" on:click={goBack}>Go Back</button>
{/if}

<!--<p>{JSON.stringify(data)}</p>-->


<style>
    .pill-button {
        display: inline-block;
        background-color: #890000;
        color: white;
        padding: 10px 20px;
        border-radius: 50px;
        text-decoration: none;
        font-family: 'Baloo 2 Variable', sans-serif;
        font-size: 16px;
        cursor: pointer;
    }
</style>