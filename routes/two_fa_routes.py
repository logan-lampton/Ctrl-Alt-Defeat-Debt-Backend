from flask import Blueprint, request, jsonify
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Twilio client with environment variables
twilio_client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
verification_service_sid = os.getenv('TWILIO_VERIFICATION_SERVICE_SID')

two_fa_blueprint = Blueprint('two_fa', __name__)

@two_fa_blueprint.route('/enable-2fa', methods=['POST'])
def enable_2fa():
    # Hardcoded phone number
    phone_number = '+12124959732'
    
    try:
        verification = twilio_client.verify.services(verification_service_sid) \
            .verifications.create(to=phone_number, channel='sms')
        return jsonify({"message": "Verification code sent via SMS"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@two_fa_blueprint.route('/verify-otp', methods=['POST'])
def verify_otp():
    # Assuming the user_id or another form of identification is still part of the request to identify the user in your system
    code = request.json.get('otp')
    
    # Hardcoded phone number for verification
    phone_number = '+12124959732'
    
    try:
        verification_check = twilio_client.verify \
            .services(verification_service_sid) \
            .verification_checks \
            .create(to=phone_number, code=code)

        if verification_check.status == 'approved':
            return jsonify({"message": "OTP verified successfully"}), 200
        else:
            return jsonify({"error": "Invalid OTP"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
