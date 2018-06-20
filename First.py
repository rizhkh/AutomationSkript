from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.by import *
from selenium.webdriver.common.keys import Keys
user = "###"
pwd = "###"
#driver = webdriver.Firefox()
#driver = webdriver.Ie("C:\\Users\\mrkhan\\Desktop\\IEDriver\\IEDriverServer.exe")
#driver = webdriver.Chrome()
driver = webdriver.Chrome()
driver.get("http://###:###@###/###/")

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

ab = driver.find_element_by_xpath('//*[@id="navTabGroupDiv"]/span[3]')
ab.click()
element = driver.find_element_by_xpath('//*[@id="Tabnav_Project"]')

#Makes sure that you are paying attention
numb = input("enter 1 to continue? ")
if(numb=='1'):
    if(driver.find_element_by_xpath('//*[@id="Tabnav_Project"]/a')):
        a1 = driver.find_element_by_xpath('//*[@id="Tabnav_Project"]/a')
        a1.click()
        a2 = driver.find_element_by_xpath('//*[@id="Tabnav_Project"]/a')
        a2.click()


numb = input("enter 1 to continue to utility? ")
if (numb == '1'): ## MAKE SURE YOU MOVE TO UTILITY ACCOUNT MANUALLY
    if (wait(driver, 4).until(EC.frame_to_be_available_and_switch_to_it("contentIFrame0"))):
        #driver.switch_to.frame("contentIFrame0")
        driver.switch_to.default_content()
        wait(driver, 4).until(EC.frame_to_be_available_and_switch_to_it("contentIFrame0"))
        #driver.switch_to.frame(driver.find_element_by_id("contentIFrame0"))
        #wait(driver, 4).until(EC.frame_to_be_available_and_switch_to_it("contentIFrame0"))
        #wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="contentIFrame0"]')))
        searchbarclick = driver.find_element_by_id('crmGrid_SavedNewQuerySelector')
        driver.switch_to.default_content()
        #Goes to the clickable frame
        wait(driver, 4).until(EC.frame_to_be_available_and_switch_to_it("contentIFrame1")) #all clickables are in frame1
        #Clicks the search bar to enter something
        searchbarclick2 = driver.find_element_by_id("crmGrid_findCriteriaButton")
        searchbarclick2.click()
        time.sleep(5)
        searchbarclick = driver.find_element_by_xpath('//*[@id="crmQuickFindTD"]/table')
        searchbarclick.click()
        #inputElement = driver.find_element_by_xpath('//*[@id="crmGrid_quickFindContainer"]')
        #This paste in the number into the form
        ################################
        ##########
        ##########
        ##########
        searchbarclick3 = driver.find_element_by_xpath('//*[@id="crmGrid_findCriteria"]')
        searchbarclick3.send_keys('6739540306')
        #searchbarclick.submit()
        searchbarclick2 = driver.find_element_by_id("crmGrid_findCriteriaButton")
        searchbarclick2.click()
        selAll = driver.find_element_by_xpath('//*[@id="crmGrid_gridBodyTable_checkBox_Image_All"]')
        selAll.click()


print ('outside x1')
driver.switch_to.default_content()
print ('Success x12')
tre = driver.find_element_by_xpath('//*[@id="trc_utilityaccount|NoRelationship|HomePageGrid|Mscrm.HomepageGrid.trc_utilityaccount.Edit"]/span/a/img')
print ('Success x2')
#edit.click()

print ('*******************')

#driver.close()
