import {json} from "@sveltejs/kit";
export async function POST({request, cookies, params}) {
        const data = await request.json();

        console.log("Server side POST handler -> " + JSON.stringify(data));

        const response = await createSession(data);

        return json(response);
        // return json({message: "test",status: 200});
}

// Function to create a session with the user input
async function createSession(data: any) {
    data.open_at = "";
    // Put request to backend to create a session
    try {
        const response = await fetch('https://api.grubfinder.io/session/create', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const responseBody = await response.json();

        if (response.ok)
            console.log('Session created successfully with id: ' + JSON.stringify(responseBody));
        else
            console.log('Error: Session creation failed');

        return responseBody;
    }
    catch (error) {
        console.error('Error:', error);
    }
}