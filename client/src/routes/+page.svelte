<script>
    import { goto } from '$app/navigation';
    import { isLoading } from '../store.js';
    import sanitizeHtml from 'sanitize-html';

    const locationImg = new URL('../../static/location.svg', import.meta.url).href;
    const lockImg = new URL('../../static/lock.svg', import.meta.url).href;
    const priceImg = new URL('../../static/dollar.svg', import.meta.url).href;

    // Initialize variables to store user input and error messages
    let location = '',
        locationError = '';

    let priceRange = '',
        priceRangeError = '';

    let pin = '',
        pinError = '';

    /**
     * Perform HTML sanitization of text input by the user
     */
    function sanitizeInput() {
        // JavaScript function to sanitize user input by removing any potentially harmful HTML elements, whitelist approach
        const sanitizedLocation = sanitizeHtml(location);
        const sanitizedPin = sanitizeHtml(pin);

        return {
            sanitizedLocation,
            sanitizedPin
        };
    }

    /**
     * Verfies that user input meets length and format requirements
     *
     * Location must be between 1 and 60 characters
     * Price range must have a value
     * PIN must be exactly 4 numerical digits
     *
     * @return true if all input is valid, false otherwise
     */
    function validateInput() {
        let isValid = true;
        // Chargoggagoggmanchauggagoggchaubunagungamaugg, Massachusetts
        // is the longest place name in the United States
        if (location === '' || location.trim().length > 60) {
            locationError = 'Please enter a valid location';
            isValid = false;
        }
        if (priceRange === '') {
            priceRangeError = 'Please select a price range';
            isValid = false;
        }
        if (pin === '' || pin.length !== 4 || !/^\d+$/.test(pin)) {
            pinError = 'Please enter a 4-digit numerical pin';
            isValid = false;
        }
        return isValid;
    }

    /**
     * Submit form to create session
     */
    async function handleSubmit() {
        isLoading.set(true);
        // Reset error messages
        locationError = '';
        priceRangeError = '';
        pinError = '';

        // Input validation
        const valid = validateInput();

        if (!valid) {
            isLoading.set(false);
            return;
        }
        
        const { sanitizedLocation, sanitizedPin } = sanitizeInput();

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

        // For testing
        // console.log(JSON.stringify(responseBody));

        const sessionId = responseBody.session_id;
        isLoading.set(false);
        if (sessionId) {
            await goto(`/session/${sessionId}/confirmation`);
        }
        else {
            // console.log(submissionError)
        }
    }
</script>

<div class="container">
    <h2 class="content-title mb-5">Need help deciding on a place to eat?</h2>
    <p>GrubFinder solves the hassle of picking where to eat.</p>
    <p class="mb-5">Easily vote on a restaurant with friends or colleagues, then let GrubFinder guide your group's dining decision impartially when ordering food.</p>
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
                <button type="button" class="pill-button" on:click={handleSubmit}>Start a session</button>
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

