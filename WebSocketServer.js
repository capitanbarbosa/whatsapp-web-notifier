const WebSocket = require("ws");

// Create a WebSocket server
const wss = new WebSocket.Server({ port: 3000 }); // Choose the desired port

// WebSocket connection event
wss.on("connection", (ws) => {
  console.log("WebSocket connected");

  // WebSocket message event
  ws.on("message", (message) => {
    console.log("Received message:", message);
    // Process the received message or relay it to other parts of your Node.js app
  });

  // WebSocket close event
  ws.on("close", () => {
    console.log("WebSocket disconnected");
  });
});
