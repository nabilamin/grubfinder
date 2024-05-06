<script>
    import {goto} from "$app/navigation";

    /**
     * Allow the user to navigate away from the “Thank You” page
     */
    function goHome() {
        goto("/");
    }
</script>

<h1>Thank you</h1>
<p>Your votes have been submitted.</p>
<button type="button" class="pill-button" on:click={goHome}>Go to homepage</button>

<style>
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