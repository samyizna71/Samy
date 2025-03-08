import time
import requests
import threading

# Tumhara server ka address aur port
SERVER_ADDRESS = "sam728y-nouZ.aternos.me"
PORT = 43662

# Ping URL jo server ko 24/7 active rakhega
PING_URL = f"http://{SERVER_ADDRESS}:{PORT}"

# Headers fake user-agent ke liye
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def keep_alive():
    while True:
        try:
            # Server ko har 30 second me ping karega
            response = requests.get(PING_URL, headers=HEADERS, timeout=5)
            if response.status_code == 200:
                print("✅ Server is still running...")
            else:
                print("🚀 Server might be down. Re-pinging...")
        except:
            print("🚀 Server might be down. Re-pinging...")
        
        # Har 30 second me server ko ping karega
        time.sleep(30)

# Background me ping script chalu rahegi
thread = threading.Thread(target=keep_alive)
thread.start()