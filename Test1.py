import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Corrected instantiation using Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


# Navigate to the URL
driver.get("https://iengage.coforge.com/ess2/Login?_M=Yydn1IEXOr4=")

try:
    wait = WebDriverWait(driver, 20)
    Login_Via_Creds = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='login-card-footer-text cust-pt-2 grey-text mt-5 mb-0 logindiv']")))
    Login_Via_Creds.click()
    print("Clicked the login button successfully.")
except Exception as e:
    print("Error:", e)

time.sleep(15)

wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='txtEmpCode']")))
driver.find_element(By.XPATH, "//*[@id='txtEmpCode']").send_keys("00123506")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='txtPassword']").send_keys("Gaga@Cof1")
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='imgBtnOK']"))).click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[title='Attendance System']"))).click()

time.sleep(5)
driver.quit()
