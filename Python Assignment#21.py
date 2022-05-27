#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Answer1:

nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))


# In[1]:


##Answer2:

word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")


# In[3]:


##Answer3:

h_age = int(input("Input a dog's age in human years: "))

if h_age < 0:
    print("Age must be positive number.")
    exit()
elif h_age <= 2:
    d_age = h_age * 10.5
else:
    d_age = 21 + (h_age - 2)*4

print("The dog's age in dog's years is", d_age)


# In[4]:


##Answer4:

def checkTriangle(x, y, z):

    if x == y == z:
        print("Equilateral Triangle")

    elif x == y or y == z or z == x:
        print("Isosceles Triangle")

    else:
        print("Scalene Triangle")

x = 8
y = 7
z = 9

checkTriangle(x, y, z)


# In[5]:


##Answer5:

def abc():
    x = 1
    y = 2
    str1= "giri"
    print("Python Exercises")

print(abc.__code__.co_nlocals)


# In[6]:


##Answer6:

mycode = 'print("hello world")'
code = """
def mutiply(x,y):
    return x*y

print('Multiply of 2 and 3 is: ',mutiply(2,3))
"""
exec(mycode)
exec(code)


# In[7]:


##Answer7:

def tuples_to_list_string(lst):
    result = list(map(' '.join, lst))
    return result   
colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print("Original list of tuples:")
print(colors)
print("\nConvert the said list of tuples to a list of strings:")
print(tuples_to_list_string(colors))
names = [('Sheridan','Gentry'), ('Laila','Mckee'), ('Ahsan','Rivas'), ('Conna','Gonzalez')]
print("\nOriginal list of tuples:")
print(names)
print("\nConvert the said list of tuples to a list of strings:")
print(tuples_to_list_string(names))


# In[8]:


##Answer8:

def list_of_dicts(marks):
    result = map(dict, zip(*[[(key, val) for val in value] for key, value in marks.items()]))
    return list(result)
marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print("Original dictionary of lists:")
print(marks)
print("\nSplit said dictionary of lists into list of dictionaries:")
print(list_of_dicts(marks))


# In[ ]:


##Answer9:

import os
root = 'g:\\testpath\\'
for entry in os.scandir(root):
    if entry.is_dir():
        typ = 'dir'
    elif entry.is_file():
        typ = 'file'
    elif entry.is_symlink():
        typ = 'link'
    else:
        typ = 'unknown'
    print('{name} {typ}'.format(
       name=entry.name,
       typ=typ,
   ))


# In[11]:


##Answer10:

import time
import datetime
print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))


# In[12]:


##Answer11:

import requests
payload = {'key1': 'value1', 'key2': 'value2'}
print("Parameters: ",payload)
r = requests.get('https://httpbin.org/get', params=payload)
print("Print the url to check the URL has been correctly encoded or not!")
print(r.url)
print("\nPass a list of items as a value:")
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
print("Parameters: ",payload)
r = requests.get('https://httpbin.org/get', params=payload)
print("Print the url to check the URL has been correctly encoded or not!")
print(r.url)


# In[13]:


##Answer12:

import requests
r = requests.get('https://api.github.com/')
response = r.headers
print("Headers information of the said response:")
print(response)
print("\nVarious Key-value pairs information of the said resource and request:")

print("Date: ",r.headers['date'])
print("server: ",r.headers['server'])
print("status: ",r.headers['status'])
print("cache-control: ",r.headers['cache-control'])
print("vary: ",r.headers['vary'])
print("x-github-media-type: ",r.headers['x-github-media-type'])
print("access-control-expose-headers: ",r.headers['access-control-expose-headers'])
print("strict-transport-security: ",r.headers['strict-transport-security'])
print("x-content-type-options: ",r.headers['x-content-type-options'])
print("x-xss-protection: ",r.headers['x-xss-protection'])
print("referrer-policy: ",r.headers['referrer-policy'])
print("content-security-policy: ",r.headers['content-security-policy'])
print("content-encoding: ",r.headers['content-encoding'])
print("X-Ratelimit-Remaining: ",r.headers['X-Ratelimit-Remaining'])
print("X-Ratelimit-Reset: ",r.headers['X-Ratelimit-Reset'])
print("X-Ratelimit-Used: ",r.headers['X-Ratelimit-Used'])
print("Accept-Ranges:",r.headers['Accept-Ranges'])
print("X-GitHub-Request-Id:",r.headers['X-GitHub-Request-Id'])


# In[14]:


##Answer13:

import csv
csv_columns = ['id','Column1', 'Column2', 'Column3', 'Column4', 'Column5']
dict_data = {'id':['1', '2', '3'],
    'Column1':[33, 25, 56],
    'Column2':[35, 30, 30],
    'Column3':[21, 40, 55],
    'Column4':[71, 25, 55],
    'Column5':[10, 10, 40], }
csv_file = "temp.csv"
try:
   with open(csv_file, 'w') as csvfile:
       writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
       writer.writeheader()
       for data in dict_data:
           writer.writerow(dict_data)
except IOError:
   print("I/O error")
data = csv.DictReader(open(csv_file))
print("CSV file as a dictionary:\n")
for row in data:
   print(row)


# In[ ]:


##Answer14:

import csv
fields = []
rows = []
with open('departments.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ', quotechar=',')
 
 fields = next(data)
 for row in data:
   print(', '.join(row))
print("\nTotal no. of rows: %d"%(data.line_num))
print('Field names are:')
print(', '.join(field for field in fields))


# In[16]:


##Answer15:

import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))


# In[ ]:




