from flask import Flask, render_template
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Load the Raspberry Pi API URL from environment variables
RPI_API_URL = os.getenv('RPI_API_URL')

@app.route('/')
def index():
    return render_template('index.html', rpi_api_url=RPI_API_URL)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
