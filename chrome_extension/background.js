chrome.runtime.onInstalled.addListener(function() {
    chrome.storage.sync.set({color: '#3aa757'}, function() {
      console.log('Hit me background page clicked');
    });
  });

  chrome.extension.onConnect.addListener(function(port) {
    console.log("Connected .....");
    const socket = io("http://localhost:8080");
    console.log("button clicked!");
    socket.emit("message", "HELLO WORLD from background.js");
    socket.on("message", function(data) {
      var today = new Date();
      var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
      console.log(data);
      port.postMessage(data);
    });
    port.onMessage.addListener(function(msg) {
         console.log("message recieved" + msg);
         port.postMessage("Hi Popup.js");
    });

    
})