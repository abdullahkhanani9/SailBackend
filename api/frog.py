from flask import Blueprint, jsonify
from flask_restful import Api, Resource
import random
import requests  # Add this import statement
from model.frog_items import *  # Make sure this import is correct

frog_item_api = Blueprint('frog_item_api', __name__,
                   url_prefix='/api/frog-items')

api = Api(frog_item_api)

# Rest of your code remains the same

if __name__ == "__main__": 
    server = 'https://your-server-url-here'  # Replace with your actual server URL
    url = server + "/api/frog-items"
    responses = []

    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']

    num = str(random.randint(0, count-1))
    responses.append(
        requests.get(url+"/"+num)
    ) 
    responses.append(
        requests.put(url+"/like/"+num)
    ) 
    responses.append(
        requests.put(url+"/dislike/"+num)
    ) 

    responses.append(
        requests.get(url+"/random")
    ) 

    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")
