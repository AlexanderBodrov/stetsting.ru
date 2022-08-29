from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.fixture(scope="function")
def browser():
    # запускаем браузер
    browser = webdriver.Chrome()
    # устанавливаем неявное ожидание
    browser.implicitly_wait(10)
    # переходим по ссылке
    link = "https://www.google.com/"
    browser.get(link)
    # вводим данные "купить кофемашину bork c804" в поисковую строку и жмем Enter
    browser.find_element(By.CLASS_NAME, "gLFyf.gsfi").send_keys("купить кофемашину bork c804", Keys.ENTER)
    # выполняем тесты
    yield browser
    # закрываем браузер
    browser.quit()


def test1(browser):
    # находим элементы заголовков выдачи
    more10 = browser.find_elements(By.CSS_SELECTOR, "h3")
    # Прверяем, что в выдаче более 10 результатов
    assert len(more10) > 10


def test2(browser):
    # Проверяем, что в выдаче есть мВидео
    m_video = browser.find_element(By.XPATH, "//*[contains(text(), 'mvideo.ru')]").text
    assert "mvideo.ru" in m_video
