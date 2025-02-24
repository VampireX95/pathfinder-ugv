from flask import Flask
from video_stream import video_feed
from steering_control import control_steering
from throttle_control import control_throttle

app = Flask(__name__)

app.add_url_rule('/video', 'video_feed', video_feed)
app.add_url_rule('/control/steering', 'control_steering', control_steering, methods=['POST'])
app.add_url_rule('/control/throttle', 'control_throttle', control_throttle, methods=['POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)