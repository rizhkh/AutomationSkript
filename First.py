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

numbers = [70547-50003]#, 1111111, 2222222, 3333333, 4444444]


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
        driver.switch_to.default_content()
        wait(driver, 4).until(EC.frame_to_be_available_and_switch_to_it("contentIFrame0"))
        searchbarclick = driver.find_element_by_id('crmGrid_SavedNewQuerySelector')
        driver.switch_to.default_content()
        #Goes to the clickable frame #############<------
        wait(driver, 4).until(EC.frame_to_be_available_and_switch_to_it("contentIFrame1")) #all clickables are in frame1
        #Clicks the search bar to enter something
        searchbarclick2 = driver.find_element_by_id("crmGrid_findCriteriaButton")
        searchbarclick2.click()
        time.sleep(5)
        searchbarclick = driver.find_element_by_xpath('//*[@id="crmQuickFindTD"]/table')
        searchbarclick.click()
        #This paste in the number into the form
        ################################
        ##########
        searchbarclick3 = driver.find_element_by_xpath('//*[@id="crmGrid_findCriteria"]')
        searchbarclick3.send_keys(numbers)
        searchbarclick2 = driver.find_element_by_id("crmGrid_findCriteriaButton")
        searchbarclick2.click()
        # THIS CHECKS ALL THE ENTRIES IF EXITS
        if(driver.find_element_by_xpath('//*[@id="crmGrid_gridBodyTable_checkBox_Image_All"]')):
            selAll = driver.find_element_by_xpath('//*[@id="crmGrid_gridBodyTable_checkBox_Image_All"]')
            selAll.click()


#IF YOU HAVE ANY PROBLEMS ITS PROBABLY RIGHT HERE PROBLEM OPENING UP EDIT
## MAKES SURE EDIT BUTTON IS VISIBLE

driver.switch_to.default_content()
time.sleep(1)  ## Try this without sleep

if(driver.find_element_by_xpath("//*[@id='trc_utilityaccount|NoRelationship|HomePageGrid|Mscrm.HomepageGrid.trc_utilityaccount.Edit']/span/a/span")):
    editbuttonclick = driver.find_element_by_xpath("//*[@id='trc_utilityaccount|NoRelationship|HomePageGrid|Mscrm.HomepageGrid.trc_utilityaccount.Edit']/span/a/span")
    hover = ActionChains(driver).move_to_element(editbuttonclick)
    hover.perform()
    editbuttonclick.click()


# moves to the new window or popup
window_before = driver.window_handles[0]
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
print ('success')

if(driver.find_element_by_xpath( "//*[@id='DlgHdTitle']" )):
    MTClick = driver.find_element_by_xpath( "// *[ @ id = 'trc_mergedto_lookupTable'] / tbody / tr / td[1] / div" )
    MTClick.click()
    MTClick2 = driver.find_element_by_xpath( "//*[@id='trc_mergedto_ledit']" ) # inputs the search bar
    MTClick2.send_keys(numbers, Keys.ENTER)
    if(driver.find_element_by_class_name( "ms-crm-IL-MenuItem-MoreInfoItem" )):
        MTClick3 = driver.find_element_by_class_name("ms-crm-IL-MenuItem-MoreInfoItem")
        MTClick3.click()
    ConfrimClick = driver.find_element_by_id("butBegin")
    ConfrimClick.click()

##### AT THIS POINT MERGING IS DONE AND ITS BACK IN THE MAIN WINDOW
driver.switch_to.window(window_before)

print ('*******************')
#driver.close()

