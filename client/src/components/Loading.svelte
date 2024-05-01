<style>
    .container {
        display: flex;          /* Establishes a flex container */
        flex-direction: column; /* Stacks children vertically */
        align-items: center;    /* Centers children horizontally in the container */
        justify-content: center; /* Optionally centers children vertically if needed */
        margin-top: 100px;      /* Adds spacing at the top */
        text-align: center;     /* Ensures text elements are also centered */
    }
    
    .loading-spinner {
        border: 5px solid #f3f3f3;
        border-top: 5px solid #890000;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        animation: spin 2s linear infinite;
        margin-bottom: 20px; /* Keeps space between the spinner and the text/button below it */
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
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
    
    <script>
        import {isLoading} from '../store.js';
    
        function goBack() {
            isLoading.set(false);
            window.location.href = "#";
        }
    </script>
    
    <div class="container">
        <div class="loading-spinner"></div>
        <p>Please wait while we find your session...</p>
        <button type="button" class="pill-button" on:click={goBack}>Go Back</button>
    </div>