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
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get('http://10.115.57.132:80/maPage.html')
#browser.get('http://10.115.57.130:8080/MapageF.html')
#browser.get('./maPage.html')


def testInput( testNom ):
    elem = browser.find_element(By.NAME, 'nom')  # Find the search box
    elem.clear()
    elem.send_keys( testNom )

    bouton = browser.find_element(By.NAME, 'bouton')
    bouton.click()

    div = browser.find_element(By.NAME, 'resultat')
    result = div. get_attribute( 'innerHTML' )

    print( 'test : '+testNom, end =' ' )
    if result == testNom.upper():
        print( 'OK' )
    else: 
        print( 'KO' )


print( "test majuscule ------------------------------")

testInput( 'toto' )
testInput( 'tété' )
testInput( '1234' )

print( "test calcul ------------------------------")
def testCalcul( expression, resultat ):
    elem = browser.find_element(By.NAME, 'saisie')  # Find the search box
    elem.clear()
    elem.send_keys( expression )

    bouton = browser.find_element(By.NAME, 'go')
    bouton.click()

    div = browser.find_element(By.NAME, 'res')
    result = div. get_attribute( 'innerHTML' )

    print( 'test : '+ expression, end =' ' )
    if result == resultat:
        print( 'OK' )
    else: 
        print( 'KO' )

testCalcul( '2+4', '6')
testCalcul( '2-4', '-2')
testCalcul( '2*4', '8')




#assert result == testNom.upper()

#time.sleep(1)
browser.quit()