// Converted this form action to a post request end point in server.ts
// Keeping this for learning and future reference
// export const actions = {
//     validate: async ({cookies,request}) => {
//         const data = await request.formData();
//         const sessionId = data.get("sessionId");
//         const sessionPin = data.get("sessionPin");
//
//         console.log("Server side -> " + sessionId + " " + sessionPin);
//
//         // store cookie
//
//         return {"success": true};
//     }
// };