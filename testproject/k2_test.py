import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"
driver.get(URL)

r_color = driver.find_element_by_id("randomColorName").text
t_color = driver.find_element_by_id("testColorName")
t_color_stop = ""
t_color_stop_after = ""

# Kigyüjtjük az összes lehetséges színt egy listába
all_color = driver.find_element_by_id("allcolors").text
all_color_list = all_color.strip('"').split('", "')


def test_tc01_initial():
    """ Helyesen jelenik meg az applikáció betöltéskor:
        * Alapból egy random kiválasztott szín jelenik meg az `==` bal oldalanán.
        A jobb oldalon csak a `[  ]` szimbólum látszik.
        <szín neve> [     ] == [     ] """
    # Ball oldalon levő szín megtalálható a listában, jobb oldalon nincs kiírva szín
    assert r_color in all_color_list
    assert t_color.text == ""


def test_tc02_start_stop():
    global t_color_stop, t_color_stop_after
    """ El lehet indítani a játékot a `start` gommbal.
        * Ha elindult a játék akkor a `stop` gombbal le lehet állítani. """
    button_start = driver.find_element_by_id("start")
    button_stop = driver.find_element_by_id("stop")
    # Megnyomjuk a start gombot majd 1 mp-el később a stop gombot.
    button_start.click()
    time.sleep(random.randint(1, 24))  # várakozás random ideig
    button_stop.click()
    # Ha a start gombra elindult a játék akkor a jobb oldalon már ki van írva egy szín
    t_color_stop = t_color.text
    assert t_color_stop != ""
    # Ha a stop gombra megáll a játék akkor ujabb 1 mp várakozás után is ugyan az a szín van kiírva a jobb oldalon
    time.sleep(1)
    t_color_stop_after = t_color.text
    assert t_color_stop_after == t_color_stop


def test_tc03_hit_not_hit():
    """ Eltaláltam, vagy nem találtam el.
        * Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le
        amikor a bal és a jobb oldal ugyan azt a színt tartalmazza akkor a `Correct!` felirat jelenik meg.
          ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az `Incorrect!` felirat kell megjelenjen. """
    hit_or_not_hit = driver.find_element_by_id("result").text
    if r_color == t_color_stop:
        assert hit_or_not_hit == "Correct!"
    else:
        assert hit_or_not_hit == "Incorrect!"
