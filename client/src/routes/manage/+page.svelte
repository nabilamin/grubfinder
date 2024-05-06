<script>
    import {goto} from "$app/navigation";
    import sanitizeHtml from 'sanitize-html';

    let session = "";
    let pin = "";

    let sessionError = '';
    let pinError = '';

    /**
     * Perform HTML sanitization of text input by the user
     */
    function sanitizeInput() {
        const sanitizedSession = sanitizeHtml(session);
        const sanitizedPin = sanitizeHtml(pin);

        return {
            sanitizedSession,
            sanitizedPin
        };
    }

    /**
     * Validates that user input fields are formatted properly
     */
    function validateInput() {
        // Input validation
        let valid = true;
        if (session === '' || session.length !== 6 || !/^\d+$/.test(session)){
            sessionError = 'Please enter a 6-digit numerical session code';
            valid = false;
        }
        if (pin === '' || pin.length !== 4 || !/^\d+$/.test(pin)) {
            pinError = 'Please enter a 4-digit numerical pin';
            valid = false;
        }
        return valid;
    }

    /**
     * Sends form data to the backend Using custom request since we want to show
     * loading screen before POST-ing form data
     */
    const handleSubmit = async () => {
        // Reset error messages
        sessionError = '';
        pinError = '';

       const valid = validateInput();
        if (!valid) {
            return;
        }
        
        const {sanitizedSession, sanitizedPin} = sanitizeInput();

        let params = new URLSearchParams();
        params.append("sessionPin", sanitizedPin);
        params.append("sessionId", sanitizedSession);


        const response = await fetch(`/session/${session}/manage`, {
            method: 'POST',
            body: params
        });

        const responseBody = await response.json();
        if(responseBody.status === 200)
            await goto(`/session/${session}/manage`)
    };
</script>

<div class="container">
    <div class="row">
        <div class="col">
            <div class="content-title">
                <h1>Manage a Session</h1>
            </div>
            <div class="form">
                <form id="manage-form" on:submit|preventDefault={handleSubmit}>
                    <div class="row justify-content-center">
                        <!--SESSION CODE INPUT-->
                        <div class="col-md-auto mb-4">
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
                            {#if sessionError}
                                <div class="error-message">{sessionError}</div>
                            {/if}
                        </div>
                        <!--PIN INPUT-->
                        <div class="col-md-auto mb-4">
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
                            {#if pinError}
                                <div class="error-message">{pinError}</div>
                            {/if}
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

    .error-message {
        color: #890000;
        font-size: 0.8em;
        margin-top: 2px;
        position: absolute;
        padding-left: 13px;
        position : relative;
        max-width: 100%;
    }

</style>