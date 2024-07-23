from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
import time

# Initialize the Edge driver
service = Service('C:\\Users\\PREMA\\msedgedriver.exe')
driver = webdriver.Edge(service=service)

# Open the URL
driver.get("https://www.saucedemo.com/")

# Display cookies before login
print("Cookies before login:")
cookies = driver.get_cookies()
for cookie in cookies:
    print(cookie)

# Perform login
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")  # replace with valid username
password.send_keys("secret_sauce")   # replace with valid password
login_button.click()

time.sleep(10)  # Wait for the page to load

# Display cookies after login
print("Cookies after login:")
cookies = driver.get_cookies()
for cookie in cookies:
    print(cookie)

# Perform logout
menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
menu_button.click()
time.sleep(2)
logout_link = driver.find_element(By.ID, "logout_sidebar_link")
logout_link.click()

time.sleep(5)  # Wait for the page to load

# Close the driver
driver.quit()

#Output:

#Cookies before login:
#Cookies after login:
#{'domain': 'www.saucedemo.com', 'expiry': 1721720576, 'httpOnly': False, 'name': 'session-username', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'standard_user'}

#Process finished with exit code 0