<script>
    import '../app.css';
    import '../fonts.css';

    export let data;

    const bgImageSrc = new URL('../../static/Grubfinder_background.svg', import.meta.url).href;
</script>

<div style="background-image: url({bgImageSrc});
                            width: 100vw;
                            height: 100vh;
                            position: absolute;">

    <div class="container text-center">
        <div class="row title">
            <div class="col ">
                <h1>GRUBFINDER</h1>
            </div>
        </div>
        <div class="row main-pane">
            <div class="col">
                <slot></slot>
            </div>
        </div>

        {#if (data.route.id === "/")}
            <div class="row">
                <nav class="bottom-nav">
                    <a href="/session/1234/vote">JOIN A SESSION</a>
                    <a href="/session/1234/vote">MANAGE A SESSION</a>
                </nav>
            </div>
        {/if}


    </div>

</div>


<style>
    h1 {
        font-weight: 800;
    }

    .title h1 {
        font-family: 'Baloo 2 Variable', sans-serif;
        font-size: 2rem;
        color: white;
        margin: 20px auto;
    }

    .main-pane {
        background-color: white;
        border-radius: 20px;
        margin-top: 20%;
        padding: 1.5em 0;
    }

    nav {
        display: flex;
        flex-direction: column;
        margin-top: 2rem;
        align-items: center;
    }

    nav > a {
        font-family: 'Baloo 2 Variable', sans-serif;
        color: white;
        text-decoration: underline;
        text-decoration-skip-ink: auto;
        padding-bottom: 12px;
        font-weight: 800;
        font-size: 1.25rem;
        margin-bottom: 0.5rem;
        margin-top: 1.5rem;
        max-width: 220px;
        max-height: 100px;
    }
</style>