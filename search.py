from ast import If
from itertools import count
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from distutils.dir_util import copy_tree
from pyvirtualdisplay import Display
from selenium import webdriver
from colorama import Fore
import time
import sys
import os

display = Display(visible=0, size=[800, 600])
display.start()

options = Options()
options.add_extension(
    './extension/01.crx')
options.add_extension(
    './extension/02.crx')
options.add_extension(
    './extension/03.crx')
options.add_argument("--window-size=100,300")
d = {}
cont = 0
for x in range(int(sys.argv[1])):
    print(Fore.BLUE + f'Creating on viewer number {x}')
    if os.path.isdir(f'./Profile {x}') == False:
        from_directory = './profile'
        to_directory = f'./Profile {x}'
        copy_tree(from_directory, to_directory)
    options.add_argument(
        f"--user-data-dir=./Profile {x}")
    try:
        d["group" + str(x)] = webdriver.Chrome(
            executable_path=r'./chromedriver', options=options)
    except:
        d["group" + str(x)] = ''
        print(Fore.RED + "Filed Start Vrome Driver Plase Restart Mechine!")

    if d["group" + str(x)] != '':
        d["group" +
            str(x)].get('https://www.youtube.com/results?search_query=Ubuntu+Screencast+Tutorial+#limitlesstutorial')
        time.sleep(5)
        links = WebDriverWait(d["group" + str(x)], 5).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.yt-simple-endpoint.style-scope.ytd-video-renderer#video-title")))
        for y in links:
            try:
                lix = y.get_attribute("href")
            except:
                lix = ''
                print(Fore.RED + "Filed get link from list!")
            if lix == 'https://www.youtube.com/watch?v=zUu64aJuOvg':
                time.sleep(3)
                try:
                    y.click()
                    cont = cont + 1
                    print(Fore.GREEN +
                          f'video clicked!, Total video clicked is {cont}')
                    time.sleep(7)
                except:
                    print(Fore.RED + "Filed to click video!")
                try:
                    find = d["group" + str(x)].find_element(
                        "xpath", f"//*[@id='skip-button:6']/span/button").click()
                    print(Fore.MAGENTA + "Ads skiped!")
                    time.sleep(3)
                except:
                    print(Fore.LIGHTBLACK_EX + "No ads detected!")
                path = '//*[@id="movie_player"]/div[1]/video'
                p = '{return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}'
                fun = f"function getElementByXpath(path) {p} let y = getElementByXpath('{path}'); y.loop=true;"
                try:
                    d["group" +
                        str(x)].execute_script(fun)
                except:
                    print(Fore.RED + "Filed Run JS")
        time.sleep(2)
        print(Fore.CYAN + f'Viewer number {x} successfully created!')

print('Done, all viewer created successfully!')
