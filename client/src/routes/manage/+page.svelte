<script>
    import {goto} from "$app/navigation";

    let session = "";
    let pin = "";

    //Using custom request since we want to show loading screen before POST-ing form data
    const handleSubmit = async () => {
        let params = new URLSearchParams();
        params.append("sessionPin", pin);
        params.append("sessionId", session);

        // POST form data
        const response = await fetch(`/session/${session}/manage`, {
            method: 'POST',
            body: params
        });

        const responseBody = await response.json();

        if(responseBody.status === 200)
            goto(`/session/${session}/manage`)
    };


    // Commented out as one option for passing posting form data
    // const handleSubmit = async () => {
    //
    //     const response = await fetch("?/", {
    //         method: 'POST',
    //         headers: {
    //             'Content-Type': 'application/json'
    //         },
    //         body: JSON.stringify({session, pin})
    //     });
    //
    //     const responseBody = await response.json();
    //
    //     if(responseBody.status === 200) {
    //         goto(`/session/${session}/manage`)
    //     }
    // };
</script>

<div class="container">
    <div class="row">
        <div class="col">
            <div class="content-title">
                <h1>Manage a Session</h1>
            </div>
            <div class="form">
<!--                Saved the following commented out lines for learning-->
<!--                <form on:submit|preventDefault="{handleSubmit}">-->
<!--                <form action="?/validate" method="POST">-->
<!--                <form action="/session/{session}/manage" method="POST">-->
                <form id="manage-form" on:submit={handleSubmit}>

                    <div class="row justify-content-center">
                        <div class="col-md-auto">
                            <label for="sessionCode" class="visually-hidden form-label">Session Code</label>
                            <input style="text-align:center"
                                   type="text"
                                   class="form-control"
                                   id="category"
                                   placeholder="Enter a Session Code"
                                   aria-label="Location"
                                   aria-describedby="session-configuration"
                                   name="sessionId"
                                   bind:value={session} />
                        </div>

                        <div class="col-md-auto">
                            <label for="userPin" class="visually-hidden form-label">User Pin</label>
                            <input style="text-align:center"
                                   type="text"
                                   class="form-control"
                                   id="category"
                                   placeholder="Enter a User Pin"
                                   aria-label="Location"
                                   aria-describedby="session-configuration"
                                   name="sessionPin"
                                   bind:value={pin} />
                        </div>

                    </div>
                    <button class="pill-button" type="submit">Manage Session</button>
                </form>
            </div>
        </div>
    </div>
</div>

<style>
    .content-title {
        font-family: 'Baloo 2 Variable', sans-serif;
        color: #890000;
        font-weight: 700;
        margin-top: 12px;
    }

    .pill-button {
        display: inline-block;
        background-color: #890000;
        color: white;
        margin-top: 15px;
        padding: 10px 20px;
        border-radius: 50px;
        text-decoration: none;
        font-family: 'Baloo 2 Variable', sans-serif;
        font-size: 16px;
        cursor: pointer;
        border: none;
    }
</style>