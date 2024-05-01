<script>
    import { goto } from '$app/navigation';
    export let data;
    const sessionId = data.params.slug

</script>

<h1>You're all set up!</h1>
<p>Your session ID is <b>{sessionId}</b></p>

<button class="btn btn-secondary" type="button" on:click={() => goto("/")}>
    {"< Go home"}
</button>

<button class="btn btn-primary" type="button" on:click={() => goto(`/manage`)}>
    Manage session
</button>

<style>
    h1 {
        font-family: 'Baloo 2 Variable', sans-serif;
        color: #890000;
        font-weight: 700;
        margin-top: 12px;
    }
</style>