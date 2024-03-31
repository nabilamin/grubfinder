<script>
    const locationImg = new URL('../../static/location.svg', import.meta.url).href;
    const categoryImg = new URL('../../static/burger.svg', import.meta.url).href;
    const priceImg = new URL('../../static/dollar.svg', import.meta.url).href;

    function createSession() {
        alert("this works");
    }
</script>

<div class="container">

    <div class="row">
        <div class="col mb-4">
            <h2 class="content-title">Need help deciding on a place to eat?</h2>
        </div>

        <div class="row mb-3">
            <!--LOCATION INPUT-->
            <div class="col-lg-4 col-md-12">
                <div class="input-group mb-3">
                    <div class="input-group-prepend">
                        <img src="{locationImg}" class="input-icon" alt="icon"/>
                    </div>
                    <input type="text" class="form-control" id="location" placeholder="Enter a location"
                           aria-label="Location"
                           aria-describedby="session-configuration">
                </div>
            </div>

            <!--CATEGORY INPUT-->
            <div class="col-lg-4 col-md-12">
                <div class="input-group mb-3">
                    <div class="input-group-prepend">
                        <img src="{categoryImg}" class="input-icon" alt="icon"/>
                    </div>
                    <input type="text" class="form-control" id="category" placeholder="Select a food category"
                           aria-label="Location"
                           aria-describedby="session-configuration">
                </div>
            </div>

            <!--PRICE INPUT-->
            <div class="col-lg-4 col-md-12">
                <div class="input-group mb-3">
                    <div class="input-group-prepend">
                        <img src="{priceImg}" class="input-icon" alt="icon"/>
                    </div>
                    <input type="text" class="form-control" id="price-range" placeholder="Select a price range"
                           aria-label="Location"
                           aria-describedby="session-configuration">
                </div>
            </div>
        </div>

        <div class="row mb-3">
            <div class="col">
                <button type="button" class="btn btn-primary" on:click={createSession}>Start a session</button>
            </div>
        </div>
    </div>

</div>

<style>
    .content-title {
        font-family: 'Baloo 2 Variable', sans-serif;
        color: #890000;
        font-weight: 700;
        margin-top: 12px;
    }

    .input-group-prepend {
        display: flex;
        border-left: 1px solid #ced4da;
        border-top: 1px solid #ced4da;
        border-bottom: 1px solid #ced4da;
        border-radius: 0.25rem;
        padding-left: 10px;
    }

    input {
        border-left: 0px;
    }

    .row > * {
        padding-right: 0;
    }


</style>