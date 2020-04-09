from requests import get, put
import json

url_fl = "http://127.0.0.1:5000"
index = '/'
todo = '/todo1'
add = 1
while(add == 1): 
  x = input("Enter data to add to the list :")
  put(url_fl+todo, data={'data':x})
  add = int(input("add more : 1/0 :"))
  print(get(url_fl+todo).json())

get(url_fl+todo).json()
#put('http://localhost:5000/todo1', data={'data': 'Remember the milk'}).json()