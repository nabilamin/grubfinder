<script>
    import {goto} from "$app/navigation";
    import sanitizeHtml from 'sanitize-html';

    let session = "";
    let sessionError = '';

    /**
     * @param {string} session
     */
    function sanitizeInput(session) {
        const sanitizedSession = sanitizeHtml(session);

        return {
            sanitizedSession
        };
    }

    const handleSubmit = async (event) => {
        event.preventDefault(); // Prevent default form submission
        // Reset error message
        sessionError = '';

        // Input validation
        let valid = true;
        if (session === '' || session.length !== 6 || !/^\d+$/.test(session)){
            sessionError = 'Please enter a 6-digit numerical session code';
            valid = false;
            console.log("Invalid session code");
        }
        if (!valid) {
            return;
        }

        const {sanitizedSession} = sanitizeInput(session);

        let params = new URLSearchParams();
        params.append("sessionId", sanitizedSession);

        // POST form data
        const response = await fetch(`/session/${session}/manage`, {
            method: 'POST',
            body: params
        });

        const responseBody = await response.json();

        if(responseBody.status === 200)
            goto(`/session/${session}/vote`)
    };
</script>

<div class="container">
    <div class="row">
        <div class="col">
            <div class="content-title">
                <h1>Enter Session Code</h1>
            </div>
            <div class="form">
            <form id="manage-form" on:submit={handleSubmit}>
                        <label for="sessionCode" class="visually-hidden form-label">Session Code</label>
                        <input style="text-align:center" type="text" class="form-control" id="category" placeholder="Session Code"
                       aria-label="Location"
                       aria-describedby="session-configuration"
                        bind:value={session}>
                        {#if sessionError}
                            <div class="error-message">{sessionError}</div>
                        {/if}
                <button class="pill-button" type="submit">Join Session</button>
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
    form {
        margin-left: 40%;
        margin-right:40%;
        width: 20%;
        padding: 37px;
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
