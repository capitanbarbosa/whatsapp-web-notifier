const { Builder, By } = require("selenium-webdriver");
const edge = require("selenium-webdriver/edge");

// Set the path to the Microsoft Edge browser executable
const edgePath = "./msedgedriver.exe";

async function startSelenium() {
  // Create a new Microsoft Edge instance
  let options = new edge.Options();
  options.setBinaryPath(edgePath);

  const driver = await new Builder()
    .forBrowser("MicrosoftEdge")
    .setEdgeOptions(options)
    .build();

  // Navigate to the desired URL
  await driver.get("your_link_here");

  // Execute the provided JavaScript code on the page
  await driver.executeScript(`
    function checkUnreadMessages() {
      const cellFrameContainers = document.querySelectorAll(
        'div[data-testid="cell-frame-container"]'
      );

      cellFrameContainers.forEach((container) => {
        const unreadSpans = container.querySelectorAll(
          'span[aria-label*="unread message"], span[aria-label*="unread messages"]'
        );
        const titleElement = container.querySelector(
          'div[data-testid="cell-frame-title"] span'
        );
        const title = titleElement ? titleElement.textContent : "Unknown Title";

        if (unreadSpans.length > 0) {
          unreadSpans.forEach((span) => {
            console.log(\`(${title}): \${span.textContent}\`);
          });
        }
      });
    }

    function recursiveCheck() {
      checkUnreadMessages();
      setTimeout(recursiveCheck, 5000); // Recursive call after 5 seconds
    }

    recursiveCheck(); // Start the recursive checking
  `);
}

// Start the Selenium script
startSelenium().catch(console.error);
