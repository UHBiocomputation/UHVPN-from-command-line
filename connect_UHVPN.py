from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import title_is,presence_of_element_located
from getpass import getpass
import time
import os
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Connect to the UH VPN from the command line,' +\
                                             ' obtaining the authentification cookie through a browser' +\
                                             ' that is controlled through Selenium.')
parser.add_argument('-u','--username', help="UH username (xx99xxx@herts.ac.uk)")
parser.add_argument('-s', '--silent',  action='store_const', dest='silent',
						const=True, default=False, 
						help="Use headless mode, i.e. don't show the browser window. " +\
						"Be aware that you may not see error messages displayed in the browser.")
args = parser.parse_args()

username = args.username
if not username:
	username = input("UH username: ")
if not username.endswith("@herts.ac.uk"):
    username += "@herts.ac.uk"
pw = getpass('UH password: ')
service = Service(executable_path=ChromeDriverManager().install())
options = Options()
options.page_load_strategy = 'normal'
if args.silent:
    options.headless = True

driver = webdriver.Chrome(service=service, options=options)
time.sleep(3)
driver.get("https://uhvpn.herts.ac.uk") 

name = driver.find_element(By.NAME,'UserName')
name.send_keys(username)
passwdfield = driver.find_element(By.NAME, 'Password')
passwdfield.send_keys(pw)
del(pw)
signinbutton = driver.find_element(By.ID, 'submitButton')
signinbutton.click()
WebDriverWait(driver,timeout=60).until(title_is('Two-Factor Authentication'))

auth = driver.find_element(By.CLASS_NAME,'remember_me_label_field')
auth.send_keys('\n')

WebDriverWait(driver,timeout=60).until(title_is("Secure Connect Secure - Home"))
dsid_cookie = driver.get_cookie('DSID')
print(dsid_cookie['value'])
driver.quit()
time.sleep(1)
print()
print("running the command:")
print('sudo', 
	'openconnect', 
	'-u', username, 
	'--cookie=DSID={}'.format(dsid_cookie['value']), 
	'--protocol=nc', 
	'uhvpn.herts.ac.uk')
print("you may be prompted for your root password to run openconnect via sudo... ")
subprocess.run(['sudo', 
	'openconnect', 
	'-u', username, 
	'--cookie=DSID={}'.format(dsid_cookie['value']), 
	'--protocol=nc', 
	'uhvpn.herts.ac.uk'])
