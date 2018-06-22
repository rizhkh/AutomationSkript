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
numbers = ['403852699996','2669930001']


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

window_before = driver.window_handles[0]


numb = input("enter 1 to continue to utility? ")
if (numb == '1'): ## MAKE SURE YOU MOVE TO UTILITY ACCOUNT MANUALLY
    #Problem: runs in the first try having trouble in the second try its about the xpath

    for i in range(len(numbers)):
        print (i)
        print(numbers[i])
        if (wait(driver, 4).until(EC.frame_to_be_available_and_switch_to_it("contentIFrame1"))):
            print ('true')
            driver.switch_to.default_content()
            print('true2')
            #Goes to the clickable frame #############<------
            wait(driver, 4).until(EC.frame_to_be_available_and_switch_to_it("contentIFrame1")) #all clickables are in frame1
            print('true3')
            #print('frame 1')
            #Clicks the search bar to enter something
            searchbarclick2 = driver.find_element_by_id("crmGrid_findCriteriaButton")
            print('true4')
            searchbarclick2.click()
            print('true5')
            time.sleep(5)
            print('true6')
            searchbarclick = driver.find_element_by_xpath('//*[@id="crmQuickFindTD"]/table')
            print('true7')
            searchbarclick.click()
            #This paste in the number into the form
            ################################
            ##########
            searchbarclick3 = driver.find_element_by_xpath('//*[@id="crmGrid_findCriteria"]')
            searchbarclick3.send_keys(numbers[i])
            searchbarclick2 = driver.find_element_by_id("crmGrid_findCriteriaButton")
            searchbarclick2.click()

            # THIS CHECKS ALL THE ENTRIES IF EXITS
            if(driver.find_element_by_xpath('//*[@id="crmGrid_gridBodyTable_checkBox_Image_All"]')):
                selAll = driver.find_element_by_xpath('//*[@id="crmGrid_gridBodyTable_checkBox_Image_All"]')
                selAll.click()

                #This exception throw basically checks if record is more than 1 exception is thrown and it understands more records are present so it runs except part
                try:
                    if (driver.find_element_by_xpath('//*[@totalrecordcount="1"]')):
                        print("***************************")
                        print("***************************")
                        print("***************************")
                        print("***************************")
                        print("***************************")
                        print("***************************")
                        time.sleep(5)
                        driver.switch_to.default_content()
                        continue


                except:
                    #IF YOU HAVE ANY PROBLEMS ITS PROBABLY RIGHT HERE PROBLEM OPENING UP EDIT
                ## MAKES SURE EDIT BUTTON IS VISIBLE
                    driver.switch_to.default_content()
                    time.sleep(2)  ## Try this without sleep
                    ## THIS PRESSES THE EDIT BUTTON
                    if(driver.find_element_by_xpath("//*[@id='trc_utilityaccount|NoRelationship|HomePageGrid|Mscrm.HomepageGrid.trc_utilityaccount.Edit']/span/a/span")):
                        editbuttonclick = driver.find_element_by_xpath("//*[@id='trc_utilityaccount|NoRelationship|HomePageGrid|Mscrm.HomepageGrid.trc_utilityaccount.Edit']/span/a/span")
                        hover = ActionChains(driver).move_to_element(editbuttonclick)
                        hover.perform()
                        editbuttonclick.click()

                    else:
                        print ('DOES NOT EXIST')
                        time.sleep(30)
                        numb2 = input("enter 9 to exit? ")
                        if (numb2 == '9'):
                            driver.close()


            # moves to the new window or popup
            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)
            #print('success')

            #if does not exist handle t2o code to bring it back and search again

            if(driver.find_element_by_xpath( "//*[@id='DlgHdTitle']" )):
                MTClick = driver.find_element_by_xpath( "// *[ @ id = 'trc_mergedto_lookupTable'] / tbody / tr / td[1] / div" )
                MTClick.click()
                #print ('in new window')
                time.sleep(2)
                MTClick2 = driver.find_element_by_xpath( "//*[@id='trc_mergedto_ledit']" ) # inputs the search bar
                MTClick2.send_keys(numbers[i], Keys.ENTER)
                time.sleep(2)
                if(driver.find_element_by_class_name( "ms-crm-IL-MenuItem-MoreInfoItem" )):
                    MTClick3 = driver.find_element_by_class_name("ms-crm-IL-MenuItem-MoreInfoItem")
                    MTClick3.click()
                print ('about to confirm and close new window')
                ConfrimClick = driver.find_element_by_id("butBegin")
                ConfrimClick.click()

        #"// *[ @ id = 'navBar']"
        #driver.switch_to.window(window_before)
        time.sleep(20)
        driver.switch_to.window(window_before)
        if ((driver.find_element_by_id("navBar"))):
            print ("It switched back")


##### AT THIS POINT MERGING IS DONE AND ITS BACK IN THE MAIN WINDOW



else :
    print ("Number not in database")

print ('*******************')



#driver.close()


