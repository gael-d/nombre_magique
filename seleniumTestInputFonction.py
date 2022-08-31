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

def testInput( idChamp, idBouton, idResultat, entree, sortie ):
    elem = browser.find_element(By.ID, idChamp )  # Find the search box
    elem.clear()
    elem.send_keys( entree )

    bouton = browser.find_element(By.ID, idBouton )
    bouton.click()

    div = browser.find_element(By.ID, idResultat)
    result = div. get_attribute( 'innerHTML' )

    print( 'test : ' + entree, end =' ' )
    if result == sortie:
        print( 'OK' )
    else: 
        print( 'KO' )




def testMaj( testNom ):
    testInput( 'nom', 'bouton', 'resultat', testNom, testNom.upper())


print( "test majuscule ------------------------------")

aTester=[ 'toto', 'rémi', '1234'  ]
for mot in aTester:
    testMaj( mot )

print( "test calcul ------------------------------")
def testCalcul( expression, resultat ):
    testInput( 'saisie', 'go', 'res', expression, resultat )


testCalcul( '2+4', '6')
testCalcul( '2-4', '-2')
testCalcul( '2*4', '8')




#assert result == testNom.upper()

#time.sleep(1)
browser.quit()