<script lang="ts">
    export let data: object;

    let index: number = 0;
    let votingResponse = new Map<string, boolean>();

    function handleClick(response: boolean) {
        votingResponse.set(data.restaurants[index].id, response);

        if (index + 1 == data.restaurants.length) {
            // Send data to Lambda
            console.log(votingResponse);
        } else {
            index++
        }
    }
</script>


<h1>{data.restaurants[index].name}</h1>
<p>Rating: {data.restaurants[index].rating}</p>
<p>Review Count: {data.restaurants[index].review_count}</p>

<div class="container">
    <div class="row g-2 mb-4">
        {#each data.restaurants[index].image_urls as {S}}
            <div class="column">
                <img src="{S}" alt="restaurant"/>
            </div>
        {/each}
    </div>

    <div class="row">
        <div class="col-6">
            <button on:click={() => handleClick(true)}>Yes</button>
        </div>
        <div class="col-6">
            <button on:click={() => handleClick(false)}>No</button>
        </div>
    </div>
</div>


<style>
    img {
        /*margin: 0 auto;*/
        width: 100%;
    }


    h1 {
        font-family: 'Baloo 2 Variable', sans-serif;
        color: #890000;
        font-weight: 700;
        margin-top: 12px;
    }

    .row {
        display: flex;
        flex-wrap: wrap;
    }

    .column {
        flex: 26%;
        /*max-width: 26%;*/
        padding: 0 4px;
    }

    button {
        width: 100%;
    }
</style>