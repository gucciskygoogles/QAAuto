from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.parametrize('transfer_protocol', ['http', 'https'])
class TestAutoMvideo:

    @pytest.mark.xfail
    @pytest.mark.find_something
    def test_search_in_and_choose(self, browser, transfer_protocol):
        browser.implicitly_wait(3)
        browser.get(f'{transfer_protocol}://www.mvideo.ru/')
        search_bar = browser.find_element(By.ID, '1')
        search_bar.send_keys('iphone')
        search_bar.send_keys(Keys.RETURN)
        first_res = browser.find_element(By.CSS_SELECTOR, '.product-cards-layout__item:nth-child(1) .product-title__text')
        first_res.click()
        browser.find_element(By.CLASS_NAME, 'mv-main-button--content').click()

    @pytest.mark.with_assert
    def test_find_store(self, browser, transfer_protocol):
        browser.set_window_size(1936, 1056)
        browser.get(f'{transfer_protocol}://www.mvideo.ru/')
        browser.find_element(By.XPATH, '//a[contains(.,"Магазины")]').click()
        time.sleep(3)
        search_stores = browser.find_element(By.ID, 'frm-search-store')
        search_stores.click()
        search_stores.send_keys('кольцо')
        search_stores.send_keys(Keys.RETURN)
        time.sleep(4)
        assert 'кольцо' in browser.page_source
        time.sleep(3)

    @pytest.mark.find_something
    def test_premium_catalog(self, browser, transfer_protocol):
        browser.set_window_size(1936, 1056)
        browser.get(f'{transfer_protocol}://www.mvideo.ru/')
        browser.find_element(By.CLASS_NAME, 'catalog-button').click()
        time.sleep(3)
        browser.find_element(By.LINK_TEXT, 'Premium').click()


@pytest.mark.parametrize('transfer_protocol', ['http', 'https'])
class TestKinopoiskUI:

    @pytest.mark.with_assert
    def test_find_film(self, browser, transfer_protocol):
        browser.set_window_size(1936, 1056)
        browser.get(f'{transfer_protocol}://www.kinopoisk.ru/')
        search = browser.find_element(By.NAME, 'kp_query')
        search.click()
        search.send_keys('Она')
        search.send_keys(Keys.RETURN)
        assert 'Она' in browser.page_source