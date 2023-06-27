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
        console.log(`(${title}): ${span.textContent}`);
      });
    }
  });
}

function recursiveCheck() {
  checkUnreadMessages();
  setTimeout(recursiveCheck, 5000); // Recursive call after 21 seconds (21000 milliseconds)
}

recursiveCheck(); // Start the recursive checking

// Optional: Stop the recursive checking after a specific duration (e.g., 5 minutes)
setTimeout(() => {
  clearInterval(recursiveCheck);
}, 300000); // Stop after 5 minutes (300000 milliseconds)
