import time
# virtualenv myVirtualPython
#  ou
# python -m venv myVirtualPython
#
# pip install -U selenium
# pip install webdriver-manager
from unittest import result
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get('http://10.115.57.132:80/maPage.html')
#browser.get('http://10.115.57.130:8080/MapageF.html')
#browser.get('./maPage.html')

testNom = 'toto'


elem = browser.find_element(By.XPATH, '/html/body/div[1]/input')  # Find the search box
elem.send_keys( testNom )

bouton = browser.find_element(By.NAME, 'bouton')
bouton.click()

div = browser.find_element(By.NAME, 'resultat')
result = div. get_attribute( 'innerHTML' )

if result == testNom.upper():
    print( 'OK' )
else: 
    print( 'KO' )

assert result == testNom.upper()

time.sleep(1)
browser.quit()