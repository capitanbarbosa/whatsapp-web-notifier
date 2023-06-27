import pickle
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

# Set the path to the Microsoft Edge WebDriver executable
edge_driver_path = 'msedgedriver.exe'

# Specify the path to your default profile directory
profile_directory = 'C:\\Users\\luisd\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default'

# Specify the paths to the extensions you want to enable
extension_paths = [
    # 'C:\\path\\to\\extension1',
'C:\\Users\\luisd\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Extensions\\jmjcgjmipjiklbnfbdclkdikplgajhgc\\1.5.24_0.crx'    # Add more extension paths if needed
# 'C:\\Users\\luisd\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Extensions\\jmjcgjmipjiklbnfbdclkdikplgajhgc\\1.5.24_0'
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

# Keep the browser window open indefinitely
while True:
    pass
