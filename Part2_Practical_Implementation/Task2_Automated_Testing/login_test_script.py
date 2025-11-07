from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Step 1: Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Step 2: Open a sample login page (you can replace this with your app)
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

# Step 3: Locate fields and fill in details
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")

# Step 4: Click login
driver.find_element(By.ID, "submit").click()

# Step 5: Wait and take a screenshot
time.sleep(3)
driver.save_screenshot("login_result.png")

# Step 6: Close browser
driver.quit()
print("✅ Test completed — screenshot saved as login_result.png")
