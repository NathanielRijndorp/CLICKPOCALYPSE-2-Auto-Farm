from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to the ChromeDriver executable
chrome_driver_path = r"C:\Users\nathan\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"  # Update this path

# Initialize the ChromeDriver service
service = Service(chrome_driver_path)

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service)

# Open the desired webpage
driver.get("https://minmaxia.com/c2/")  # Replace with your target URL

# Function to click an element by its ID
def click_element_by_id(element_id):
    try:
        # Wait until the element is clickable
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, element_id))
        )
        element.click()
    except Exception as e:
        print(f"Error: {e}")

# Function to crawl sub-panels and click based on text content
def crawl_and_click_subpanels(container_id, text_list):
    try:
        # Find the container
        container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, container_id))
        )
        
        # Find all sub-panels within the container
        sub_panels = container.find_elements(By.CLASS_NAME, "upgradeButton")
        
        for panel in sub_panels:
            # Check if the panel contains any of the specified text
            panel_text = panel.text
            for text in text_list:
                if text in panel_text:
                    print(f"Clicking on panel with text: {text}")
                    panel.click()
                    break
    except Exception as e:
        print(f"Error: {e}")

# Text strings to check for
text_strings = [
    "Level Up",
    "Equip All Item Upgrades",
    "Achievement",
    "Rare Item Drops",
    "More Item Drops",
    "Item Level Bonus",
    "More Treasure Chests",
    "Buy Monster Farm",
    "Harvest Rewards",
    "More Monsters",
    "More Gold Drops"
]

# Loop to click elements and crawl sub-panels every 1.5 seconds
try:
    while True:
        # Click the treasureChestLootButtonPanel element
        click_element_by_id("treasureChestLootButtonPanel")
        
        # Crawl through sub-panels and click based on text content
        crawl_and_click_subpanels("upgradeButtonContainer", text_strings)
        
        # Wait for 1.5 seconds before repeating
        time.sleep(1.5)
except KeyboardInterrupt:
    print("Auto-clicking stopped by user")

# Keep the browser open (you can manually close it when done)
input("Press Enter to close the browser...")
driver.quit()
