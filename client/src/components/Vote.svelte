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
<button on:click={() => handleClick(true)}>Yes</button>
<button on:click={() => handleClick(false)}>No</button>

<style>

</style>
