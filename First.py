from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
#from selenium.webdriver.common.by import *
from selenium.webdriver.common.keys import Keys
user = "######"
pwd = "#########"
#driver = webdriver.Firefox()
#driver = webdriver.Ie("C:\\Users\\mrkhan\\Desktop\\IEDriver\\IEDriverServer.exe")
#driver = webdriver.Chrome()
driver = webdriver.Chrome()
driver.get("http://"######":"#########"@#####/######/")

#assert "Google" in driver.title
#elem = driver.find_element_by_id("buttonCancel")

#driver.findElement(By.cssSelector("a[href*='long']")).click();
#driver.find_element(By.L("navTourButtonText navTourSmallText navTourWhiteText")).click()
#driver.find_element(By.LINK_TEXT("No, ")).click();

#if(driver.switch_to().frame(driver.find_element(By.ID("InlineDialog_Iframe")))):
 #   print ('true')


#driver.find_element(By.CLASS_NAME("navTourCloseButton")).click()
#driver.switch_to().defaultContent()


#button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'buttonClose')));
#button.click();

#This basically switches to the inner Frame if it exists with that name
if(wait(driver, 4).until(EC.frame_to_be_available_and_switch_to_it("InlineDialog_Iframe"))):
    a = wait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it("InlineDialog_Iframe"))
    a=driver.find_element_by_id('buttonClose') #now it looks for the id if it exists clicks it which closes the popup
    a.click()
driver.switch_to.default_content()

element = driver.find_element_by_id('Tabnav_Project')
hover = Actionchains(driver).move_to_element(element)
hover.perform()

if (driver.find_element_by_xpath('//*[@id="trc_utilityaccount"]')):
    print ('Found it')


print ('*******************')

#driver.close()
