from flask import Blueprint, request, jsonify
import pyotp
from models.models import User 
from config import api, db


two_fa_blueprint = Blueprint('two_fa', __name__)

@two_fa_blueprint.route('/enable-2fa', methods=['GET'])
def enable_2fa():
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    user._totp_secret = pyotp.random_base32()

    db.session.add(user)
    db.session.commit()

    totp = pyotp.TOTP(user._totp_secret)
    uri = totp.provisioning_uri(name=user.email, issuer_name='Money Magnet')
    return jsonify({"qr_code_uri": uri, 'totp_secret': user._totp_secret})

@two_fa_blueprint.route('/verify-otp', methods=['POST'])
def verify_otp():
    user_id = request.json.get('user_id')
    otp = request.json.get('otp')
    
    user = User.query.get(user_id)
    if not user or not user._totp_secret:
        return jsonify({"error": "Invalid user or 2FA not set up"}), 400

    totp = pyotp.TOTP(user._totp_secret)
    if totp.verify(otp):
        return jsonify({"success": "OTP verified"}), 200
    else:
        return jsonify({"error": "Invalid OTP"}), 400
