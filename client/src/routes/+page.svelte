<script>
    import { goto } from '$app/navigation';
    import { isLoading } from '../store.js';
    import sanitizeHtml from 'sanitize-html';

    const locationImg = new URL('../../static/location.svg', import.meta.url).href;
    const lockImg = new URL('../../static/lock.svg', import.meta.url).href;
    const priceImg = new URL('../../static/dollar.svg', import.meta.url).href;

    // Initialize variables to store user input
    let location = '';
    let priceRange = '';
    let pin = '';
    // Initialize variables to store error messages
    let locationError = '';
    let priceRangeError = '';
    let pinError = '';

    let sessionId = "";

    /**
     * @param {string} location
     * @param {string} pin
     */
    function sanitizeInput(location, pin) {
        // JavaScript function to sanitize user input by removing any potentially harmful HTML elements, whitelist approach
        const sanitizedLocation = sanitizeHtml(location);
        const sanitizedPin = sanitizeHtml(pin);

        return {
            sanitizedLocation,
            sanitizedPin
        };
    }

    async function handleSubmit() {
        isLoading.set(true);
        // Reset error messages
        locationError = '';
        priceRangeError = '';
        pinError = '';

        // Input validation
        let valid = true;
        // Chargoggagoggmanchauggagoggchaubunagungamaugg, Massachusetts is the longest place name in the United States
        if (location === '' || location.trim().length > 60) {
            locationError = 'Please enter a valid location';
            valid = false;
        }
        if (priceRange === '') {
            priceRangeError = 'Please select a price range';
            valid = false;
        }
        if (pin === '' || pin.length !== 4 || !/^\d+$/.test(pin)) {
            pinError = 'Please enter a 4-digit numerical pin';
            valid = false;
        }

        if (!valid) {
            isLoading.set(false);
            return;
        }
        

        const { sanitizedLocation, sanitizedPin } = sanitizeInput(location, pin);

        // Data object to send to backend
        const data = {
            "location": sanitizedLocation,
            "price": priceRange,
            "pin": sanitizedPin,
            "open_at": ""
        };

        const res = await fetch("/", {
           method: "POST",
           headers: {"Content-Type": "application/json"},
           body: JSON.stringify(data)
        });

        const responseBody = await res.json();

        // console.log(JSON.stringify(responseBody));
        const sessionId = responseBody.session_id;
        isLoading.set(false);
        if (sessionId) {
            await goto(`/session/${sessionId}/confirmation`);
        }
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
                   aria-describedby="session-configuration" bind:value={location}>
            {#if locationError}
                <div class="error-message">{locationError}</div>
            {/if}
            <span class="input-group-append">
                <img src="{locationImg}" class="input-icon" alt="icon"/>
            </span>
            </div>

        <!--PRICE INPUT-->
        <div class="col-lg-4 col-md-12 mb-3">
            <label class="visually-hidden form-label" for="price-range">Price range</label>
            <select class="form-select" id="price-range" aria-label="Location" aria-describedby="session-configuration" bind:value={priceRange}>
                <option value="" selected>Select a price range</option>
                <option value="1">$</option>
                <option value="2">$$</option>
                <option value="3">$$$</option>
                <option value="4">$$$$</option>
            </select>
            {#if priceRangeError}
                <div class="error-message">{priceRangeError}</div>
            {/if}
            <span class="input-group-append">
                <img src="{priceImg}" class="input-icon" alt="icon"/>
            </span>
        </div>

        <!--PIN INPUT-->
        <div class="col-lg-4 col-md-12 mb-3">
            <label class="visually-hidden form-label" for="pin">Session pin</label>
            <input type="text" class="form-control" id="pin" placeholder="Enter a session pin" aria-label="Location" aria-describedby="session-configuration" bind:value={pin} maxlength="4" minlength="4" pattern="\d{4}">
            {#if pinError}
                <div class="error-message">{pinError}</div>
            {/if}
            <span class="input-group-append">
                <img src="{lockImg}" class="input-icon" alt="icon"/>
            </span>
        </div>

        <div class="row mb-3">
            <div class="col">
                <button type="button" class="btn btn-primary" on:click={handleSubmit}>Start a session</button>
            </div>
        </div>
    </form>

    <!--{/if}-->

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

    .error-message {
        color: #890000;
        font-size: 0.8em;
        margin-top: 5px;
        position: absolute;
        padding-left: 38px;
    }

    input {
        padding-left: 37px;
    }

    .row > * {
        padding-right: 0;
    }

    #price-range {
        text-indent: 26px;
    }
</style>

