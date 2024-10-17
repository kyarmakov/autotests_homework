# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://sbis.ru/'
tensor_about = 'https://tensor.ru/about'

driver = webdriver.Chrome()

try:
    driver.get(url)
    driver.maximize_window()

    # Находим ссылку Контакты и переходим по ней
    contacts_link = driver.find_element(By.CSS_SELECTOR, "a[href='/contacts']")
    contacts_link.click()

    # Находим баннер Тензор и кликаем по нему
    tensor_banner = driver.find_element(By.CSS_SELECTOR, "div#contacts_clients a[href='https://tensor.ru/']")
    tensor_banner.click()

    # Переключаемся на вкладку сайта Тензор
    driver.switch_to.window(driver.window_handles[-1])
    sleep(1)

    # Находим блок 'Сила в людях', скроллим до него и проверяем, что он отображается
    block = driver.find_element(By.XPATH, "//p[text()='Сила в людях']")
    driver.execute_script('return arguments[0].scrollIntoView(true)', block)
    assert block.is_displayed()

    # Переходим в этом блоке в "Подробнее" и убеждаемся, что открывается https://tensor.ru/about
    about_link = driver.find_element(By.CSS_SELECTOR, "div.tensor_ru-Index__block4-bg a[href='/about']")
    about_link.click()
    assert driver.current_url == tensor_about

except Exception as e:
    print(e)

finally:
    driver.quit()
