<script>
    import {goto} from "$app/navigation";
    import sanitizeHtml from 'sanitize-html';

    let session = "";
    let sessionError = '';

    /**
     * Perform HTML sanitization of text input by the user
     */
    function sanitizeInput() {
        return sanitizeHtml(session);
    }

    /**
     * Validates that user input fields are formatted properly
     */
    function  validateInput() {
        // Input validation
        let valid = true;
        if (session === '' || session.length !== 6 || !/^\d+$/.test(session)) {
            sessionError = 'Please enter a 6-digit numerical session code';
            valid = false;
        }
        return valid;
    }

    /**
     * Verify that session ID is properly formatted and correct, if so then add
     * user to the voting session.
     */
    const handleSubmit = async () => {
        // Reset error message
        sessionError = '';

        const valid = validateInput();
        if (!valid) {
            return;
        }

        const sanitizedSession = sanitizeInput();

        let params = new URLSearchParams();
        params.append("sessionId", sanitizedSession);

        // POST form data
        const response = await fetch(`/session/${session}/manage`, {
            method: 'POST',
            body: params
        });

        const responseBody = await response.json();

        if (responseBody.status === 200)
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
                <form id="manage-form" on:submit|preventDefault={handleSubmit}>
                    <label for="sessionCode" class="visually-hidden form-label">Session Code</label>
                    <input style="text-align:center"
                           type="text"
                           class="form-control"
                           id="category"
                           placeholder="Session Code"
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

    .container {
        display: flex; /* Establishes a flex container */
        flex-direction: column; /* Stacks children vertically */
        align-items: center; /* Centers children horizontally in the container */
        justify-content: center; /* Optionally centers children vertically if needed */
        margin-top: 10px; /* Adds spacing at the top */
        text-align: center; /* Ensures text elements are also centered */
    }

    .error-message {
        color: #890000;
        font-size: 0.8em;
        margin-top: 2px;
        position: absolute;
        padding-left: 13px;
        position: relative;
        max-width: 100%;
    }
</style>
