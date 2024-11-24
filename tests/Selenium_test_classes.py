# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Registration:
    def __init__(self, driver):
        self.__driver = driver
        self.__registrationButton = None
        self.__username = None
        self.__email = None
        self.__firstpassword = None
        self.__secondpassword = None
        self.__submit = None
        self.__close = None
        self.__error = None

    def register(self, username, email, firstpassword, secondpassword):
        try:
            # Show registration window
            self.__registrationButton = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'registrationButton')))
            self.__registrationButton.click()

            # Get text boxes from registration
            self.__username = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'username')))

            self.__email = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'email')))

            self.__firstpassword = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'pass1')))

            self.__secondpassword = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'pass2')))

            self.__submit = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'sendReg')))

            # Register
            self.__username.send_keys(username)
            self.__email.send_keys(email)
            self.__firstpassword.send_keys(firstpassword)
            self.__secondpassword.send_keys(secondpassword)
            self.__submit.click()

            try:
                alert = WebDriverWait(self.__driver, 10).until(EC.alert_is_present())
                alert.accept()

                try:
                    try:
                        self.__close = self.__driver.find_element(By.CLASS_NAME, 'registrationClose')
                    except:
                        self.__close = None

                    if self.__close.is_displayed():
                        self.__close.click()
                            
                        print("Couldnt register! Possibly your account already exist!")
                    else:
                        print("Successfully registered!")
                except:
                    print("Successfully registered!")
            except:
                print("Couldnt register!")
        except:
            raise Exception('Couldnt register!')
        
    def validation(self, username, email, firstpassword, secondpassword):
        try:
            # Show registration window
            self.__registrationButton = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'registrationButton')))
            self.__registrationButton.click()

            # Get text boxes from registration
            self.__username = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'username')))

            self.__email = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'email')))

            self.__firstpassword = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'pass1')))

            self.__secondpassword = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'pass2')))

            self.__submit = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'sendReg')))

            # Register
            self.__username.send_keys(username)
            self.__email.send_keys(email)
            self.__firstpassword.send_keys(firstpassword)
            self.__secondpassword.send_keys(secondpassword)
            self.__submit.click()

            try:
                alert = WebDriverWait(self.__driver, 10).until(EC.alert_is_present())
                alert.accept()

                try:
                    try:
                        self.__close = self.__driver.find_element(By.CLASS_NAME, 'registrationClose')
                    except:
                        self.__close = None

                    if self.__close.is_displayed():
                        self.__close.click()
                            
                        print("Validation of registration finished successfully!")
                    else:
                        print("Validation of registration doesn't work!")
                except:
                    print("Validation of registration doesn't work!")
            except:
                print("Validation of registration doesn't work!")
        except:
            raise Exception("Validation of registration doesn't work!")

class Login:
    def __init__(self, driver):
        self.__driver = driver
        self.__loginButton = None
        self.__email = None
        self.__password = None
        self.__submit = None
        self.__close = None

    def login(self, email, password):
        try:
            # Show login window
            self.__loginButton = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'loginButton')))
            self.__loginButton.click()
            
            # Get text boxes from login window
            self.__email = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'emailLogin')))

            self.__password = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'passLogin')))

            self.__submit = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'sendLog')))

            # Log in
            self.__email.send_keys(email)
            self.__password.send_keys(password)
            self.__submit.click()

            try:
                alert = WebDriverWait(self.__driver, 10).until(EC.alert_is_present())
                alert.accept()

                try:
                    try:
                        self.__close = self.__driver.find_element(By.CLASS_NAME, 'loginClose')
                    except:
                        self.__close = None

                    if self.__close.is_displayed():
                        self.__close.click()
                        print("Couldnt log in! Possibly you are not registered!")
                    else:
                        print("Successfully loged in!")
                except:
                    print("Successfully loged in!")
            except:
                print("Couldnt log in!")
        except:
            raise Exception('Couldnt log in!')
        
    def validation(self, email, password):
        try:
            # Show login window
            self.__loginButton = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'loginButton')))
            self.__loginButton.click()
            
            # Get text boxes from login window
            self.__email = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'emailLogin')))

            self.__password = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'passLogin')))

            self.__submit = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'sendLog')))

            # Log in
            self.__email.send_keys(email)
            self.__password.send_keys(password)
            self.__submit.click()

            try:
                alert = WebDriverWait(self.__driver, 10).until(EC.alert_is_present())
                alert.accept()

                try:
                    try:
                        self.__close = self.__driver.find_element(By.CLASS_NAME, 'loginClose')
                    except:
                        self.__close = None

                    if self.__close.is_displayed():
                        self.__close.click()
                        print("Validation of login finished successfully")
                    else:
                        print("Validation of login doesn't work!")
                except:
                    print("Validation of login doesn't work!")
            except:
                print("Validation of login doesn't work!")
        except:
            raise Exception("Validation of login doesn't work!")

class MakeRecipe:

    def __init__(self, driver):
        self.__driver = driver
        self.__createRecipe = None
        self.__addIngredient = None
        self.__removeIngredient = None
        self.__addStep = None
        self.__removeStep = None
        self.__recipeName = None
        self.__ingredientTextBox = None
        self.__stepTextBox = None
        self.__finishButton = None
        self.__home = None

    def makeRecipe(self, name, ingredient, step):
        try:
            # Go to create recipe
            self.__createRecipe = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'createRecipe')))
            self.__createRecipe.click()

            # Check all buttons that are available
            self.__addIngredient = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'addIngredient')))
            self.__addIngredient.click()

            self.__removeIngredient = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'removeIngredient')))
            self.__removeIngredient.click()

            self.__addStep = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'addStep')))
            self.__addStep.click()

            self.__removeStep = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'removeStep')))
            self.__removeStep.click()

            # Full fill text areas
            self.__recipeName = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'recipeName')))
            self.__recipeName.send_keys(name)

            self.__ingredientTextBox = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'textareaIngredients')))
            self.__ingredientTextBox.send_keys(ingredient)

            self.__stepTextBox = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'textareaSteps')))
            self.__stepTextBox.send_keys(step)

            # Click finish and accept alert
            self.__finishButton = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'finish')))
            self.__finishButton.click()

            alert = self.__driver.switch_to.alert
            alert.accept()

            # Go back to home
            self.__home = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'home')))
            self.__home.click()
            
            print("Successfully maded recipe!")
        except:
            raise Exception('Couldnt make a recipe!')

class CheckList:
    def __init__(self, driver):
        self.__driver = driver
        self.__list = None
        self.__recipesList = None

    def checkList(self):
        try:
            # Go to list of recipes
            self.__list = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'favoriteRecipe')))
            self.__list.click()
            
            # Check does recipe is added
            self.__recipesList = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'favoriteUL')))
            recipes = self.__recipesList.find_elements(By.TAG_NAME, "li")

            if len(recipes) != 0:
                try:
                    recipeButton = self.__recipesList.find_element(By.TAG_NAME, 'li')
                    recipeButton.click()

                    print("Successfully checked recipe list!")
                except:
                    print("Couldnt check does recipes has been added!")
            else:
                print("Successfully checked recipe list!")
        except:
            raise Exception('Couldnt check does recipes has been added!')
