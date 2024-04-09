<div class="container">
    <div class="row">
        <div class="col">
            <div class="content-title">
                <h1>Enter Session Code</h1>
            </div>
            <div class="form">
            <form action="session/1234/vote" method="POST">
                    <label for="sessionCode" class="visually-hidden form-label">Session Code</label>
                    <input style="text-align:center" type="text" class="form-control" id="category" placeholder="Session Code"
                   aria-label="Location"
                   aria-describedby="session-configuration">
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
</style>
