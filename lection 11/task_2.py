# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
login, password = 'glushevskaya1', 'glushevskaya1glushevskaya1'
user = 'Глушевская Лидия Сергеевна'
text = 'Вебинар 11 задание 2 - отправка и удаление сообщения'

try:
    # Авторизация на https://fix-online.sbis.ru/
    driver.get("https://fix-online.sbis.ru/")
    sleep(2)
    driver.find_element(By.NAME, 'Login').send_keys(login, Keys.ENTER)
    sleep(1)
    driver.find_element(By.NAME, 'Password').send_keys(password, Keys.ENTER)
    sleep(5)

    # Открытие раздела контакты
    driver.find_element(By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion__title"]').click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, '[name="headTitle"]').click()
    sleep(2)

    # Отправка сообщения самому себе
    driver.find_element(By.CSS_SELECTOR, '.icon-RoundPlus').click()
    sleep(2)
    driver.find_element(By.CLASS_NAME, 'controls-Search__nativeField_caretEmpty').send_keys(user, Keys.ENTER)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]').click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph').send_keys(text)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.icon-BtArrow').click()
    sleep(2)

    # Проверка наличия сообщения
    message = driver.find_element(By.CSS_SELECTOR, '.msg-entity-text')
    sleep(2)
    assert message.text == text, 'Сообщение не найдено'
    action_chains = ActionChains(driver)
    action_chains.move_to_element(message)
    action_chains.context_click(message)
    action_chains.perform()

    # Удаление сообщения и проверка удаления
    driver.find_element(By.CSS_SELECTOR, '[title="Перенести в удаленные"]').click()
    sleep(2)
    assert driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item__content-inner') != message, 'Сообщение не удалено!'
    sleep(2)

finally:
    driver.quit()
