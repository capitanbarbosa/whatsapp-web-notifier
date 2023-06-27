// Create a function to check for unread messages
function checkUnreadMessages() {
  // Find all cell-frame-container elements on the page
  const cellFrameContainers = document.querySelectorAll(
    'div[data-testid="cell-frame-container"]'
  );

  // Iterate over each container
  cellFrameContainers.forEach((container) => {
    // Find any spans with aria-label containing "unread message" or "unread messages"
    const unreadSpans = container.querySelectorAll(
      'span[aria-label*="unread message"], span[aria-label*="unread messages"]'
    );

    // If there are unread spans, print a message for each occurrence
    if (unreadSpans.length > 0) {
      unreadSpans.forEach((span) => {
        console.log("Unread message found:", span.textContent);
      });
    }
  });
}

// Create a MutationObserver instance
const observer = new MutationObserver(checkUnreadMessages);

// Observe changes within the document body and its descendants
observer.observe(document.body, { subtree: true, childList: true });

// Initial check for unread messages
checkUnreadMessages();
