import {json} from "@sveltejs/kit";
export async function POST({request, cookies, params}) {
        const data = await request.json();
        const session = data.session;
        const pin = data.pin;

        console.log("Server side -> " + session + " " + pin);
        // store cookie

        return json({status: 200});
}