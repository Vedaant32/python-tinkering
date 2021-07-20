import os, sys
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

link = "https://www.linkedin.com/mynetwork/"

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://linkedin.com")

while "1" != input("press 1 when signed in: "):
    pass

print("Accessing Networks Page : ", link)
driver.get(link)
sleep(2)
el = driver.find_elements_by_xpath("//*[@class='invitation-card__action-btn artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']")
for x in el:
    x.click()
    sleep(1)

