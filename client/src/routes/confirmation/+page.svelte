
  <style>
    .container {
      text-align: center;
      margin-top: 50px;
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
    h1 {
      font-family: 'Baloo 2 Variable', sans-serif;
      color: #890000;
      font-weight: 700;
    }
  </style>
<script>
    // Function to navigate back to the home screen
    function goHome() {
      window.location.href = "/";
    }
  </script>
  
  <div class="container">
    <h1>Voting Complete</h1>
    <p>Check in with your host for the results.</p>
    <button class="pill-button" on:click={goHome}>Go to Home</button>
  </div>

