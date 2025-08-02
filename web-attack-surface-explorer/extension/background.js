chrome.webRequest.onCompleted.addListener(
  function(details) {
    if (details.url.startsWith('http')) {
      fetch("http://localhost:5000/collect", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          url: details.url,
          method: details.method,
          type: details.type,
          statusCode: details.statusCode,
          initiator: details.initiator
        })
      });
    }
  },
  { urls: ["<all_urls>"] },
  []
);
