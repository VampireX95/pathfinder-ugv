Here's a basic README for your project, which will guide someone through setting up the environment and installing the required packages to run the Flask app on the Raspberry Pi:

---

# Pathfinder UGV Control

This project allows you to control a Raspberry Pi-powered UGV (Unmanned Ground Vehicle) with a web interface. You can steer the vehicle and control its throttle using a simple Flask web app. The Raspberry Pi captures and streams video from the PiCamera, allowing you to monitor the UGV in real-time.

## Requirements

- **Raspberry Pi** (with Raspbian OS installed)
- **PiCamera** (or USB webcam for video feed)
- **PCA9685 Servo Driver HAT** (for controlling steering and throttle)
- **Internet Connection** (for setting up the Raspberry Pi and your PC)

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your Raspberry Pi:
```bash
git clone https://github.com/your-username/pathfinder-ugv.git
cd pathfinder-ugv
```

### 2. Install Dependencies

Make sure you have **Python 3** installed on your Raspberry Pi. Then, install the necessary Python packages using `pip`.

1. **Install Python dependencies**:
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-dev python3-venv
   sudo apt install libatlas-base-dev
   ```

2. **Install required Python packages**:
   ```bash
   pip3 install -r requirements.txt
   ```

   Create a `requirements.txt` file with the following content:
   ```
   Flask
   picamera
   adafruit-pca9685
   ```

   These packages are required for:
   - Flask: To serve the web interface.
   - PiCamera: To capture and stream video from the PiCamera.
   - adafruit-pca9685: To control the servos and ESC using the PCA9685 Servo Driver HAT.

### 3. Run the Flask App

1. **Navigate to the project directory**:
   ```bash
   cd /path/to/your/project
   ```

2. **Run the Flask app**:
   ```bash
   nohup python3 app.py &
   ```

   This will start the Flask app in the background. You can now access the UGV control interface from any device on the same network.

### 4. Access the Web Interface

On your PC or another device connected to the same network, open a browser and enter the Raspberry Pi's IP address with port `5000`:
```
http://<Raspberry_Pi_IP>:5000
```

You should see the control interface and video feed.

### 5. (Optional) Running the Flask App on Boot

To have the Flask app start automatically on boot, follow the instructions for setting up the app with `systemd` as described earlier.

## Usage

- **Steering**: Use the left, center, and right buttons to control the steering.
- **Throttle**: Use the stop, half-speed, and full-speed buttons to control the throttle.
- **Video Feed**: The live video feed from the PiCamera is displayed on the webpage.

## Troubleshooting

- **Camera not working**: Make sure the PiCamera is enabled. Run `raspi-config` and enable the camera under "Interfacing Options".
- **Control not responding**: Verify that the Raspberry Pi and PC are on the same network and can communicate.

## License

This project is open-source and available under the MIT License.

---

This README should help anyone set up the project from scratch. You can customize it further with more specific instructions, particularly if you're setting up any custom hardware or configurations.

Let me know if you need any additional modifications or clarifications!