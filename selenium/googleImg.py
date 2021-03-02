from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

crawlingImgName = "아이유"
driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys(crawlingImgName)
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    image.click()
    # 2초 휴식
    time.sleep(2)
    # imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
    imgUrl = driver.find_element_by_xpath(
        "//*[@id='Sva75c']/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img").get_attribute("src")
    urllib.request.urlretrieve(imgUrl, str(count) + crawlingImgName + ".jpg")
    count = count + 1

driver.close()

# images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
# count = 1
# for image in images:
#     image.click()
#     # 3초 휴식
#     time.sleep(3)
#     imgUrl = driver.find_element_by_css_selector(
#         ".n3VNCb").get_attribute("src")
#     urllib.request.urlretrieve(imgUrl, str(count) + "test.jpg")
#     count = count + 1
# driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click()
# # 3초 휴식
# time.sleep(3)

# # print(driver.find_element_by_css_selector(".n3VNCb").get_attribute("src"))
# imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")

# urllib.request.urlretrieve(imgUrl, "test.jpg")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
