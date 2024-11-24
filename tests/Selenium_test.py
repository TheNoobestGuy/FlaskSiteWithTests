# Import classes
from Selenium_test_classes import *

# Driver definition
driver = webdriver.Edge()

# Test
try:
    # Open a website
    driver.get('http://127.0.0.1:5000')

    # Initialize tests
    register = Registration(driver)
    login = Login(driver)
    makeRecipe = MakeRecipe(driver)
    checkList = CheckList(driver)

    # Tests
    register.validation("12.80s", "@@netfaskpl", "11111111", "11111111")
    register.register("maciek", "aerobat@onet.pl", "11111111", "11111111")
    login.validation("%R@onet.pl", "11111111")
    login.login("aerobat@onet.pl", "11111111")
    makeRecipe.makeRecipe("Tomato soup", "Tomato", "Stir tomato")
    checkList.checkList()

finally:
    driver.quit()