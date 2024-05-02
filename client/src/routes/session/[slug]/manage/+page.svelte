<script>
    import {page} from "$app/stores";
    import {isLoading} from "../../../../store.js";
    import {goto} from "$app/navigation";

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

        const reqData = {"sessionId": $page.params.slug};

        const res = await fetch(`/session/${$page.params.slug}/end`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: ""
        });

        const responseBody = await res.json();

        console.log(JSON.stringify(responseBody));
        // const sessionId = responseBody

        isLoading.set(false);
        goto(`/session/${$page.params.slug}/end`);
    }
</script>

{#if data.sessionIsClosed}
    <p>Session is closed</p>
    <h1>Winner</h1>
    <p><b>Restaurant: {data.restaurantName}</b></p>
    <p>{data.restaurantAddress}</p>
    <p>Rating: {data.rating}</p>
    <p>Review Count: {data.reviewCount}</p>
    <p>Delivery: {data.hasDelivery ? "yes" : "no"}</p>
    <button type="button" class="pill-button" on:click={goBack}>Go Back</button>
{:else if data.voteCount > -1}
    <h1>Manage your session</h1>
    <p>Session ID: {$page.params.slug}</p>
    <p>Vote count: {JSON.stringify(data.voteCount)}</p>
    <p>Session URL: {getSessionUrl()}</p>

    <button type="button" class="pill-button" on:click={endSession}>End session</button>
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