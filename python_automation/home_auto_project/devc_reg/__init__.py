from flask import Flask
import markdown #to handle the markdown 
import os
import shelve #for data persistence 

#important flask stuff
from flask import g
from flask_restful import Resource, Api, 

app_for_reg = Flask(__name__)


#with statement - better exceptions handling and closes the file automatically 


@app_for_reg.route("/")
def index():
  with open('./README.md') as mark_d_file:
    data = mark_d_file.read()
  return markdown.markdown(data)