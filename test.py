import os
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

driver = webdriver.Remote(
command_executor='http://127.0.0.1:4723/wd/hub',
desired_capabilities={
    'app': 
os.path.expanduser('C:/Users/berkin.tatlisu/Desktop/shop/client/android/app/build/outputs/apk/debug/app-debug.apk'),
    'platformName': 'Android',
    'deviceName': 'Nexus_5X_API_21',
})

def runtest():

 


    time.sleep(10)
    print "test is starting"
    # wait for app to load
    time.sleep(10)

    #asd = driver.back()

    # find the link with the text "Click here" and click on it
    #link = 
    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]')

    #link = driver.find_element_by_accessibility_id('test1')
    #link =
    link = driver.find_element_by_accessibility_id("test1")
    link.click()
    #link1 = driver.find_element_by_accessibility_id("test2")
    #link1.click()


    #link.click()
    link.send_keys("Hello world! hello world! robot testing robot testing ");
    driver.hide_keyboard()

    link1 = driver.find_element_by_accessibility_id("test2")
    link1.click()
    link1.send_keys("assdsdfdasfdas")
    driver.hide_keyboard()

    chek = driver.find_element_by_accessibility_id("test3")



    button = driver.find_element_by_accessibility_id("button1")
    actions = TouchAction(driver)
    actions.tap(chek)
    actions.perform()

    actions.tap(button)
    actions.perform()


    #button = driver.find_element_by_accessibility_id("button1") 
    #link.click()
    #button.click()
    # wait for the next screen to load
    ##time.sleep(10)

    # make sure the correct "Success" result is on the page
    #driver.find_element_by_xpath('//*[@text="Success"]')

    # important; you will not be able to launch again if this does not 
    #happen
    time.sleep(3)
    #driver.quit()
    driver.back()
    print "test is done!"
    runtest()


runtest()
