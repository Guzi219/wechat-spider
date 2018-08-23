from time import sleep

from selenium import webdriver

# firefox_profile = webdriver.FirefoxProfile(r'C:\Users\guyongping\AppData\Roaming\Mozilla\Firefox\Profiles\m9xbudt5.default')
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

firefox_profile = webdriver.FirefoxProfile(r'C:\Users\guyongping\AppData\Roaming\Mozilla\Firefox\Profiles\gtsjcul8.default')
binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
# driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver = webdriver.Firefox(firefox_profile=firefox_profile)
print '123'
driver.get("https://www.baidu.com")
print '345'
# js = 'window.open("https://www.baidu.com","a")'
# driver.execute_script(js)
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
sleep(1.3)
driver.close()