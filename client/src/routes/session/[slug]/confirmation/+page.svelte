<script>
    import { goto } from '$app/navigation';
    export let data;
    const sessionId = data.params.slug

</script>

<h1>You're all set up!</h1>
<p>Your session ID is <b>{sessionId}</b></p>

<button class="pill-button" type="button" on:click={() => goto("/")}>
    {"< Go home"}
</button>

<button class="pill-button" type="button" on:click={() => goto(`/manage`)}>
    Manage session
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