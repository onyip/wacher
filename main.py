from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# options.add_argument(
#     "--user-data-dir=/home/developer/.config/google-chrome/Profile 19/Profile 01")
options = Options()
options.add_extension(
    './extension/01.crx')
options.add_extension(
    './extension/02.crx')
options.add_extension(
    './extension/03.crx')

options.add_argument("--window-size=100,300")
d = {}
for x in range(30):
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
