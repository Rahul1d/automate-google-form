from selenium import webdriver
import random
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
# option.add_argument("--headless")
#option.add_argument("disable-gpu")

start = time.time()
print(start)
browser = webdriver.Chrome(executable_path='chromedriver', options=option)
for i in range(1000):
    
    browser.get("https://forms.gle/pCKkgEzEkatAatY19")

    # print("attempt" , i, time.time())
    # textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
    radiobuttons = browser.find_elements_by_class_name("freebirdFormviewerComponentsQuestionRadioChoice")
    # checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
    submitbutton = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")

    # 1
    radiobuttons[random.randint(0, 1)].click()

    # 2
    radiobuttons[random.randint(2, 6)].click()

    # 3
    radiobuttons[random.randint(7, 9)].click()

    # 4
    radiobuttons[random.randint(10, 12)].click()

    # 5
    radiobuttons[random.randint(13, 14)].click()

    # 6
    radiobuttons[random.randint(15, 17)].click()

    # 7
    radiobuttons[random.randint(18, 19)].click()

    # 8
    radiobuttons[random.randint(20, 21)].click()

    print(submitbutton.click())
    
    print(f'Time: {time.time() - start}', "attempt", i)
