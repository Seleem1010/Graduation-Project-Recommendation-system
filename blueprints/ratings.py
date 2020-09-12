from flask import Blueprint, jsonify, request, make_response
import models.ratings_model as rm

ratings = Blueprint('ratings', __name__)

@ratings.route('', methods=['POST'])
def add_new_rating():
    id = 1
    uid = request.json['uid']
    pid = request.json['pid']
    rate = request.json['rate']

    new_rate = rm.add_rate(rate, pid ,uid)
    return make_response(jsonify(id), 201)

@ratings.route('<id>', methods=['PUT'])
def change_rating():
    id = 1
    rate = request.json['rate']

    edited_rate = rm.edit_rate(id, rate)
    return make_response(jsonify(id), 200)

