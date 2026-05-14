//Function to self close alert message after a defined amount of time

document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        let messages = document.getElementById("msg");
        if (messages) {
            let alert = new bootstrap.Alert(messages);
            alert.close();
        }
    }, 8000);
});