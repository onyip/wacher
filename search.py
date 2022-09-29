from ast import If
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from distutils.dir_util import copy_tree
from pyvirtualdisplay import Display
from selenium import webdriver
import time
import sys
import os

# display = Display(visible=0, size=[800, 600])
# display.start()

options = Options()
options.add_extension(
    './extension/01.crx')
options.add_extension(
    './extension/02.crx')
options.add_extension(
    './extension/03.crx')
options.add_argument("--window-size=100,300")
d = {}
for x in range(int(sys.argv[1])):
    print(f'Creating on viewer number {x}')
    if os.path.isdir(f'./Profile {x}') == False:
        from_directory = './profile'
        to_directory = f'./Profile {x}'
        copy_tree(from_directory, to_directory)
    options.add_argument(
        f"--user-data-dir=./Profile {x}")
    d["group" + str(x)] = webdriver.Chrome(
        executable_path=r'./chromedriver', options=options)
    d["group" +
        str(x)].get('https://www.youtube.com/results?search_query=Ubuntu+Screencast+Tutorial+#limitlesstutorial')
    time.sleep(5)
    links = WebDriverWait(d["group" + str(x)], 5).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.yt-simple-endpoint.style-scope.ytd-video-renderer#video-title")))
    for y in links:
        if y.get_attribute("href") == 'https://www.youtube.com/watch?v=zUu64aJuOvg':
            time.sleep(3)
            y.click()
            time.sleep(7)
            path = '//*[@id="movie_player"]/div[1]/video'
            p = '{return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}'
            fun = f"function getElementByXpath(path) {p} let y = getElementByXpath('{path}'); y.loop=true;"
            d["group" +
                str(x)].execute_script(fun)
    time.sleep(2)
    print(f'Viewer number {x} successfully created!')

print('Done, all viewer created successfully!')
