import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Set to False for debugging
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

# Initialize driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the URL
driver.get("https://iengage.coforge.com/ess2/Login?_M=Yydn1IEXOr4=")

# Wait for full page load
WebDriverWait(driver, 20).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
)

try:
    wait = WebDriverWait(driver, 20)
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='login-card-footer-text cust-pt-2 grey-text mt-5 mb-0 logindiv']")))
    login_button.click()
    print("Clicked the login button successfully.")
except Exception as e:
    print("Error clicking login button:", e)

time.sleep(5)

# Retry logic for finding the EmpCode field
max_retries = 3
retry_delay = 5
element_found = False

for attempt in range(max_retries):
    try:
        wait = WebDriverWait(driver, 20)
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#txtEmpCode')))
        print("Element found!")
        element_found = True
        break
    except Exception as e:
        print(f"Attempt {attempt + 1} failed: {e}")
        if attempt < max_retries - 1:
            print(f"Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
        else:
            print("Element not found after multiple attempts.")
            driver.save_screenshot("debug_screenshot.png")
            with open("page_source_debug.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            driver.quit()
            raise

if element_found:
    driver.find_element(By.XPATH, "//*[@id='txtEmpCode']").send_keys("00123506")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='txtPassword']").send_keys("Gaga@Cof1")
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='imgBtnOK']"))).click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[title='Attendance System']"))).click()
    time.sleep(5)

driver.quit()
