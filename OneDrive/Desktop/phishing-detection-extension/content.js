// content.js

// Listen for messages from the background script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "alertPhishing") {
      showPhishingAlert(request.url);
    }
  });
  
  // Function to display an alert for phishing attempts
  function showPhishingAlert(url) {
    // Create a visual alert (you can customize this to fit your design)
    const alertDiv = document.createElement("div");
    alertDiv.style.position = "fixed";
    alertDiv.style.top = "10px";
    alertDiv.style.right = "10px";
    alertDiv.style.backgroundColor = "red";
    alertDiv.style.color = "white";
    alertDiv.style.padding = "10px";
    alertDiv.style.zIndex = "9999";
    alertDiv.innerText = `Phishing Alert! Possible phishing link detected: ${url}`;
  
    // Add a close button
    const closeButton = document.createElement("button");
    closeButton.innerText = "X";
    closeButton.style.marginLeft = "10px";
    closeButton.style.color = "white";
    closeButton.style.backgroundColor = "transparent";
    closeButton.style.border = "none";
    closeButton.style.cursor = "pointer";
    
    // Close button functionality
    closeButton.onclick = function () {
      alertDiv.remove();
    };
  
    alertDiv.appendChild(closeButton);
    document.body.appendChild(alertDiv);
  }
  
  // Example: Add visual cues to suspicious links
  document.querySelectorAll("a").forEach(link => {
    // You can implement more complex logic to identify suspicious links
    if (link.href.includes("login") || link.href.includes("verify")) {
      link.style.border = "2px solid red"; // Highlight suspicious links
      link.title = "Warning: This link may be phishing!"; // Add a tooltip
    }
  });
  