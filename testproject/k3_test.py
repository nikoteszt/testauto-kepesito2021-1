from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"
driver.get(URL)
# Alfanumerikus mező validáció tesztelése

# Az input mező és a validációs üzenet helye
input_field = driver.find_element_by_id("title")
error_message = driver.find_element_by_tag_name("span")

# Teszt adatok
send = ["abcd1234", "teszt233@", "abcd"]
error_text = ["", "Only a-z and 0-9 characters allewed", "Title should be at least 8 characters; you entered 4."]


def filling(field, error):
    input_field.clear()
    input_field.send_keys(field)
    assert error_message.text == error


def test_tc01_good_filling():
    """ Helyes kitöltés esete:
        * title: abcd1234
        * Nincs validációs hibazüzenet """
    filling(send[0], error_text[0])


def test_tc02_illegal_filling():
    """ Illegális karakterek esete:
        * title: teszt233@
        * Only a-z and 0-9 characters allewed. """
    filling(send[1], error_text[1])


def test_tc03_short_filling():
    """ Tul rövid bemenet esete:
        * title: abcd
        * Title should be at least 8 characters; you entered 4. """
    filling(send[2], error_text[2])
