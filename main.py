from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from distutils.dir_util import copy_tree
from pyvirtualdisplay import Display
from selenium import webdriver
import random
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
foo = [
    'https://www.youtube.com/watch?v=zUu64aJuOvg&loop=50',
]
for x in range(int(sys.argv[1])):
    if os.path.isdir(f'./Profile {x}') == False:
        from_directory = './profile'
        to_directory = f'./Profile {x}'
        copy_tree(from_directory, to_directory)
    options.add_argument(
        f"--user-data-dir=./Profile {x}")
    d["group" + str(x)] = webdriver.Chrome(
        executable_path=r'./chromedriver', options=options)
    d["group" + str(x)].get(f'{random.choice(foo)}')
    # time.sleep(10)
    # find = d["group" + str(x)].find_element(
    #     "xpath", f'//*[@id="movie_player"]/div[4]/button').click()
    element = WebDriverWait(d["group" + str(x)], 60).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="movie_player"]/div[4]/button')))
    element.click()
print('y')
