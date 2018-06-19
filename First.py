from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#user = ""
#pwd = ""
#driver = webdriver.Firefox()
#driver = webdriver.Ie("C:\\Users\\mrkhan\\Desktop\\IEDriver\\IEDriverServer.exe")
driver = webdriver.Ie()
driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F%3Fgws_rd%3Dssl&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
assert "Google" in driver.title
#elem = driver.find_element_by_id("email")
#elem.send_keys(user)
#elem = driver.find_element_by_id("pass")
#elem.send_keys(pwd)
#elem.send_keys(Keys.RETURN)
#driver.close()
