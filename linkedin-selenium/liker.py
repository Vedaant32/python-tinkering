import os
from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

links = [
    "https://www.linkedin.com/posts/shimanshu-yadav-146a19191_devsnestday14-devsnest6monthschallenge-activity-6789618484444823552-raSr",
    "https://www.linkedin.com/posts/activity-6789638183744258049-dIDI",
    "https://www.linkedin.com/posts/shimanshu-yadav-146a19191_devsnestday12-devsnest6monthschallenge-activity-6788891728729526273-sTVE",
    "https://www.linkedin.com/posts/sidd-oo_100daysofcode-devsnestday21-devsnest6monthschallenge-activity-6789459261542973440-x7FX/",
    "https://www.linkedin.com/posts/ross-nelson-32493684_devsnest6monthschallenge-devsnestday21-slowandsteady-activity-6788661474186338304-Dx0z",
]

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://linkedin.com")

while "1" != input("press 1 when signed in: "):
    pass
for link in links:
    try:
        print("Accessing link", link)
        driver.get(link)
        sleep(2)
        el = driver.find_element_by_class_name("react-button__trigger")
        if "false" == el.get_attribute("aria-pressed"):
            print("Liking")
            el.click()
            print("Liked")
            sleep(1)
        else:
            print("Already Processed Link ", link)
    except Exception as e:
        print("Error Processing Link\nlink: ", link, "\nerror", e)

driver.close()
