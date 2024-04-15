<script> 
    function goBack() {
        if (document.referrer) {
          // If there's a referrer, go back to the previous page
          window.history.back();
        } else {
          // If there's no referrer, navigate to the homepage
          window.location.href = "/";
        }
      };
    </script> 
    
    <div> 
        <h2 class="content-title">404 Page Not Found</h2>
        <p>Looks Like You Lost Your Way</p>
        <button type="button" class="pill-button" on:click={goBack}>Go Back</button>
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
    