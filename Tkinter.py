import pickle
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.edge.service import Service

# Rest of the code...

# Boolean variable to keep track of the visibility state of the list
list_visible = False


def update_display(results):
    # Clear the previous boxes
    for box in chat_boxes:
        box.destroy()
    chat_boxes.clear()

    # Create a box for each chat title
    for result in results:
        box = tk.Label(root, text=result, relief=tk.SOLID, borderwidth=1)
        box.pack(fill=tk.X, padx=10, pady=5)
        chat_boxes.append(box)


def toggle_list():
    global list_visible
    if list_visible:
        for box in chat_boxes:
            box.pack_forget()  # Hide the chat boxes
        list_visible = False
        # Reposition the window to the original coordinates
        root.geometry(f"+{window_x}+{window_y}")
    else:
        for box in chat_boxes:
            box.pack(fill=tk.X, padx=10, pady=5)  # Show the chat boxes
        list_visible = True
        # Reposition the window to the new coordinates
        root.geometry("+1126+1248")




# Set up the GUI
root = tk.Tk()
root.title("WhatsApp Unread Messages")

# -- Remove the title bar and make the window transparent
root.overrideredirect(True)
# root.attributes("-alpha", 0.8)

# Set the window geometry to position it at the specified location
window_x = 1090
window_y = 1405
root.geometry(f"+{window_x}+{window_y}")

# List to store the chat boxes
chat_boxes = []

# Set the path to the Microsoft Edge WebDriver executable
edge_driver_path = 'msedgedriver.exe'

# Specify the path to your default profile directory
profile_directory = 'C:\\Users\\luisd\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default'

# Specify the paths to the extensions you want to enable
extension_paths = [
    'C:\\Users\\luisd\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Extensions\\jmjcgjmipjiklbnfbdclkdikplgajhgc\\1.5.24_0.crx'
]

# Create a new Edge driver with your default profile
edge_options = webdriver.EdgeOptions()
edge_options.add_argument(f'--user-data-dir={profile_directory}')

# Add the extension paths to the browser options
for extension_path in extension_paths:
    edge_options.add_extension(extension_path)

driver = webdriver.Edge(service=Service(edge_driver_path), options=edge_options)

# Navigate to WhatsApp Web
driver.get('https://web.whatsapp.com')

try:
    # Load cookies from the previous session
    cookies = pickle.load(open("whatsapp_cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    # Refresh page after loading cookies
    driver.refresh()
except Exception as e:
    print(f"Error loading cookies: {e}")

# If this is the first time running the script, you'll need to manually scan the QR code
# Once you're logged in, save the cookies for the next session
pickle.dump(driver.get_cookies(), open("whatsapp_cookies.pkl", "wb"))


# Define JavaScript functions to check unread messages
js_code = """
function checkUnreadMessages() {
  const cellFrameContainers = document.querySelectorAll(
    'div[data-testid="cell-frame-container"]'
  );

  var unreadMessages = [];

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
        unreadMessages.push(`(${title}): ${span.textContent}`);
      });
    }
  });

  return unreadMessages;
}

return checkUnreadMessages();
"""


def check_messages():
    results = driver.execute_script(js_code)
    update_display(results)
    root.after(5000, check_messages)


# Create a button to toggle the list visibility
toggle_button = tk.Button(root, text="Toggle List", command=toggle_list)
toggle_button.pack(pady=10)

# Adjust initial display based on the initial state of list_visible
if not list_visible:
    for box in chat_boxes:
        box.pack_forget()  # Hide the chat boxes initially

# Start checking messages
check_messages()

# Run the GUI event loop
root.mainloop()
