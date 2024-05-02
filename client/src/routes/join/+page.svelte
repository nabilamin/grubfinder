<script>
    import {goto} from "$app/navigation";

    let session = "";

    const handleSubmit = async () => {
        let params = new URLSearchParams();
        params.append("sessionId", session);

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
        display: flex;          /* Establishes a flex container */
        flex-direction: column; /* Stacks children vertically */
        align-items: center;    /* Centers children horizontally in the container */
        justify-content: center; /* Optionally centers children vertically if needed */
        margin-top: 100px;      /* Adds spacing at the top */
        text-align: center;     /* Ensures text elements are also centered */
    }
</style>
