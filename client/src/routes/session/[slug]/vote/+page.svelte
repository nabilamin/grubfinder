<script lang="ts">
    export let data;

    export let dataLength = data.restaurants.length;

    export let index = 0;

    export let votingData = new Map<string, boolean>();

    function handleClick(value: boolean) {
        votingData.set(data.restaurants[index].id, value);

        if (index + 1 == dataLength) {
            console.log(votingData);
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