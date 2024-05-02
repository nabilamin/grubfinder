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
        <p>Please wait while we work on your voting session...</p>
    </div>