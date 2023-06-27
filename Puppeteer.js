const puppeteer = require("puppeteer");

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  // Enable console messages
  await page.on("console", async (msg) => {
    const consoleOutput = await Promise.all(
      msg.args().map((arg) => arg.jsonValue())
    );
    if (consoleOutput.length > 0 && consoleOutput[0].type === "unreadMessage") {
      const unreadMessage = consoleOutput[0].message;
      console.log("Unread message received:", unreadMessage);
      // Process the unread message in your Node.js app
    }
  });

  // Navigate to the target webpage
  await page.goto("https://web.whatsapp.com"); // Replace with the URL of your target webpage

  // Keep the Node.js app running
  await new Promise(() => {});
})();
