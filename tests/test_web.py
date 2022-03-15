import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
	driver = Chrome()
	driver.implicitly_wait(10)
	yield driver
	driver.quit()


def test_basic_duckduckgo_search(browser):
	URL = 'https://www.duckduckgo.com'
	PHRASE = 'panda'
	
	browser.get(URL)
	
	search_input = browser.find_element(By.ID, 'search_form_input_homepage')
	search_input.send_keys(PHRASE + Keys.RETURN)
	
	link_divs = browser.find_elements(By.CSS_SELECTOR, '#links > div')
	assert len(link_divs) > 0
	
	xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE}')]"
	results = browser.find_elements(By.XPATH, xpath)
	assert len(results) > 0
	
	search_input = browser.find_element(By.ID, 'search_form_input')
	assert search_input.get_attribute('value') == PHRASE

