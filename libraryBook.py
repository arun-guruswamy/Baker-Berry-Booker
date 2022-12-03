import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

times = ['9:00pm', '9:30pm', '10:00pm', '10:30pm']
fin_slots = []
username = ''
password = ''
meeting_name = 'Study group'
#bypass_code = ''

# with open('C:/Documents/Projects/cookies.pkl', 'rb') as f:
#     data = pickle.load(f)

# print(data)

#create webdriver object
s = Service(':C\chromedriver_win32\chromedriver.exe')
chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:\environments\selenium") 
driver = webdriver.Chrome(options=chrome_options, service=s)
driver = webdriver.Chrome(service=s)

# # get homepage
# driver.get('https://www.library.dartmouth.edu/')


# Scrapes table containing time slot buttons
# time_slots = driver.find_element(By.XPATH, "//table[@class='fc-scrollgrid-sync-table table-bordered']/tbody/tr[1]/td")

#Delete current cookies
# driver.delete_all_cookies()

#Load cookies
# cookies = pickle.load(open("C:/Documents/Projects/cookies.pkl", "rb")) 
# for cookie in cookies:
#     driver.add_cookie(cookie)
# driver.refresh()

#Get booking page
driver.get("https://libcal.dartmouth.edu/spaces?lid=2988&gid=5070&c=0")

for i in range(3):
    t = times[i]
    title = t +  " 12/3/2022 - Baker 158 - Available"
    slot = driver.find_element(By.XPATH, "//a[@title='"+title+"']")
    driver.execute_script("arguments[0].click();", slot)
    fin_slots.append(slot)

#Submit time slots
submit_button = driver.find_element(By.ID, 'submit_times')
driver.execute_script("arguments[0].click();", submit_button)
sleep(2)

#Login

#Enter Username and Password
# if driver.title == 'Dartmouth Web Authentication':
username_field = driver.find_element(By.ID, 'username')
username_field.send_keys(username)
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(password)
sleep(2)   

#Click Login
login_button = driver.find_element(By.NAME, 'submit')
driver.execute_script("arguments[0].click();", login_button)
sleep(2)   

# Duo Push
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='duo_iframe']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Send Me a Push']"))).click()
# WebDriverWait(driver, 12).until(EC.url_to_be('https://libcal.dartmouth.edu/spaces/auth?returnUrl=%2Fspaces%3Flid%3D2988%26gid%3D5070%26c%3D0'))
sleep(3)

#Save Cookies data
# pickle.dump(driver.get_cookies(), open("C:/Documents/Projects/cookies.pkl", "wb"))

# Click continue after logging in
driver.switch_to.default_content()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'continue')))
continue_button = driver.find_element(By.NAME, 'continue')
driver.execute_script("arguments[0].click()", continue_button)
sleep(2)

# Input meeting name
name_field = driver.find_element(By.ID, 'nick')
name_field.send_keys(meeting_name)
sleep(3)   

final_submit_button = driver.find_element(By.ID, 's-lc-eq-bform-submit')
driver.execute_script("arguments[0].click();", final_submit_button)
sleep(3)  

driver.close()


# #Click Bypass Code
# bypass_button = driver.find_element(By.ID, 'passcode')
# driver.execute_script("arguments[0].click();", bypass_button)
# sleep(1)

# # #Enter Bypass code
# # bypass_field = driver.find_element(By.NAME, 'passcode')
# # bypass_field.send_keys(bypass_code)
# # driver.execute_script("arguments[0].click();", bypass_button)