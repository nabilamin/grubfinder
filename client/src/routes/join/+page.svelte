


<div class="container">
    <div class="content-title">
        <h1>Enter Lobby Code</h1></div>
    <form action="/Loading" method="POST">
        <div class="form-group">
            <label for="lobbyCode">Lobby Code:</label>
            <input type="text" id="lobbyCode" name="lobbyCode" required>
        </div>
        <input type="submit" value="Join Lobby">
    </form>
</div>
<p><a href="/loading">loading</a></p>

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
      padding: 10px 20px;
      border-radius: 50px; 
      text-decoration: none;
      font-family: 'Baloo 2 Variable', sans-serif;
      font-size: 16px;
      cursor: pointer;
    }
  </style>
