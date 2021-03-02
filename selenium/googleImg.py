from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("hdc 현대산업개발")
elem.send_keys(Keys.RETURN)
driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click()
# 3초 휴식
time.sleep(3)

# print(driver.find_element_by_css_selector(".n3VNCb").get_attribute("src"))
imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")

urllib.request.urlretrieve(imgUrl, "test.jpg")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
