import {json} from "@sveltejs/kit";

export async function POST({request, cookies, params}) {
    const sessionId = params.slug;

    console.log("Server side POST handler -> " + sessionId);
    const response = await endSession(sessionId);

    return json(response);
    // return json({message: "test",status: 200});
}

// Function to create a session with the user input
async function endSession(sessionId: string) {
    try {
        const response = await fetch(`https://api.grubfinder.io/session/${sessionId}/end`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: ""
        });

        const responseBody = await response.json();

        if (response.ok)
            console.log('Session ended successfully with id: ' + sessionId);
        else
            console.log('Error: Session end failed');

        return responseBody;
    }
    catch (e) {
        console.log("ERR -> " + e);
    }
}