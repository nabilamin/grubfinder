<script>
    import '../app.css';
    import bgImg from "../../static/Grubfinder_background.svg";

    const src = new URL('../../static/Grubfinder_background.svg', import.meta.url).href;
</script>

<style>
    .bg {
        width: 100%;
    }
</style>

<div class="bg" style="background-image: url({src});
                        width: 100%;
                        height: 100%;">

</div>
