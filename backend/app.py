from flask import Flask, jsonify, request, send_from_directory
import subprocess
import threading
import os

app = Flask(__name__)

# Function to run the deauthentication attack
def run_deauth(target_mac, ap_mac, iface):
    command = f"sudo python3 deauth.py {target_mac} {ap_mac} {iface}"
    subprocess.call(command, shell=True)

# Route to serve the main HTML page
@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

# API endpoint to start the deauthentication attack
@app.route('/deauth', methods=['POST'])
def deauth():
    data = request.json
    target_mac = data.get('target_mac')
    ap_mac = data.get('ap_mac')
    iface = data.get('iface')

    # Run the deauth attack in a separate thread
    thread = threading.Thread(target=run_deauth, args=(target_mac, ap_mac, iface))
    thread.start()

    return jsonify({"status": "Deauthentication attack started."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
