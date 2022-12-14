#create driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
import os
import sys

#path of executable ".exe"
app_path = os.path.dirname(sys.executable)

recent = datetime.now()
#day and year
time_recent = recent.strftime("%d%m%y")

#define website
website = "https://www.thesun.co.uk/sport/football/"
path = "C:/chrome driver/chromedriver"

#headless mode
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service,options=options)

#open driver
driver.get(website)

#import to csv file
titles = []
subtitles = []
links = []
#find element
containers = driver.find_elements(by="xpath",value='//div[@class="teaser__copy-container"]')

for container in containers:
    title = container.find_element(by="xpath",value='./a/h2').text
    subtitle = container.find_element(by="xpath",value='./a/p').text
    link = container.find_element(by="xpath",value='./a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)
    
#create dataframe
dict_ = {'Titles':titles,'Subtitles':subtitles,'Links':links}
df_headlines = pd.DataFrame(dict_)

file_name = f'headlines--{time_recent}.csv'
folder_path = os.path.join(app_path,file_name)
df_headlines.to_csv(folder_path)

driver.quit()


