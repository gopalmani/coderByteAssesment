import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  
    yield driver
    driver.quit()

def test_application_workflow(driver):
    # Step 1: Login to the website
    driver.get("https://staging3-akes.nexquare.io")
    username = driver.find_element(By.ID,"txtuser")
    password = driver.find_element(By.ID, "txtpassword")

    username.send_keys("S0075")
    password.send_keys("Abc!@1")
    password.send_keys(Keys.RETURN)

    # Verify that login was successful and landed on the Dashboard


    # Step 2: Go to 'Staff Profile Management' -> 'Staff Add'
    staff_management_menu = driver.find_element(By.ID,"hr")
    staff_management_menu.click()

    staff_add_name = driver.find_element(By.ID,"id","link_addStaff")
    staff_add_name.send_keys("Gopal Dubey")

    staff_add_employee_type = driver.find_element(By.ID,"class_name","select-dropdown dropdown-trigge")
    staff_add_employee_type.click()
    staff_add_employee_type_value = driver.get_element(By.ID,"select-options-68a2569f-6aff-c944-2ee2-aed39cbe71330")
    staff_add_employee_type_value.click()
    staff_add_dob = driver.find_element(By.ID, "dob")
    staff_add_dob.click()
    dob_value = driver.find_element_by_class_name("ui-state-default")
    dob_value.click()
    staff_add_joiningDate = driver.find_element(By.ID,"id","joinDate")
    staff_add_joiningDate.click()
    jd_value = driver.find_element(By.CLASS_NAME,"ui-state-default")
    jd_value.click()
    staff_email = driver.find_element(By.ID,"email")
    staff_email.send_keys("abc@gmail.com")
    salary_start_date = driver.find_element(By.ID,"id","salaryStartDate")
    salary_start_date.click()
    salary_start_date_value = driver.get_element(BY.CLASS_NAME, "ui-state-default")
    salary_start_date_value.click()
    submit_button = driver.find_element(By.ID,"submitButton")
    submit_button.click()

    # Step 4: Go to 'Fee Configuration' and then 'Fee Collection'
    fee_configuration_menu = driver.find_element_by_xpath("//a[contains(text(), 'Fee Configuration')]")
    fee_configuration_menu.click()


    # Verify that we landed on the 'Fee Collection' page
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "fee_collection")))
    assert "Fee Collection" in driver.title

    # Step 5: Enter '200011312' into the 'Global Student Search' box and search
    search= driver.find_element_by_id("staffName")
    search.send_keys("200011312")
    search.send_keys(Keys.RETURN)

    # Step 6: Select a pending invoice under 'Payable' -> 'Pending Invoice' section
    pending_invoice_section = driver.find_element_by_id("pending_invoice_section")
    pending_invoice = pending_invoice_section.find_element_by_xpath("//tr[contains(@class, 'pending-invoice')]")
    pending_invoice.click()

    # Step 7: Choose the 'Payment Mode' under 'Payments' and click 'Pay' button
    payment_mode_dropdown = driver.find_element_by_id("payment_mode_dropdown")
    # Select the desired payment mode

    pay_button = driver.find_element_by_xpath("//button[contains(text(), 'Pay')]")
    pay_button.click()

    # Perform any additional assertions or actions as needed

