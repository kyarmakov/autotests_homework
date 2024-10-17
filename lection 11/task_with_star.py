# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import os
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://sbis.ru/'
download_path = os.path.join(os.getcwd())
plugin_name = 'sbisplugin-setup-web.exe'

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
}

options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)

try:
    driver.get(url)
    driver.maximize_window()

    # Находим ссылку 'Скачать локальные версии' и переходим по ней
    download_link = driver.find_element(By.CSS_SELECTOR, "a[href='/download']")
    download_link.click()

    # Находим плагин для Windows, скачиваем его и проверяем, что он скачался
    plugin = driver.find_element(By.XPATH, "//a[contains(@href, 'sbisplugin-setup-web.exe')]")
    plugin.click()

    wait_for = 20
    current = 0

    while current <= wait_for:
        time.sleep(1)
        if plugin_name in os.listdir(download_path):
            break

        if current == wait_for:
            assert False, 'Плагин не скачался'

        current += 1

    # Выводим на печать размер скачанного файла в мегабайтах
    print(round(os.path.getsize(os.path.join(download_path, plugin_name)) / (1024 * 1024), 2), 'MB')

except Exception as e:
    print(e)

finally:
    driver.quit()
