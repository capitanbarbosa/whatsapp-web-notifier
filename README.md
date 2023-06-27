# Method 1: Capture Console Output in Node.js

The browser script uses window.postMessage to send console messages as custom messages to the browser.
In the Node.js app, a headless browser automation library like Puppeteer is used to launch a headless browser, navigate to the target webpage, and capture console messages using the console event.
The Node.js app can process the received console messages and perform further actions.

# Method 2: Relay Messages via WebSocket

The browser script establishes a WebSocket connection to a WebSocket server running in the Node.js app.
Unread message information is sent from the browser as WebSocket messages using the browser's built-in WebSocket API.
The Node.js app sets up a WebSocket server using the ws library, receives the WebSocket messages, and processes them.
The Node.js app can perform further processing or relay the received messages to other parts of the application.
In summary, Method 1 captures console output from the browser and retrieves it in the Node.js app using Puppeteer, while Method 2 establishes a WebSocket connection between the browser and the Node.js app to relay messages in real-time. The choice between the two methods depends on your specific use case and requirements.
