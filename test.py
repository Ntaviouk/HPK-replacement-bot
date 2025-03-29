from selenium import webdriver


def take_screenshot(url, screenshot_path):
    driver = webdriver.Chrome()

    try:
        driver.get(url)

        driver.execute_script("window.scrollTo(0, 1000);")

        # Робимо скріншот
        driver.save_screenshot(screenshot_path)

    except Exception as e:
        print(f"Помилка: {e}")

    finally:
        driver.quit()


url = 'https://hpk.edu.ua/replacements'
screenshot_path = r'C:\Users\dimas\PycharmProjects\HPK_telegram\Replacement API\screens\screenshot.png'

take_screenshot(url, screenshot_path)
