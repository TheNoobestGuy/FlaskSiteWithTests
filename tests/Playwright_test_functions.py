import asyncio
import requests
from playwright.async_api import async_playwright

async def register(page, user, mail, password1, password2):
    try:
        await asyncio.sleep(1)

        # Go to registration window
        registration = await page.wait_for_selector('#registrationButton')
        await registration.click()
        await asyncio.sleep(1)

        # Check spreadsheet
        username = await page.wait_for_selector('#username')
        email = await page.wait_for_selector('#email')
        pass1 = await page.wait_for_selector('#pass1')
        pass2 = await page.wait_for_selector('#pass2')

        await username.type(user)
        await email.type(mail)
        await pass1.type(password1)
        await pass2.type(password2)
        await asyncio.sleep(1)

        # Pass registration
        submit = await page.wait_for_selector('.sendReg')
        await submit.click()
        await asyncio.sleep(1)

        # Close registration window if open
        closeVis = await page.is_visible('.registrationClose')
        if closeVis:
            close = await page.wait_for_selector('.registrationClose')
            await close.click()

        # Check does user is registered successfully
        try:
            response = requests.get('http://127.0.0.1:5000/Data')

            if response.status_code == 200:
                data = response.json()
                registered = False

                if len(data["RegisteredUsers"]) != 0:
                    for i in data["RegisteredUsers"]:
                        if i[0] == user and i[1] == mail and i[2] == password1:
                            registered = True
                   
                    if registered:
                        print('Successfully registered!')
                    else:
                        print('Failed to register!')
                else:
                    print('Failed to register!')
            else:
                print("Failed to register! Error:", response.status_code)
        except:
            print('Propably failed to register! Cannot check database!')
    except:
        print('Failed to register!')


async def login(page, emial, password):
    try:
        await asyncio.sleep(1)

        # Go to login window
        log = await page.wait_for_selector('#loginButton')
        await log.click()
        await asyncio.sleep(1)

        # Check spreadsheet
        emailLog = await page.wait_for_selector('#emailLogin')
        passLog = await page.wait_for_selector('#passLogin')

        await emailLog.type(emial)
        await passLog.type(password)
        await asyncio.sleep(1)

        # Pass login
        submit = await page.wait_for_selector('.sendLog')
        await submit.click()
        await asyncio.sleep(1)

        # Close login window if open
        closeVis = await page.is_visible('.loginClose')
        if closeVis:
            close = await page.wait_for_selector('.loginClose')
            await close.click()
        
        # Check does user is logged successfully
        try:
            response = requests.get('http://127.0.0.1:5000/Data')

            if response.status_code == 200:
                data = response.json()
                
                if len(data["Logged"]) != 0:
                    print('Successfully loged in!')
                else:
                    print('Failed to log in! Propably there is no such account!')
            else:
                print('Failed to log in! Cannot check database!')
        except:
            print('Failed to log in! Propably there is no such account!')
    except:
        print('Failed to log in!')

async def createRecipe(page, name, ingredient, step):
    try:
        await asyncio.sleep(1)

        # Go to create recipe page
        createPage = await page.wait_for_selector('#createRecipe')
        await createPage.click()
        await asyncio.sleep(1)

        # Check all buttons to create recipe
        addIngredient = await page.wait_for_selector('#addIngredient')
        removeIngredient = await page.wait_for_selector('#removeIngredient')
        addStep = await page.wait_for_selector('#addStep')
        removeStep = await page.wait_for_selector('#removeStep')

        await addIngredient.click()
        await asyncio.sleep(1)

        await addStep.click()
        await asyncio.sleep(1)

        await removeIngredient.click()
        await asyncio.sleep(1)

        await removeStep.click()
        await asyncio.sleep(1)

        # Check all textboxes
        recipeName = await page.wait_for_selector('#recipeName')

        await recipeName.fill(name)
        await asyncio.sleep(1)

        ingredientFill = await page.wait_for_selector('#textareaIngredients')
        await ingredientFill.fill(ingredient)
        await asyncio.sleep(1)

        stepFill = await page.wait_for_selector('#textareaSteps');
        await stepFill.fill(step)
        await asyncio.sleep(1)

        # Sumbit recipe
        submit = await page.wait_for_selector('#finish')
        await submit.click()
        await asyncio.sleep(1)

        # Go back to home page
        homePage = await page.wait_for_selector('#home')
        await homePage.click()
        await asyncio.sleep(1)

        print('Successfully created recipe!')
    except:
        print('Failed to create recipe!')

async def checkRecipesList(page):
    try:
        await asyncio.sleep(1)

        # Go to recipes list page
        listPage = await page.wait_for_selector('#favoriteRecipe')
        await listPage.click()
        await asyncio.sleep(1)

        # Check does recipe is clickable
        recipe = await page.wait_for_selector('#recipeButton')
        await recipe.click()
        await asyncio.sleep(1)

        # Go back to home page
        homePage = await page.wait_for_selector('#home')
        await homePage.click()
        await asyncio.sleep(1)

        print('Successfully checked recipes list!')
    except:
        print('Failed to check recipes list!')