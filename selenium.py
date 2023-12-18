# coding=utf-8
#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import re
import names
from random import randint
from fp.fp import FreeProxy




#chrome_options = webdriver.ChromeOptions()


dates = str(randint(10, 28)) + '/' + str(randint(10, 12)) + '/' + str(randint(2000, 2004))
# proxy = FreeProxy(rand=True).get()
# print(proxy)
options = webdriver.ChromeOptions()
# options.add_argument("--proxy-server="+proxy)
# options.add_argument("ignore-certificate-errors")
driver = webdriver.Chrome('./chromedriver',options=options)
try:
 driver.get("#############################################")
 myElem = WebDriverWait(driver, 4).until(
     EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
 myElem.click();


 Nom =driver.find_element_by_xpath('//*[@id="email"]')
 Nom.send_keys("georges")
 Nom.send_keys(names.get_first_name())


 myElem = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '//*[@id="didomi-notice-disagree-button"]')))
 myElem.click();
#driver.refresh();
 driver.switch_to.frame('qualifio-CED945CC-3BD1-4031-AC2F-B9E292E34DBE')

 myElem = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '//*[@id="iubenda-cs-banner"]/div/div[1]/div/div[3]/div[2]/button[1]')))
 myElem.click();

 button= WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jouer"]')))
 button.click()

 driver.implicitly_wait(4)
 civilite=Select(driver.find_element_by_xpath('//*[@id="choix_2543782"]'))
#civilte= WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '//*[@id="choix_2543782"]')))
 civilite.select_by_value(str(randint(1,2)))
except:
 driver.close()


Nom = driver.find_element_by_id("choix_2543776")
Nom.send_keys(names.get_first_name())

Prenom = driver.find_element_by_id("choix_2543775")
Prenom.send_keys(names.get_last_name())

date = driver.find_element_by_id("2543781")
date.send_keys(dates)

email = driver.find_element_by_id("choix_2543777")
email.send_keys(names.get_first_name()+names.get_last_name()+str(randint(1,10))+'@gmail.com')

tel = driver.find_element_by_id("choix_2546076")
tel.send_keys(str(randint(645734567,745735567)))

postal = driver.find_element_by_id("choix_2543785")
postal.send_keys(str(randint(75001,75020)))

postal = driver.find_element_by_id("coreg28393")
postal.click()

button= WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register"]')))
button.click()

button= WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="answerPic_8590421"]')))
button.click()
temp=driver.find_element('xpath',"//*[@id=\"instant_result\"]").text;
if "gagné un" in temp:
    m1 = re.search('gagné(.+?)\n', temp)
    m2 = re.search(':(.+?)\n', temp)
    with open("gains.txt", "a") as text_file:
        text_file.write(m1.group(1)+m2.group(1)+'\n')
    driver.close()
else:
    driver.close()
    #time.sleep(20)
    #driver.close()
#driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
print('a')
