import {isLoading} from "../../../../store";
let pin: any;

export const actions = {
    default: async ({cookies,request}) => {

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

        console.log(JSON.stringify(responseBody.vote_count));

        // vote_count is undefined when pin is incorrect
        const voteCount = responseBody.vote_count;

        isLoading.set(false);

        return {voteCount};


        // if (responseBody.vote_count > -1) {
        //     console.log("WE HAVE A VOTE COUNT");
        //     isLoading.set(false);
        //     return {voteCount};
        // }
        // else {
        //     console.log("NO VOTE COUNT");
        //     isLoading.set(false);
        //     return {voteCount};
        // }
    }
    catch (error) {
        isLoading.set(false);
        console.error('Error:', error);
    }
}


