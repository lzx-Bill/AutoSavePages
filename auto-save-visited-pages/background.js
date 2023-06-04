chrome.webNavigation.onCompleted.addListener(
    function (details) {
      // 延迟1秒以确保页面加载完成
      setTimeout(() => {
        postData(details.url);
      }, 1000);
    },
    { url: [{ urlMatches: "http://*/*" }, { urlMatches: "https://*/*" }] }
  );



function postData(url) {
    const endpoint = "http:localhost:5000/save_url";
    const data = { url: url };
  
    fetch(endpoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: new URLSearchParams(data),
    })
      .then((response) => {
        if (response.ok) {
          console.log("URL successfully sent to server:", url);
        } else {
          console.error("Error while sending URL to the server:", response.status);
        }
      })
      .catch((error) => {
        console.error("Network error:", error);
      });
  }