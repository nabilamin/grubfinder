<script>
    import UnderConstruction from "./+page.svelte";
    import '../app.css';
    import '../fonts.css';

    const bgImageSrc = new URL('../../static/Grubfinder_background.svg', import.meta.url).href;
</script>

<style>
    h1 {
        font-weight: 800;
    }

    .title {
        font-family: 'Baloo 2 Variable', sans-serif;
        color: white;
        margin: 20px auto;
    }

    .main-pane {
        background-color: white;
        border-radius: 20px;
        margin-top: 20%;
        padding: 1.5em 0;
    }
</style>

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
                <UnderConstruction/>
            </div>
        </div>
    </div>

</div>