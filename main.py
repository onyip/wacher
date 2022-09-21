from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options = Options()
# options.add_argument(
#     "--user-data-dir=/home/developer/.config/google-chrome/Profile 19/Profile 01")
options.add_extension(
    './extension/01.crx')
options.add_extension(
    './extension/02.crx')
options.add_extension(
    './extension/03.crx')

options.add_argument("--window-size=100,300")
driver = webdriver.Chrome(executable_path=r'./chromedriver', options=options)
driver.get("https://www.youtube.com/results?search_query=ogdangid pubg")

video_number = 1
find = driver.find_element(
    "xpath", f"(//a[@id='video-title'])[{video_number}]").click()

find = driver.find_element(
    By.XPATH("//span[contains(string(),'144p')]")).click()


# driver.find_element_by_xpath("//div[contains(text(),'Quality')]").click()

# find = driver.find_element(
# "xpath", f"(//span[contains(string(),'144p')])").click()
# driver.FindElement(By.XPath("//span[contains(string(),'144p')]")).Click()
