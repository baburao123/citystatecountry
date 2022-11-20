from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import json

# countryListFile = open('address_country.json',encoding="utf8")
# stateListFile = open('address_state.json',encoding="utf8")
# cityListFile = open('address_city.json',encoding="utf8")

# countryList = json.load(countryListFile)
# stateList = json.load(stateListFile)
# cityList = json.load(cityListFile)

# countryList = countryList[2]['data']
# stateList = stateList[2]['data']
# cityList = cityList[2]['data']


# # creating the flask app
# app = Flask(__name__)
# # creating an API object
# api = Api(app)

# class Country(Resource):
#     def get(self):
#         return jsonify({'status':True,result:countryList})
    
# class State(Resource):
#     def get(self,cid):
#         arr = []
#         for i in stateList:
#             if i['country_id'] == str(cid):
#                 arr.append(i)
#         if len(arr)>0:
#             return jsonify({'status': True,'result':arr})
#         return jsonify({'status': False})
    
# class City(Resource):
#     def get(self,cid,sid):
#         if sid == None:
#             return State().get(cid)
#         arr = []
#         for i in cityList:
#             if i['country_id'] == str(cid) and i['state_id'] == str(sid):
#                 arr.append(i)
#         if len(arr)>0:
#             return jsonify({'status': True,'result':arr})
#         return jsonify({'status': False})


# # adding the defined resources along with their corresponding urls
# api.add_resource(Country, '/')
# api.add_resource(State, '/<int:cid>')
# api.add_resource(City, '/<int:cid>/<int:sid>')


# # driver function
# if __name__ == '__main__':

# 	app.run(debug = True)
