import {json} from "@sveltejs/kit";
import {page} from "$app/stores";

export async function POST({request, cookies, params}) {
    const votingData = await request.json();

    const sessionId = params.slug;

    console.log("Server side POST handler -> " + sessionId);
    const response = await submitVotes({sessionId, votingData});

    return json(response);
    // return json({message: "test",status: 200});
}

/**
 * @param {{ sessionId: any; votingData: any; }} data
 */
async function submitVotes(data: { sessionId: any; votingData: any; }) {
    console.log(JSON.stringify(data));
    try {
        const response = await fetch(`https://api.grubfinder.io/session/${data.sessionId}/vote`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data.votingData)
        });

        const responseBody = await response.json();

        if (response.ok)
            console.log('Session ended successfully with id: ' + data.sessionId);
        else
            console.log('Error: Session end failed');

        return responseBody;
    }
    catch (e) {
        console.log("ERR -> " + e);
    }
}