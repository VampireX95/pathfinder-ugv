from flask import request, jsonify
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
throttle_channel = 1  # Adjust as needed

def control_throttle():
    data = request.json
    power = float(data.get('power', 0))  # Default to 0 (neutral)
    power = max(0, min(180, power))  # Constrain to range (ESC specific)
    kit.servo[throttle_channel].angle = power
    return jsonify({'status': 'success', 'throttle_power': power})