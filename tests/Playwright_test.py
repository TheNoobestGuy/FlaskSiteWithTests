from Playwright_test_functions import *

async def handle_dialog(dialog):
    await dialog.accept()

async def run(playwright):
    # Launch the browser
    browser = await playwright.chromium.launch(
        headless=False,
        executable_path='C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
    )
    page = await browser.new_page()

    # Listen for dialog events
    page.on('dialog', handle_dialog)
    await page.goto('http://127.0.0.1:5000')

    # Test
    await register(page, "Maciek", "aerobat@onet.pl", "11111111", "11111111")
    await login(page, "aerobat@onet.pl", "11111111")
    await createRecipe(page, "name", "ingredient", "step")
    await checkRecipesList(page)


    # Close the browser
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

if __name__ == '__main__':
    asyncio.run(main())