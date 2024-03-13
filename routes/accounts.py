from flask_restful import Resource
from flask import request, session

from models.models import Account
from config import api, db

class Accounts(Resource):
    def get(self):
        list = []

        for account in Account.query.all():
            account_obj = account.to_dict()
            list.append(account_obj)

        return list, 200
    
api.add_resource(Accounts, "/accounts")