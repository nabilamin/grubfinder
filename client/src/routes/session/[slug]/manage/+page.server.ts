import {isLoading} from "../../../../store";

let pin: any;

export const actions = {
    default: async ({cookies, request}) => {

        const data = await request.formData();
        // const sessionId = data.get("sessionId");
        const sessionPin = data.get("sessionPin");

        pin = sessionPin;
        // console.log("Server side -> " + session + " " + pin);

        // Enhancement: store cookie

        return {"success": true};
    }
};

export async function load({params}) {
    try {
        isLoading.set(true);
        const response = await fetch(`https://api.grubfinder.io/session/${params.slug}`,
            {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': pin
                },
            });

        if (response.ok)
            console.log(`Successfully retrieved session with id: ${params.slug}`);
        else
            console.log('Error: Getting session failed');

        const responseBody = await response.json();

        // console.log(JSON.stringify(responseBody));

        // vote_count is undefined when pin is incorrect
        const voteCount = responseBody.vote_count;
        const sessionIsClosed = responseBody.is_closed;
        const winningRestaurantId = responseBody.winning_restaurant_id;

        if (sessionIsClosed && winningRestaurantId) {
            try {
                const restaurantResponse =
                    await fetch(`https://api.grubfinder.io/session/${params.slug}/restaurant/${winningRestaurantId}`, {
                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                    });

                if (response.ok)
                    console.log(`Successfully fetched winning restaurant with id: ${winningRestaurantId}`);
                else
                    console.log('Error: Getting session failed');

                const restaurantResponseBody = await restaurantResponse.json();

                const hasDelivery = restaurantResponseBody.has_delivery;
                const rating = restaurantResponseBody.rating;
                const reviewCount = restaurantResponseBody.review_count;
                const restaurantName = restaurantResponseBody.name;
                const restaurantAddress = restaurantResponseBody.address;

                return {
                    voteCount,
                    sessionIsClosed,
                    restaurantAddress,
                    restaurantName,
                    reviewCount,
                    rating,
                    hasDelivery
                };
            }
            catch (e) {
                isLoading.set(false);
                console.error('Error: ', e);
            }
        }
        else {
            return {voteCount, sessionIsClosed};
        }

        isLoading.set(false);


    }
    catch (error) {
        isLoading.set(false);
        console.error('Error:', error);
    }
}


