from flask import Flask, render_template
from dotenv import load_dotenv
import os
from controls.video_stream import video_feed
from controls.steering_control import control_steering
from controls.throttle_control import control_throttle

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Load the Raspberry Pi API URL from environment variables
RPI_API_URL = os.getenv('RPI_API_URL')

@app.route('/')
def index():
    return render_template('index.html', rpi_api_url=RPI_API_URL)

app.add_url_rule('/video', 'video_feed', video_feed)
app.add_url_rule('/control/steering', 'control_steering', control_steering, methods=['POST'])
app.add_url_rule('/control/throttle', 'control_throttle', control_throttle, methods=['POST'])
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
