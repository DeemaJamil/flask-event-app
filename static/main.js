document.addEventListener("DOMContentLoaded", function() {

    const infoBtn = document.getElementById("info-btn");
    if (infoBtn) {
        infoBtn.addEventListener("click", function() {
            alert("Hello! You clicked the About Page button 🎉");
        });
    }


    const welcomeBtn = document.getElementById("welcome-btn");
    if (welcomeBtn) {
        welcomeBtn.addEventListener("click", function() {
            alert("Welcome to our Home Page! ");
        });
    }
});
