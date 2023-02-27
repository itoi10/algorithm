import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By


def main():

    driver = init_driver()
    time.sleep(3)
    try:
        # ChatGPTのログインページにアクセス
        driver.get("https://chat.openai.com/auth/login")
        time.sleep(10)
        # ログインボタン押下
        driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//button[text()="Log in"]'))
        time.sleep(1)

        email = input("Emailを入力してください:")
        password = input("Passwordを入力してください:")

        # Email入力
        driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(email)
        time.sleep(1)
        # Continue押下
        driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//button[text()="Continue"]'))
        time.sleep(1)
        # Password入力
        driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(password)
        time.sleep(1)
        # Continue押下
        driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//button[text()="Continue"]'))
        time.sleep(1)

        time.sleep(30)

    finally:
        driver.quit()


def init_driver() -> uc.Chrome:
    """WebDriverの初期化を行う"""
    options = uc.ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--lang=ja")
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver = uc.Chrome(options=options)
    driver.implicitly_wait(3)
    driver.delete_all_cookies()
    return driver


if __name__ == "__main__":
    main()
