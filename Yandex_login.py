from selenium import webdriver
from selenium.webdriver.common.by import By
from login_password import login, password

#   запускаем браузер
link = "https://yandex.ru/"
browser = webdriver.Chrome()
#   устанавливаем неявное ожидание
browser.implicitly_wait(10)
#   переходим по ссылке
browser.get(link)
try:
    # ищем кнопку "Войти", кликаем по ней
    browser.find_element(By.CSS_SELECTOR, "a.home-link.desk-notif-card__login-new-item.desk-notif-card__login-new-item_mail.home-link_black_yes > div.desk-notif-card__login-new-item-title").click()
    # Находим поле "логин" отправляем логин
    browser.find_element(By.ID, "passp-field-login").send_keys(login)
    # находим кнопку "Войти" кликаем по ней
    browser.find_element(By.ID, "passp:sign-in").click()
    # Находим поле "пароль" отправляем пароль
    browser.find_element(By.ID, "passp-field-passwd").send_keys(password)
    # находим кнопку "Войти" кликаем по ней
    browser.find_element(By.ID, "passp:sign-in").click()
finally:
    # закрываем браузер
    browser.quit()
