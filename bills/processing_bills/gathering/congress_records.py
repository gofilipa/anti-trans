# if the request returns 404, then remove the volume & number 
# or add a number (-2, -3, -4) to the end. If that doesn't work,
# then do both and repeat

import requests # for making http (web) requests
import pandas as pd # for working with tabular (spreadsheet) data
import csv # also for working with tabular data, in csv format
from time import sleep
import random

# https://www.congress.gov/search?q=%7B%22source%22%3A%22congrecord%22%2C%22search%22%3A%22gender%22%2C%22congress%22%3A%22119%22%7D
bills = pd.read_csv('../bill_data/records-gender-119.csv')
df = pd.DataFrame(bills)
df = df.drop_duplicates(subset=['Title'], keep='first')

# separate date into three columns: year, month, day
# add zero in front of month and day if they are single digit
df[['Month', 'Day', 'Year']] = df['Issue Date'].str.split('/', expand=True)
df['Month'] = df['Month'].str.zfill(2)
df['Day'] = df['Day'].str.zfill(2)


def request(url):
    r = requests.get(url)
    return r

def add_one(url, num):
    num = num
    url = f'https://www.congress.gov/119/crec/20{year}/{month}/{day}/{volume}/{number}/modified/CREC-20{year}-{month}-{day}-pt1-Pg{page}{num+1}.htm'
    return new_url, new_num

def remove_volnum(url, num):
    num = num
    url = f'https://www.congress.gov/119/crec/20{year}/{month}/{day}/{volume}/modified/CREC-20{year}-{month}-{day}-pt1-Pg{page}{num}.htm'
    return new_new_url

gender_119 = []

for i in range(0, 10):
    year = df.iloc[i]['Year']
    month = df.iloc[i]['Month']
    day = df.iloc[i]['Day']
    volume = df.iloc[i]['Volume']
    number = df.iloc[i]['Number'] 
    page = df.iloc[i]['Page']

    url = f'https://www.congress.gov/119/crec/20{year}/{month}/{day}/{volume}/{number}/modified/CREC-20{year}-{month}-{day}-pt1-Pg{page}.htm'
    
r = request(url)

while r.status_code == 404:
    # add one
    url, num = add_one(url, num)
    r = request(url)
    sleep(random.uniform(.1, 3))

while r.status_code == 404:
    num = 1
    url, num = remove_volnum(url, num)
    r = request(url)
    sleep(random.uniform(.1, 3))

if r.status_code == 200:
    text = r.text
    gender_119.append(text)

# sleep for a random amount of time between .1 and 3 seconds
sleep(random.uniform(.1, 3))

# save list to txt file
with open('../records_texts/records-gender-119.txt', 'w') as f:
    for item in gender_119:
        f.write(item)
