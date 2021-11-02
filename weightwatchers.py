from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from shutil import which
from selenium.webdriver.common.keys import Keys

# function to get and print hours
def get_hours(driver):
    days = driver.find_elements_by_css_selector('div.day-qBhx-')
    for day in days:
        dayName = day.find_element_by_css_selector('span').text
        dayHours = day.find_element_by_css_selector('div.hours-2ntIH > div').text
        print(dayName + ': ' + dayHours)

# Initialize the Bot
chromeOptions = Options()
# uncomment following line if you want to run headless
# chromeOptions.add_argument("--headless")
chromePath = which("chromedriver")

# starting ChromeDriver
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chromeOptions)
driver.maximize_window()

# Getting the url
driver.get("https://www.weightwatchers.com/us/find-a-workshop/")
sleep(2)

# get Studio button and click on it
studioButton = driver.find_elements_by_css_selector("button.toggleButton-2ikVW")[-1]
studioButton.click()
sleep(2)

# get input field and enter location
inField = driver.find_element_by_id("location-search")
inField.send_keys("10011")
inField.send_keys(Keys.ENTER)
sleep(2)

# print title and distance of first result
firstResult = driver.find_element_by_css_selector("div#search-results > div")
title = firstResult.find_element_by_css_selector("div.linkContainer-1NkqM > a").text
distance = firstResult.find_element_by_css_selector("span.distance-OhP63").text
print("Title: " + title)
print("Distance: " + distance)

# Click on first result
firstResult = firstResult.find_element_by_css_selector("div.linkContainer-1NkqM > a")
firstResult.click()
sleep(2)

# check that that the title is same as we printed
newTitle = driver.find_element_by_css_selector("h1").text
if title.strip() == newTitle.strip():
    print("Title is same")

# get available hours and print
hours = get_hours(driver)
