from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"
driver.get(URL)
a_side = driver.find_element_by_id("a")
b_side = driver.find_element_by_id("b")
cal = driver.find_element_by_id("submit")
c_side_visibility = driver.find_element_by_id("results")
c_side_calculation = driver.find_element_by_id("result")
# Teszt adatok
a = ["", "2"]
b = ["", "3"]
c = ["NaN", "10"]


def clear():
    a_side.clear()
    b_side.clear()


def a_b_empty():
    assert a_side.get_attribute("value") == a[0]
    assert b_side.get_attribute("value") == b[0]


def test_tc01_initial():
    """ Helyesen jelenik meg az applikáció betöltéskor:
        a: <üres>
        b: <üres>
        c: <nem látszik> """
    a_b_empty()
    assert c_side_visibility.get_attribute("style") == "display: none;"


def test_tc02_calculation():
    """ Számítás helyes, megfelelő bemenettel
        a: 2
        b: 3
        c: 10 """
    a_side.send_keys(a[1])
    b_side.send_keys(b[1])
    cal.click()
    assert a_side.get_attribute("value") == a[1]
    assert b_side.get_attribute("value") == b[1]
    assert c_side_calculation.text == c[1]


def test_tc03_empty():
    """ Üres kitöltés:
        a: <üres>
        b: <üres>
        c: NaN """
    clear()
    cal.click()
    a_b_empty()
    assert c_side_calculation.text == c[0]
