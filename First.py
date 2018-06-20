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

ab = driver.find_element_by_xpath('//*[@id="navTabGroupDiv"]/span[3]')
ab.click()
print ('Success x1')
element = driver.find_element_by_xpath('//*[@id="Tabnav_Project"]')

#Makes sure that you are paying attention
numb = input("enter 1 to continue? ")
if(numb=='1'):
    if(driver.find_element_by_xpath('//*[@id="Tabnav_Project"]/a')):
        print('inside x2')
        a1 = driver.find_element_by_xpath('//*[@id="Tabnav_Project"]/a')
        a1.click()
        a2 = driver.find_element_by_xpath('//*[@id="Tabnav_Project"]/a')
        a2.click()
        print ('Success x2')


numb = input("enter 1 to continue to utility? ")
if (numb == '1'): ## MAKE SURE YOU MOVE TO UTILITY ACCOUNT MANUALLY
    if (wait(driver, 4).until(EC.frame_to_be_available_and_switch_to_it("contentIFrame0"))):
        #driver.switch_to.frame("contentIFrame0")
        driver.switch_to.default_content()
        wait(driver, 4).until(EC.frame_to_be_available_and_switch_to_it("contentIFrame0"))
        print ('I see it')
        #driver.switch_to.frame(driver.find_element_by_id("contentIFrame0"))
        #wait(driver, 4).until(EC.frame_to_be_available_and_switch_to_it("contentIFrame0"))
        #wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="contentIFrame0"]')))
        searchbarclick = driver.find_element_by_id('crmGrid_SavedNewQuerySelector')
        driver.switch_to.default_content()
        #Goes to the clickable frame
        wait(driver, 4).until(EC.frame_to_be_available_and_switch_to_it("contentIFrame1")) #all clickables are in frame1
        #Clicks the search bar to enter something
        searchbarclick2 = driver.find_element_by_xpath('//*[@id="crmGrid_findCriteriaImg"]')
        searchbarclick2.click()
        wait(driver, 10).until(EC.presence_of_element_located((By.ID, 'crmGrid_findHintText')))
        searchbarclick = driver.find_element_by_xpath('//*[@id="crmGrid_findHintText"]')
        searchbarclick.click()
        print ('successs x3')
        #inputElement = driver.find_element_by_xpath('//*[@id="crmGrid_quickFindContainer"]')
        print ('successs x4')
        searchbarclick.send_keys("6739540306")
        print ('successs x5')

        #a = wait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it("InlineDialog_Iframe"))

    #e = driver.find_element_by_xpath('//*[@id="actionGroupControl_rightNavContainer"]')
    #e.click()
    #print ('aaaaaaaaaaaaaaaaaa')
    #if(driver.find_element_by_id('//*[@id="actionGroupControl_rightNavContainer"]')):
        #element2 = driver.find_element_by_id('//*[@id="actionGroupControl_rightNavContainer"]')
        #hover2 = ActionChains(driver).move_to_element(element2)
        #hover2.perform()
        #print ('Success x3')

#aD = driver.find_element_by_xpath('//*[@id="trc_utilityaccount"]')
#aD.click()
#print ('Success x3')

#click 3 times

#if(driver.find_element_by_xpath('//*[@id="navTabGroupDiv"]/span[3]')):
#    print ("success")
#element = driver.find_element_by_xpath('//*[@id="navTabGroupDiv"]/span[3]')
#hover = ActionChains(driver).move_to_element(element)
#hover.perform()
#if (driver.find_element_by_xpath('//*[@id="trc_utilityaccount"]')):
#    print ('Found it')


print ('*******************')

#driver.close()
