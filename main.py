from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from distutils.dir_util import copy_tree
import time
import os

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
    if os.path.isdir(f'/home/developer/.config/google-chrome/Profile {x}') == False:
        from_directory = './profile'
        to_directory = f'/home/developer/.config/google-chrome/Profile {x}'
        copy_tree(from_directory, to_directory)
    options.add_argument(
        f"--user-data-dir=/home/developer/.config/google-chrome/Profile {x}")
    d["group" + str(x)] = webdriver.Chrome(
        executable_path=r'./chromedriver', options=options)
    d["group" +
        str(x)].get("https://www.youtube.com/results?search_query=ogdangid pubg")
    time.sleep(5)
    video_number = 1
    find = d["group" + str(x)].find_element(
        "xpath", f"(//a[@id='video-title'])[{video_number}]").click()
    time.sleep(5)

print('y')
