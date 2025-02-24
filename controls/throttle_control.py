from flask import request, jsonify
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
steering_channel = 0  # Adjust as needed

def control_steering():
    data = request.json
    angle = float(data.get('angle', 90))  # Default to center position
    angle = max(0, min(180, angle))  # Constrain to servo range
    kit.servo[steering_channel].angle = angle
    return jsonify({'status': 'success', 'steering_angle': angle})