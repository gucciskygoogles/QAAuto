from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytest
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class TestAutoMvideo:

    def test_search_in_and_choose(self, browser):
        browser.implicitly_wait(3)
        browser.get('https://www.mvideo.ru/')
        search_bar = browser.find_element(By.ID, '1')
        search_bar.send_keys('iphone')
        search_bar.send_keys(Keys.RETURN)
        first_res = browser.find_element(By.CSS_SELECTOR, '.product-cards-layout__item:nth-child(1) .product-title__text')
        first_res.click()
        browser.find_element(By.CLASS_NAME, 'mv-main-button--content').click()

    def test_find_store(self, browser):
        browser.set_window_size(1936, 1056)
        browser.get('https://www.mvideo.ru/')
        browser.find_element(By.XPATH, '//a[contains(.,"Магазины")]').click()
        time.sleep(3)
        search_stores = browser.find_element(By.ID, 'frm-search-store')
        search_stores.click()
        search_stores.send_keys('кольцо')
        search_stores.send_keys(Keys.RETURN)
        time.sleep(4)
        assert 'кольцо' in browser.page_source
        time.sleep(3)
        
    def test_premium_catalog(self, browser):
        browser.set_window_size(1936, 1056)
        browser.get('https://www.mvideo.ru/')
        browser.find_element(By.CLASS_NAME, 'catalog-button').click()
        time.sleep(3)
        browser.find_element(By.LINK_TEXT, 'Premium').click()


class TestKinopoiskUI:

    def test_find_film(self, browser):

        browser.set_window_size(1936, 1056)
        browser.get('https://www.kinopoisk.ru/')
        search = browser.find_element(By.NAME, 'kp_query')
        search.click()
        search.send_keys('Она')
        search.send_keys(Keys.RETURN)
        assert 'Она' in browser.page_source