<script>
    import { onMount } from 'svelte';

    const locationImg = new URL('../../static/location.svg', import.meta.url).href;
    const lockImg = new URL('../../static/lock.svg', import.meta.url).href;
    const priceImg = new URL('../../static/dollar.svg', import.meta.url).href;

    // Food categories to pick from
    let foodCategories = [ "New American",
"Italian",
"French",
"Restaurants",
"American",
"Steakhouses",
"Seafood",
"Gastropubs",
"Diners",
"Bars",
"Southern",
"Wine Bars",
"Mediterranean",
"Cocktail Bars",
"Spanish",
"Nightlife",
"Comfort Food",
"Tapas/Small Plates",
"Persian/Iranian",
"Caribbean",
"Mexican",
"Portuguese",
"Burgers",
"Breakfast & Brunch",
"Soul Food",
"Lounges",
"Pizza",
"Peruvian",
"Beer Bar",
"Greek",
"Food Court",
"Cuban",
"Pubs",
"Brewpubs",
"Latin American",
"New Mexican Cuisine",
"Thai",
"Sports Bars",
"Hawaiian",
"Irish Pub",
"Asian Fusion",
"Pasta Shops",
"Pop-Up Restaurants",
"Cajun/Creole",
"Salad",
"Barbeque",
"Tacos",
"Indian",
"Chinese",
"Filipino",
"Brazilian",
"Fish & Chips",
"Breweries",
"Korean",
"Vegetarian",
"Middle Eastern",
"Tex-Mex",
"Buffets",
"Vegan",
"Gluten-Free",
"Cafes",
"Cafeteria",
"Seafood Markets",
"Sandwiches",
"Teppanyaki",
"Halal",
"Vietnamese",
"Wraps",
"Himalayan/Nepalese",
"Ramen",
"Soup",
"Specialty Food",
"Desserts",
"Sushi Bars",
"Chicken Wings",
"Japanese",
"Hot Dogs",
"Food Stands",
"Food Delivery Services",
"Creperies",
"Delis",
"Laotian",
"Pancakes",
"Waffles",
"Food",
"Chicken Shop",
"Poke",
"Street Vendors",
"Hot Pot",
"Noodles",
"Fast Food",
"Food Trucks",
];
    // Initialize variables to store user input
    let location = '';
    let priceRange = '';
    let pin = '';

    // Function to create a session with the user input
    async function createSession() {

        // Data object to send to backend
        const data = {
            location: location,
            priceRange: priceRange,
            pin: pin
        };

        // Show data for testing purposes
        console.log(data);
        alert('Session was created with the following data: ' + JSON.stringify(data));

        // Put request to backend to create a session
        try {
            const response = await fetch('/api/session/create', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            // Check response
            if (response.ok) {
                console.log('Session created successfully');
            } else {
                console.log('Error: Session creation failed');
            }
        } catch (error) {
            console.error('Error:', error);
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
            <span class="input-group-append">
                <img src="{locationImg}" class="input-icon" alt="icon"/>
            </span>
        </div>

        <!--CATEGORY INPUT-->
        <!-- <div class="col-lg-4 col-md-12 mb-3">
            <label class="visually-hidden form-label" for="category">Food category</label>
            <input type="text" class="form-control" id="category" placeholder="Select a food category"
                   aria-label="Location"
                   aria-describedby="session-configuration">
            <input class="form-control" id="category" aria-label="Location" aria-describedby="session-configuration" list="foods" type="text" placeholder="Select a food category" autocomplete="on" maxlength="22" bind:value={category}>
            <datalist id="foods">
                {#each foodCategories as foodCategory}
                    <option value={foodCategory}/>
                {/each}
            </datalist>
            <span class="input-group-append">
                <img src="{categoryImg}" class="input-icon" alt="icon"/>
            </span>
        </div> -->

        <!--PRICE INPUT-->
        <div class="col-lg-4 col-md-12 mb-3">
            <label class="visually-hidden form-label" for="price-range">Price range</label>
            <!-- <input type="text" class="form-control" id="price-range" placeholder="Select a price range"
                   aria-label="Location"
                   aria-describedby="session-configuration"> -->
            <!-- <input class="form-control" id="price-range" aria-label="Location" aria-describedby="session-configuration" list="prices" placeholder="Select a price range" autocomplete="off" maxlength="4" bind:value={priceRange}>
            <datalist id="prices">
                <option value="$"/>
                <option value="$$"/>
                <option value="$$$"/>
                <option value="$$$$"/>
            </datalist> -->
            <select class="form-select" id="price-range" aria-label="Location" aria-describedby="session-configuration" bind:value={priceRange}>
                <option value="" selected>Select a price range</option>
                <option value="1">$</option>
                <option value="2">$$</option>
                <option value="3">$$$</option>
                <option value="4">$$$$</option>
            </select>
            <span class="input-group-append">
                <img src="{priceImg}" class="input-icon" alt="icon"/>
            </span>
        </div>

        <!--PIN INPUT-->
        <div class="col-lg-4 col-md-12 mb-3">
            <label class="visually-hidden form-label" for="pin">Session pin</label>
            <input type="text" class="form-control" id="pin" placeholder="Enter a session pin" aria-label="Location" aria-describedby="session-configuration" bind:value={pin} maxlength="4" minlength="4" pattern="\d{4}">
            <span class="input-group-append">
                <img src="{lockImg}" class="input-icon" alt="icon"/>
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