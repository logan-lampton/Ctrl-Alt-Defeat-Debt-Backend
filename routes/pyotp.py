from flask_restful import Resource
from flask import request, session
from config import api, db

from models.models import User
import pyotp

class Generate_totp_secret(Resource):

    def post(self):
        totp_secret = pyotp.random_base32()
        user_id = session.get("user_id")
        user = User.query.filter(User.id == user_id).first()
        user['totp_secret'] = totp_secret

        return {"totp_secret": totp_secret}, 200

    # @app.route('/generate_totp_secret/<int:user_id>', methods=['POST'])
    # def generate_totp_secret(user_id):
    #     totp_secret = pyotp.random_base32()
    #     users[user_id]['totp_secret'] = totp_secret
    #     return jsonify({'totp_secret': totp_secret})

class Verify_totp(Resource):

    def post(self):
        user_id = session.get("user_id")
        if not user_id:
            return {"message": "User not found"}, 401
        
        user = User.query.filter(User.id == user_id).first()
        totp_secret = user.totp_secret
        totp_code = request.get_json()['totp_code']
        if not totp_secret or not totp_code:
            return {'message': 'TOTP secret or code not provided'}, 401
        
        totp = pyotp.TOTP(totp_secret)
        if totp.verify(totp_code):
            return {'message': 'Verification successful'}, 200
        else:
            return {'message': 'Invalid TOTP code'}, 401
    
    # @app.route('/verify_totp/<int:user_id>', methods=['POST'])
    # def verify_totp(user_id):
    #     user = users.get(user_id)
    #     if not user:
    #         return jsonify({'message': 'User not found'}), 404

    #     totp_secret = user['totp_secret']
    #     totp_code = request.json.get('totp_code')
    #     if not totp_secret or not totp_code:
    #         return jsonify({'message': 'TOTP secret or code not provided'}), 400

    #     totp = pyotp.TOTP(totp_secret)
    #     if totp.verify(totp_code):
    #         return jsonify({'message': 'Verification successful'})
    #     else:
    #         return jsonify({'message': 'Invalid TOTP code'}), 401
        
api.add_resource(Generate_totp_secret, "/generate_totp_secret/<int:user_id>")
api.add_resource(Verify_totp, "/verify_totp/<int:user_id>")
    
