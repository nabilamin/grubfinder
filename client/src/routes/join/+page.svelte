<div class="container">
    <div class="content-title">
        <h1>Enter Session Code</h1></div>
    <form action="session/1234/vote" method="POST">
        <div class="form-group">
            <label for="sessionCode">Session Code:</label>
            <input type="text" id="sessionCode" name="sessionCode" required>
        </div>
        <input class="pill-button" type="submit" value="Join Session">
    </form>
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
      padding: 10px 20px;
      border-radius: 50px; 
      text-decoration: none;
      font-family: 'Baloo 2 Variable', sans-serif;
      font-size: 16px;
      cursor: pointer;
    }
  </style>
