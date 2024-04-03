<style>  
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
body {
    font-family: 'Baloo 2 Variable', sans-serif;
    background-color: #f4f4f4;
}
.container {
    text-align: center;
    margin-top: 100px;
}
.loading-spinner {
    border: 5px solid #f3f3f3;
    border-top: 5px solid #890000;
    border-radius: 50%;
    width: 50px;
    height: 50px;
    animation: spin 2s linear infinite;
    margin-bottom: 20px;
    position: fixed;
    left: 49%;
    top: 30%;

}
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
</style>

<script> 
import { page } from '$app/stores';
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

<div class="container">
    <div class="loading-spinner"></div>
    <p>Please wait while we find your session...</p>
    <button type="button" class="pill-button" on:click={goBack}>Go Back</button>
</div>