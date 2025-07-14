from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def check_sauce_demo_elements():
    # Настройка драйвера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Переход на страницу
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)  # Ожидание загрузки страницы

        # Поиск элементов
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        submit = driver.find_element(By.ID, "login-button")

        # Проверка наличия элементов
        if username and password and submit:
            print("Элементы найдены")
        else:
            print("Не все элементы найдены")

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        driver.quit()


# Вызов функции
if __name__ == "__main__":
    check_sauce_demo_elements()