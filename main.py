import writeHTML
import gitpy
import os
import time
import json
import datetime
import string
import unicodedata
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

#Function: write data to json format
def writeToJSON(fileName,data):
    with open(fileName, 'w') as output:
        json.dump(data, output)

#format to valid filename
#Reference: https://gist.github.com/wassname/1393c4a57cfcbf03641dbc31886123b8
def clean(name, replace=' '):
    whitelist = "-_.() %s%s" % (string.ascii_letters, string.digits)
    # replace spaces
    for r in replace:
        name = name.replace(r,'_')
    
    # keep only valid ascii chars
    cleaned = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode()
    
    # keep only whitelisted chars
    return ''.join(c for c in cleaned if c in whitelist)

#Function: strip data
def getData(browser, buildingName):
    #Select Facilities Filter
    facilitiesSelect = Select(browser.find_element_by_id('ctl00_pc_Facilities_ddl'))
    facilitiesSelect.select_by_visible_text(buildingName)

    time.sleep(1) #time

    #Select Room Filter
    roomSelect = Select(browser.find_element_by_id('ctl00_pc_Rooms_ddl'))
    roomList = roomSelect.options

    for index, room in enumerate(roomList[1:]):
        eventInfo = []

        roomName = clean(room.text)
        
        print('-------- %s --------' %(roomName))

        time.sleep(1) #time

        #Select room
        roomSelect.select_by_visible_text(room.text)

        time.sleep(1) #time

        #click "Apply"
        browser.find_element_by_id("ctl00_pc_ApplyFilterButton").click()

        time.sleep(1) #time
        
        #Strip data from room
        table = browser.find_element_by_id('ctl00_pc_ListViewGrid')
        rows = table.find_elements_by_tag_name('tr')
        for row in rows[2:]:
            obj = row.find_elements_by_tag_name('td')
            
            startTime = obj[0].text
            endTime = obj[1].text
            eventName = obj[2].text
			#if roomName == "Conference A1000":
			#	eventName = "Conference Meeting"
            client = obj[4].text
            info = {'startTime':startTime,
                    'endTime':endTime,
                    'eventName':eventName,
                    'client':client}

            eventInfo.append(info)

            print('%s %s %s %s' %(startTime, endTime, eventName, client))
       
        writeHTML.writeToHTML(roomName,eventInfo)
        
        time.sleep(1) #time
            
        #Select Filter
        browser.find_element_by_id('ctl00_pc_FilterViewButton').click()

if __name__== '__main__':
    # options = Options()
    # options.add_argument("--disable-infobars")
    # browser = webdriver.Chrome(chrome_options=options)
    # url = 'http://vems.oit.uci.edu/MedicalEducation/BrowseEvents.aspx'
    # browser.get(url)

# ##    #Select view as Monthly List
# ##    browser.find_element_by_id('tab2-tab').click()
# ##    #Select view By Location
# ##    browser.find_element_by_xpath('//*[@id="groupByOptions"]/label[2]').click()
    
    # #Select Filter
    # browser.find_element_by_id("ctl00_pc_FilterViewButton").click()

    # time.sleep(2) #time

    # getData(browser, 'SOM Medical Education')
    # getData(browser, 'College of Health Sciences')

    # #close the browser window
    # browser.quit()

    #commit to git
    print("Commit to GIT")
    temp=time.localtime(time.time())
    uploaddate= str(temp[0])+'_'+str(temp[1])+'_'+str(temp[2])+'_'+str(temp[3])+'_'+str(temp[4])

    repodir= os.getcwd()
    gitpy.gitAdd('.',repodir )
    gitpy.gitCommit(uploaddate, repodir)
    gitpy.gitPush(repodir)
    print('++++DONE++++')
