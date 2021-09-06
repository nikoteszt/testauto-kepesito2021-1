from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"
driver.get(URL)


character = driver.find_element_by_id("chr")
operator = driver.find_element_by_id("op")
number = driver.find_element_by_id("num")
cal = driver.find_element_by_id("submit")
res = driver.find_element_by_id("result")


def test_tc01_corect_start():
    # Helyesen betöltődik az applikáció:
    #    * Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
    #    * !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
    abc_tabla_expected = \
        "!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    abc_tabla_app = driver.find_element_by_xpath('/html/body/div/div/p[3]').text
    assert abc_tabla_app == abc_tabla_expected


""" Megjelenik egy érvényes művelet:
    * `chr` megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
    * `op` mező vagy + vagy - karaktert tartlamaz
    * `num` mező egy egész számot tartalamaz """
