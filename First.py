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
        searchbarclick2 = driver.find_element_by_id("crmGrid_findCriteriaButton")
        searchbarclick2.click()
        time.sleep(5)
        print ('aaaaaaaaaa')
        searchbarclick = driver.find_element_by_xpath('//*[@id="crmQuickFindTD"]/table')
        searchbarclick.click()
        print ('successs x3')
        #inputElement = driver.find_element_by_xpath('//*[@id="crmGrid_quickFindContainer"]')
        print ('successs x4')
        #This paste in the number into the form
        ################################
        ##########
        ##########
        ##########
        searchbarclick3 = driver.find_element_by_xpath('//*[@id="crmGrid_findCriteria"]')
        searchbarclick3.send_keys('6739540306')
        #searchbarclick.submit()
        print ('successs x5')


print ('*******************')

#driver.close()
