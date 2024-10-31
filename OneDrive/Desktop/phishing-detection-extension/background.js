// background.js

// Listener for web requests to monitor URLs
chrome.webRequest.onBeforeRequest.addListener(
    function (details) {
      // Check if the request URL is potentially a phishing attempt
      const url = details.url;
      
      // Basic URL pattern check (you may implement a more advanced check)
      if (isPhishingURL(url)) {
        // Log the phishing attempt (you can also show notifications)
        console.log("Phishing attempt detected: ", url);
        
        // Send a message to the content script to notify the user
        chrome.tabs.sendMessage(details.tabId, { action: "alertPhishing", url: url });
      }
    },
    { urls: ["<all_urls>"] }, // Match all URLs
    ["blocking"] // Allows us to block the request if needed
  );
  
  // Function to determine if a URL is likely phishing
  function isPhishingURL(url) {
    // Add your logic for detecting phishing URLs here
    const phishingIndicators = [
      /login/i, // Common keyword in phishing URLs
      /secure/i, // Often used in phishing
      /verify/i, // Frequently used in phishing attempts
      // Add more patterns as necessary
    ];
  
    return phishingIndicators.some(pattern => pattern.test(url));
  }
  
  // Listener for messages from the popup or content scripts
  chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "getPhishingReports") {
      // Retrieve and send reports of phishing attempts (if any)
      const reports = getPhishingReports(); // Function to fetch stored reports
      sendResponse({ reports: reports });
    }
  });
  
  // Function to simulate fetching phishing reports (implement your storage logic)
  function getPhishingReports() {
    // For simplicity, returning a static report, but implement storage as needed
    return [
      { url: "http://example-phishing.com", timestamp: Date.now() },
      { url: "http://malicious-site.com", timestamp: Date.now() },
    ];
  }
  