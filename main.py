from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from distutils.dir_util import copy_tree
import time
import os
from pyvirtualdisplay import Display

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
for x in range(2):
    if os.path.isdir(f'./Profile {x}') == False:
        from_directory = './profile'
        to_directory = f'./Profile {x}'
        copy_tree(from_directory, to_directory)
    options.add_argument(
        f"--user-data-dir=./Profile {x}")
    d["group" + str(x)] = webdriver.Chrome(
        executable_path=r'./chromedriver', options=options)
    d["group" +
        str(x)].get("https://www.youtube.com/results?search_query=OGdangID pubg lite")
    time.sleep(5)
    find = d["group" + str(x)].find_element(
        "xpath", f"(//a[@id='video-title'])[1]").click()
    time.sleep(5)

print('y')
