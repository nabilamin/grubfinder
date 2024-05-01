<script lang="ts">
    import {page} from "$app/stores";

    export let data: object;
    const restaurants = data.sessionRestaurants;
    const sessionExists = restaurants && restaurants.length > 0;
    // For testing
    // const restaurants = [{"has_delivery":true,"restaurant_id":"-urNLXq1RYUDAy5XCWLaqQ","rating":"4.2","has_pickup":true,"session_id":"454044","vote_count":"0","address":"133 N La Cienega Blvd Beverly Hills, CA 90211","name":"Fogo de Chão Brazilian Steakhouse","review_count":"6239","image_urls":["https://s3-media0.fl.yelpcdn.com/bphoto/S6vDblZAaS24bSCYzlBCbw/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/Lrsx5NNPH3mRPhHLH29CkA/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/iG55qCVZvB1Yy3do9aaDNQ/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/I4DYmV_vi9PbGy-vNFrL-w/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/lG2gaPv8np-ubxgwNxkVzA/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/FXU5eAj_4181UMMrnITzhg/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/2Y_cTU29jt-txVXnn_pwNA/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/QWGQN-TGcTl03WCH0Q6OTg/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/z7MrhlANS0NdcncwzYmesA/258s.jpg"]},{"has_delivery":true,"restaurant_id":"77wBjs8t-4hQTQv3vpzD5Q","rating":"4.2","has_pickup":false,"session_id":"454044","vote_count":"0","address":"300 S Doheny Dr Four Season Hotel Los Angeles, CA 90048","name":"Cabana Restaurant","review_count":"12","image_urls":["https://s3-media0.fl.yelpcdn.com/bphoto/NLwOcGMEwKrhPQD1GHgA_Q/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/X9hsKf9MRySVrOmsV1Ek-g/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/z_ldSOH6mh7JMVZDIcmaGg/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/L0slojvOKhdhW_KlSCsHog/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/06iZey-v6a_luWWX-1Jisw/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/Q2pt9jutDT0IC27T_-hr2Q/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/asFYyUeEFkMZyhSdZZe0AA/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/42dYdAHzIr9avX6cje8h8w/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/82j_ar9nwb4HY-aFki5BMQ/258s.jpg"]},{"has_delivery":false,"restaurant_id":"NL_4r564fLOiYQtm4fSXGQ","rating":"4.3","has_pickup":false,"session_id":"454044","vote_count":"0","address":"346 South Doheny Dr Los Angeles, CA 90048","name":"Four Seasons Sunday Brunch","review_count":"43","image_urls":["https://s3-media0.fl.yelpcdn.com/bphoto/1HzKM0g35g8PnTcT5M8X-A/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/3r6x_57PilLh36AvgRqj-w/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/5PxgRNiZke6FNqzAoLSJyQ/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/R0bVhdPl7IAqllk-tFLrcg/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/x4Jju4J8TaBKFHv9eYP93g/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/GU7ixUHawTACRt1JkNco2Q/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/CnbMiCoj7AiYaE08XvLJnA/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/z8QuB_fZhp3dOVh1bUaUqQ/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/rzkTauvUGqbUzDqIubwnHw/258s.jpg"]},{"has_delivery":true,"restaurant_id":"TRI4waA9FzpmX9IbAtGrXg","rating":"4","has_pickup":false,"session_id":"454044","vote_count":"0","address":"129 N La Cienega Blvd Beverly Hills, CA 90211","name":"Matsuhisa","review_count":"1245","image_urls":["https://s3-media0.fl.yelpcdn.com/bphoto/8w-nKs__QAkIgqHd0QYTbA/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/C0Na7Htq7fadQMwF451CHA/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/fvW79TaSIm0EP1Q76ERqSg/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/5utTi0qqXasqmzk4I6iUGA/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/xpt2sQ_l3agBfKud-rAGfg/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/jRlpUq0DDg2WD4Gn2Q43Hg/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/ZZotEOfz03JgxswJWWOUIw/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/_4af2WoKw6kdDbbnA4UCMg/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/Aek7NY69bzb5hm5YsMRQMw/258s.jpg"]},{"has_delivery":true,"restaurant_id":"ZfHO3reY56DliVYFtvDP1g","rating":"3.8","has_pickup":false,"session_id":"454044","vote_count":"0","address":"8879 W Pico Blvd Ste 4 Los Angeles, CA 90035","name":"Red Fish Kitchen","review_count":"59","image_urls":["https://s3-media0.fl.yelpcdn.com/bphoto/zr_0Xqk8dWQUXpbOfNpvuQ/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/mkwWpwd7NQZ1hJTJUrpwKw/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/hrcspUy_mo9tleWyIsELzg/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/BPxFfwEqh1hLT5qbMG9R_A/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/3k1IqXUrqeX7WK9pwCD1Cw/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/nixkQyAGpmATcDOOdoYAgQ/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/3Vl_J-ATu3_nAhUspNUfbg/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/C-hCwlHyIcGKfsdTnpTrOA/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/iO2gzc91OdSMX4LRPHQG2w/258s.jpg"]},{"has_delivery":true,"restaurant_id":"gkWJaWkV-NkgiDrr_EXPEA","rating":"4.4","has_pickup":false,"session_id":"454044","vote_count":"0","address":"265 S Robertson Blvd Beverly Hills, CA 90211","name":"Yasu Beverly Hills","review_count":"86","image_urls":["https://s3-media0.fl.yelpcdn.com/bphoto/oF1DJmjA-RdEnEcSIxxDUA/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/BIo-iWAD6HJVwxxt-vr__Q/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/0qCtQu8cGjY0G9kX75oBsg/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/M63mJqEKHvDcYE_yiVPWAA/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/plnqOkzEaA8NRhU5mkrXBQ/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/PXY6rBkV4qnoYuSvGuI3Hw/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/AQBxrNM3s_4KgK5u1zIFxw/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/d_LYJvsiEWNvBB_-e_Kk5g/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/uu-Z3D-T2qiwPm_52QD-8g/258s.jpg"]},{"has_delivery":true,"restaurant_id":"nAZHwJYXc9Wk0pWX0cZKhQ","rating":"4.2","has_pickup":true,"session_id":"454044","vote_count":"0","address":"9162 W Olympic Blvd Beverly Hills, CA 90212","name":"Sasabune Beverly Hills","review_count":"271","image_urls":["https://s3-media0.fl.yelpcdn.com/bphoto/2olC4c3mK0p1l_UWCVpcZA/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/17x7HEQS0ZKV42XhVqJx1Q/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/c_99RmCBwMWSOZFwYYQvMQ/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/T5pb1WKAJVKH2soLyJmGHw/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/foG7mBUactZ5zHaPx8OsPQ/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/6mB3bz1ofoRG2Qd14ufNIg/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/cIVjT1U7jadRTAPbFo-3Mg/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/i11Fkt789yvX0W9BF56OIA/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/MHEtltJZUWCIhzbDhZ-SWQ/258s.jpg"]},{"has_delivery":true,"restaurant_id":"q-EW9VbGiCgxDsMtBRF3LA","rating":"4","has_pickup":true,"session_id":"454044","vote_count":"0","address":"100 N La Cienega Blvd Beverly Hills, CA 90211","name":"Lawry's The Prime Rib - Beverly Hills","review_count":"4993","image_urls":["https://s3-media0.fl.yelpcdn.com/bphoto/eiK1IyjMp0vi9ke5G3MMOA/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/D2lTLoWBWX5mm9Nj3y1LLQ/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/WrMbaON8YNyM7jNntVBA7g/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/MXOSptWN1iPyNmN8u16bRw/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/lhX5xH8dqUG9UWz4SYzVaA/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/-jk8jjmOTkK3r4dtkFGEVQ/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/0hnYOrCtH1lUbiR2EIlWtQ/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/8TU4RNwmJVg8YhvprXyiPA/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/u0CgOAjT-cbDFuPj1PeLFQ/258s.jpg"]},{"has_delivery":true,"restaurant_id":"quDRbtVyZHsvVeEMe0K6zw","rating":"4.5","has_pickup":true,"session_id":"454044","vote_count":"0","address":"8486 W 3rd St Los Angeles, CA 90048","name":"Manpuku Japanese BBQ Dining - West Hollywood","review_count":"184","image_urls":["https://s3-media0.fl.yelpcdn.com/bphoto/J__CItWMuzEPPvIcKYpbTg/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/e4STfiyeE9HhL0a1f2EaKQ/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/JGhGYmqDfLv83qkoy4E6YA/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/U9GBw2FzyAaKc07Fqen6Rg/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/6vPwuRFaFmYILgx5ieAU9g/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/6ElwOfnxqaTYe7rmtEyyMw/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/q7Hvnmj1xMny-I-l4AAoSQ/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/e5upRGmjLnw13Mmp8VCWhg/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/h1ksDrWH-OTY1UOW1vIrdQ/258s.jpg"]},{"has_delivery":true,"restaurant_id":"vDHpZdx3QtQnrSZdDdXtdg","rating":"4.3","has_pickup":true,"session_id":"454044","vote_count":"0","address":"170 N La Cienega Blvd Beverly Hills, CA 90211","name":"Genwa Korean BBQ Beverly Hills","review_count":"897","image_urls":["https://s3-media0.fl.yelpcdn.com/bphoto/ftuQ5-uAJ8ec6gfLKqC25A/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/14s49ygEjVIASLtY-x5bhA/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/kzG1uns7UonyHaJBtVSfkQ/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/i-fgdJn4bhhRNYSnvBNNng/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/1ePfP0JH3GLIBrWdht4KHw/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/_BZzKmMAzWXPWWPb6mHvYw/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/zTKhxEIACyf4sEREixgYRg/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/E60cp1B3qxwU6fDEDB6mPA/258s.jpg","https://s3-media0.fl.yelpcdn.com/bphoto/LULRXoF-XvwwSqgU9W4n9A/258s.jpg"]}];

    let index: number = 0;
    let votingResponse = new Map<string, boolean>();

    async function handleClick(voterResponse: boolean) {
        votingResponse.set(restaurants[index].restaurant_id, voterResponse);

        // console.log("Adding " + JSON.stringify(restaurants[index]) + " - " + voterResponse);

        if (index + 1 == restaurants.length) {
            let votingData: {[key: string]: boolean} = {};
            votingResponse.forEach((val, key) => {
                votingData[key] = val;
            });

           const response = await fetch(`https://api.grubfinder.io/session/${$page.params.slug}/vote`,{
                method: "POST",
                headers: {
                    'Accept': '*/*',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(votingData)
            });

           const responseBody = await response.json();

            console.log("Request body is " + JSON.stringify(votingData));
            console.log("Response body is " + JSON.stringify(responseBody));


        } else {
            index++
        }
    }

    function goBack() {
        history.back();
    }
</script>

<!--<p>{JSON.stringify(restaurants)}</p>-->
{#if (sessionExists)}

    <h1>{restaurants[index].name}</h1>
    <p>Rating: {restaurants[index].rating}</p>
    <p>Review Count: {restaurants[index].review_count}</p>

    <div class="container">
        <div class="row g-2 mb-4">
            {#each restaurants[index].image_urls as url}
                <div class="column">
                    <img src="{url}" alt="restaurant"/>
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
{:else }
    <p>Invalid session id</p>
    <button type="button" class="pill-button" on:click={goBack}>Go Back</button>
{/if}


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

     .pill-button {
         display: inline-block;
         background-color: #890000;
         color: white;
         padding: 10px 20px;
         border-radius: 50px;
         text-decoration: none;
         font-family: 'Baloo 2 Variable', sans-serif;
         font-size: 16px;
         cursor: pointer;
     }

</style>