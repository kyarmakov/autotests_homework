# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

url = 'https://test-sso.sbis.ru/auth-online/?ret=test-online.sbis.ru'
login = 'Демо_тензор'
password = 'Демо123'
dialogs = 'https://test-online.sbis.ru/page/dialogs'
message = 'test message'

driver = webdriver.Chrome()

try:
    # Переходим на сайт https://test-sso.sbis.ru
    driver.get(url)
    driver.maximize_window()
    sleep(1)

    # Авторизуемся
    login_input = driver.find_element(By.XPATH, "(//*[contains(@class, 'controls-Field')])[1]")
    login_input.send_keys(login, Keys.ENTER)

    password_input = driver.find_element(By.XPATH, "(//*[contains(@class, 'controls-Field')])[2]")
    password_input.send_keys(password, Keys.ENTER)
    sleep(10)

    # Переходим в реестр Контакты
    contacts = driver.find_element(By.XPATH, "//span[text()='Контакты']")
    action_chains = ActionChains(driver)
    action_chains.double_click(contacts).perform()

    sleep(3)

    assert driver.current_url == dialogs

    items = driver.find_elements(By.XPATH, "(//div[@data-qa='items-container'])[4]/div[@data-qa='item']")
    items_before = len(items)

    # Отправляем сообщение самому себе
    add_btn = driver.find_element(By.CSS_SELECTOR, "[data-name='sabyPage-addButton']")
    add_btn.click()

    sleep(5)
    person = driver.find_element(By.XPATH, "(//span[ text()='Иванов Егор'])[2]")
    person.click()

    sleep(3)
    textbox = driver.find_element(By.XPATH, "//div[@role='textbox']")
    textbox.send_keys(message)

    send_btn = driver.find_element(By.CSS_SELECTOR, "[data-qa='msg-send-editor__send-button']")
    send_btn.click()
    close_btn = driver.find_element(By.CSS_SELECTOR, "[data-qa='controls-stack-Button__close']")
    close_btn.click()

    sleep(3)
    # Убеждаемся, что сообщение появилось в реестре
    items = driver.find_elements(By.XPATH, "(//div[@data-qa='items-container'])[4]/div[@data-qa='item']")
    items_after = len(items)
    assert items_after - items_before == 1

    # Удаляем сообщение и убеждаемся, что удалили
    new_message = driver.find_element(By.XPATH, "((//div[@data-qa='items-container'])[4]/div[@data-qa='item'])[1]")

    action_chains = ActionChains(driver)
    action_chains.context_click(new_message)
    action_chains.perform()

    delete_btn = driver.find_element(By.CSS_SELECTOR, "div[data-qa='cell'] div[title='Перенести в удаленные']")
    delete_btn.click()
    sleep(2)

    items = driver.find_elements(By.XPATH, "(//div[@data-qa='items-container'])[4]/div[@data-qa='item']")
    items_after_delete = len(items)

    assert items_before - items_after_delete == 0

finally:
    driver.quit()
