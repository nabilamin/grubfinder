<script>
    const locationImg = new URL('../../static/location.svg', import.meta.url).href;
    const categoryImg = new URL('../../static/burger.svg', import.meta.url).href;
    const priceImg = new URL('../../static/dollar.svg', import.meta.url).href;

    function createSession() {
        alert("this works");
    }
</script>

<div class="container">
    <h2 class="content-title mb-5">Need help deciding on a place to eat?</h2>

    <form class="row">
        <!--LOCATION INPUT-->
        <div class="col-lg-4 col-md-12 mb-3">
            <label class="visually-hidden form-label" for="location">Location</label>
            <input type="text" class="form-control" id="location" placeholder="Enter a location"
                   aria-label="Location"
                   aria-describedby="session-configuration">
            <span class="input-group-append">
                <img src="{locationImg}" class="input-icon" alt="icon"/>
            </span>
        </div>

        <!--CATEGORY INPUT-->
        <div class="col-lg-4 col-md-12 mb-3">
            <label class="visually-hidden form-label" for="category">Food category</label>
            <input type="text" class="form-control" id="category" placeholder="Select a food category"
                   aria-label="Location"
                   aria-describedby="session-configuration">
            <span class="input-group-append">
                <img src="{categoryImg}" class="input-icon" alt="icon"/>
            </span>
        </div>

        <!--PRICE INPUT-->
        <div class="col-lg-4 col-md-12 mb-5">
            <label class="visually-hidden form-label" for="price-range">Price range</label>
            <input type="text" class="form-control" id="price-range" placeholder="Select a price range"
                   aria-label="Location"
                   aria-describedby="session-configuration">
            <span class="input-group-append">
                <img src="{priceImg}" class="input-icon" alt="icon"/>
            </span>
        </div>


        <div class="row mb-3">
            <div class="col">
                <button type="button" class="btn btn-primary" on:click={createSession}>Start a session</button>
            </div>
        </div>
    </form>

</div>

<style>
    .content-title {
        font-family: 'Baloo 2 Variable', sans-serif;
        color: #890000;
        font-weight: 700;
        margin-top: 12px;
    }

    .input-icon {
        margin-left: 15px;
        margin-right: 15px;
        transform: translateY(-159%);
        pointer-events: none;
    }

    input {
        padding-left: 37px;
    }

    .row > * {
        padding-right: 0;
    }


</style>