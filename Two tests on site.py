from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time



class AutoMvideo(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_search_in_and_choose(self):
        driver = self.driver
        driver.implicitly_wait(3)
        driver.set_window_size(1936, 1056)
        driver.get('https://www.mvideo.ru/')
        search_bar = driver.find_element_by_id('1')
        search_bar.send_keys('iphone')
        search_bar.send_keys(Keys.RETURN)
        first_res = driver.find_element_by_css_selector('.product-cards-layout__item:nth-child(1) .product-title__text')
        first_res.click()
        add_to_cart = driver.find_element_by_class_name('mv-main-button--content').click()


    def test_find_store(self):
        driver = self.driver
        driver.set_window_size(1936, 1056)
        driver.get('https://www.mvideo.ru/')
        stores_btn = driver.find_element_by_xpath('//a[contains(.,"Магазины")]').click()
        time.sleep(3)
        search_stores = driver.find_element_by_id('frm-search-store')
        search_stores.click()
        search_stores.send_keys('кольцо')
        search_stores.send_keys(Keys.RETURN)
        time.sleep(4)
        self.assertTrue('кольцо' in driver.page_source)
        time.sleep(3)
        
    def test_premium_catalog(self):
        driver = self.driver
        driver.set_window_size(1936, 1056)
        driver.get('https://www.mvideo.ru/')
        driver.find_element_by_class_name('catalog-button').click()
        time.sleep(3)
        driver.find_element_by_link_text('Premium').click()

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()

