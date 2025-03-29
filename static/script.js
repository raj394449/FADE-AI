document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.getElementById("fileInput");
    const uploadForm = document.getElementById("uploadForm");
    const fileNameDisplay = document.getElementById("file-name");

    fileInput.addEventListener("change", function () {
        if (fileInput.files.length > 0) {
            fileNameDisplay.textContent = fileInput.files[0].name;
        }
    });

    uploadForm.addEventListener("submit", function (event) {
        if (fileInput.files.length === 0) {
            event.preventDefault();
            alert("Please select an image before submitting.");
        }
    });
});
