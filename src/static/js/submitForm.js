function submitForm(event, submitBTNid, url) {
  // Prevent the default form submission
  event.preventDefault();

  // Disable the button and change its text to "Loading"
  const submitButton = document.getElementById(submitBTNid);
  submitButton.disabled = true;
  submitButton.textContent = "Updating..";

  // Serialize the form data
  const formData = new FormData(event.target);

  // Send a fetch POST request to the server
  fetch(url, {
    method: "POST",
    body: formData,
  }).then(() => {
    // Re-enable the button and set its text back to "Update" when the request is completed
    submitButton.disabled = false;
    submitButton.textContent = "Update";
  });
}
document.addEventListener("DOMContentLoaded", function () {
  const tabButtons = document.querySelectorAll(".tab-button");
  const tabContents = document.querySelectorAll(".tab-content");

  tabButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const tab = button.dataset.tab;

      tabButtons.forEach((btn) => {
        if (btn === button) {
          button.classList.remove("hover:bg-secondary");
          btn.classList.add("bg-primary");
        } else {
          btn.classList.remove("bg-primary");
          button.classList.add("hover:bg-secondary");
        }
      });

      tabContents.forEach((content) => {
        content.style.display = content.dataset.tab === tab ? "block" : "none";
      });
    });
  });
});
