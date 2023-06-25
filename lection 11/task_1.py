# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

try:
    #  Заходим на сайт 'https://sbis.ru/'
    driver.get("https://sbis.ru/")
    driver.maximize_window()
    assert driver.current_url == "https://sbis.ru/", 'Не верно открыт сайт'

    #  Переходим в раздел контакты, проверяем адрес и заголовок страницы
    button_txt = "Контакты"
    contacts_btn = driver.find_element(By.XPATH, "//a[text()='Контакты']")
    assert contacts_btn.is_displayed(), "Вкладка Контакты не отображается на странице"
    assert contacts_btn.text == button_txt, "Неверный текст вкладки Контакты"
    assert contacts_btn.get_attribute("href") == "https://sbis.ru/contacts", "Неверная ссылка у вкладки Контакты"
    contacts_btn.click()
    assert "https://sbis.ru/contacts" in driver.current_url
    sleep(1)

    # Находим баннер Тензора, проверяем его наличие, нажимаем
    banner_tensor = driver.find_element(By.CSS_SELECTOR, "[title='tensor.ru']")
    assert banner_tensor.is_displayed(), "Баннер Тензор не отображается"
    banner_tensor.click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'https://tensor.ru/', 'Неверный адрес страницы'

    # Проверяем, что есть блок "Сила в людях"
    block_tensor = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__card-title")
    driver.execute_script("return arguments[0].scrollIntoView(true);", block_tensor)
    assert block_tensor.is_displayed(), "Блок новости 'Сила в людях' не отображается"

    # Переходим в 'Подробнее' и убеждаемся, что открывается https://tensor.ru/about"
    more = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-link.tensor_ru-Index__link[href='/about']")
    driver.execute_script("arguments[0].scrollIntoView();", more)
    more.click()
    assert driver.current_url == "https://tensor.ru/about", "Неправильный адрес сайта"

finally:
    driver.quit()
