from pyngrok import ngrok
import time

# Start ngrok tunnel
http_tunnel = ngrok.connect(3000)
print(f"Public URL: {http_tunnel.public_url}")

# Keep the script running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nShutting down ngrok tunnel...")
    ngrok.kill() 