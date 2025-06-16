import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (make sure the appropriate driver is installed and in PATH)
driver = webdriver.Chrome()  # or use webdriver.Edge(), webdriver.Firefox(), etc.

# Navigate to the URL
driver.get("https://iengage.coforge.com/ess2/Login?_M=Yydn1IEXOr4=")

# Wait for the button to be clickable and click it
try:
    wait = WebDriverWait(driver, 10)
    # ad_login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ad-Credentials']")))
    Login_Via_Creds = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='login-card-footer-text cust-pt-2 grey-text mt-5 mb-0 logindiv']")))
    Login_Via_Creds.click()
    # driver.find_element_by_xpath("//*[@id='txtEmpCode']").send_keys("00123506")
    # driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("Gaga@Cof1")
    # Emp_Code = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='txtEmpCode']")
    # Emp_Code.click()

    print("Clicked the login button successfully.")
except Exception as e:
    print("Error:", e)
time.sleep(5)


wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='txtEmpCode']")))

# Enter Employee Code
driver.find_element(By.XPATH, "//*[@id='txtEmpCode']").send_keys("00123506")

# Wait briefly
time.sleep(2)

# Enter Password
driver.find_element(By.XPATH, "//*[@id='txtPassword']").send_keys("Gaga@Cof1")

wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='imgBtnOK']"))).click()

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[title='Attendance System']"))).click()




time.sleep(5)
# driver.quit()