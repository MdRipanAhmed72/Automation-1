import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def Login_valid_function_test():
    # STEP1 FOR THE TEST
    driver = webdriver.Firefox ()
    driver.maximize_window ()

    driver.get ( "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login" )
    time.sleep ( 20 )

    User_name = driver.find_element ( By.NAME , "username" )
    User_name.send_keys ( "Admin" )

    User_pasword = driver.find_element ( By.NAME , "password" )
    User_pasword.send_keys ( "admin123" )

    Login_button = driver.find_element ( By.CSS_SELECTOR , ".orangehrm-login-button" )
    Login_button.click ()
    time.sleep ( 20 )
    driver.close ()




def test_fast_one_invliad_issue():
    driver = webdriver.Firefox()
    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(20)

    User_name = driver.find_element(By.NAME, "username")
    User_name.send_keys("Admin12")

    User_pasword = driver.find_element(By.NAME, "password")
    User_pasword.send_keys("admin1234")

    Login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
    Login_button.click()
    time.sleep(5)
    # driver.close ()
    error_massage = driver.find_element(By.CSS_SELECTOR, ".oxd-alert-content-text")
    actual_error_massage_text = error_massage.text

    expected_error_massage = "Invalid credentials"

    if expected_error_massage == actual_error_massage_text:
        print("lgin failed.error_massage:" +expected_error_massage)

    else:
        print("did not get:"+ expected_error_massage)

    driver.close()

test_fast_one_invliad_issue()