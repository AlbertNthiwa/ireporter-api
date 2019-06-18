from flask import Flask, jsonify, make_response, request, abort
from flask_restful import Resource

posts = []

class RedFlags(Resource):

   def __init__(self):
       self.db = posts
       self.id = len(posts) + 1

   def get(self):

       return make_response(jsonify({
           "status" : 200,
           "data" : self.db
       }), 200)


   def post(self):

       data = {
           'id' : self.id,
           'createdBy' : request.json['createdBy'],
           'type' : 'red-flags',
           'location' : request.json['location'],
           'status' : "Under Investigation",
           'images' : request.json['images'],
           'videos' : request.json['videos'],
           'title' : request.json['title'],
           'comment' : request.json['comment']
       }
       self.db.append(data)

       success_message = {
           'id' : self.id,
           'message' : 'Red-Flag Created'
       }

       return make_response(jsonify({
           "status" : 201,
           "data" : success_message
       }), 201)

class RedFlag(Resource):

   def __init__(self):
       self.db = posts
       self.id = len(posts) + 1
   def get(self, redflag_id):

       for post in posts:
           if post['id'] == redflag_id:
               return make_response(jsonify({
                   "status" : 200,
                   "data" : post
               }), 200)  

   def put(self, redflag_id):
       data = {
           'id' : redflag_id,
           'createdBy' : request.json['createdBy'],
           'type' : 'red-flags',
           'location' : request.json['location'],
           'status' : "Pending",
           'images' : request.json['images'],
           'videos' : request.json['videos'],
           'title' : request.json['title'],
           'comment' : request.json['comment']
       }
       for post in posts:
           if post['id'] == redflag_id:
               posts[self.id] = data
               return make_response(jsonify({
                   "status" : 201,
"data" : post
               }), 201)

   def delete(self, redflag_id):
        for post in posts:
           if post['id'] == redflag_id:
               posts.pop(redflag_id - 1)
               success_message = {
               'id' : self.id,
               'message' : 'Red-Flag Deleted'
               }
               return make_response(jsonify({
               "status" : 204,
               "data" : success_message
               }), 204)
