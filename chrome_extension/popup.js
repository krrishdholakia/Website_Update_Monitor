let hitBtn = document.getElementById('hitBtn');
console.log("button clicked!");

var port = chrome.extension.connect({
  name: "Sample Communication"
});
port.postMessage("Hi BackGround");
port.onMessage.addListener(function(msg) {
  console.log("message recieved" + msg);
  chrome.browserAction.setBadgeText({text: "10+"});
});

hitBtn.onclick = function(element) {
  const socket = io("http://localhost:8080");
  console.log("button clicked!");
  initial_run = true
  while (initial_run) {
    socket.emit("message", "HELLO WORLD from extension");
    socket.on("message", function(data) {
    var today = new Date();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    console.log(data);
    document.getElementById("hitBtn").innerHTML = data
    document.getElementById("further_information").innerHTML = "value last updated at: " + time; 
    chrome.browserAction.setBadgeText({text: "10+"});
    });
    initial_run = false
  }
  setInterval(function() {
    console.log("button clicked!");
    socket.emit("message", "HELLO WORLD from extension");
    socket.on("message", function(data) {
      var today = new Date();
      var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
      console.log(data);
      document.getElementById("hitBtn").innerHTML = data
      document.getElementById("further_information").innerHTML = "value last updated at: " + time; 
    });
  }, 70000)
  
};
