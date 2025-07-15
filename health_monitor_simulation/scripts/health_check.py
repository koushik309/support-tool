import os
import sys
import socket
import logging
import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger('ServerHealthCheck')

def main():
    """Main health check function"""
    # Get configuration
    hostname = os.getenv('SERVER_HOST', 'sys2')  # Default to Docker service name
    port = int(os.getenv('SERVER_PORT', '60000'))
    timeout = float(os.getenv('CONNECTION_TIMEOUT', '2.0'))
    
    # Try hostname resolution
    try:
        ip = socket.gethostbyname(hostname)
        logger.info(f"Resolved {hostname} → {ip}")
    except socket.gaierror:
        logger.warning(f"DNS resolution failed for {hostname}")
        ip = hostname
    
    # Check server status
    try:
        url = f"http://{ip}:{port}/health"
        logger.info(f"Checking server at {url}")
        response = requests.get(url, timeout=timeout)
        
        if response.status_code == 200:
            data = response.json()
            logger.info(f"✅ Server is running! Version: {data['version']}")
            logger.info(f"Uptime: {data['uptime']} seconds")
            return True
        else:
            logger.error(f"⚠️ Unexpected status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logger.error(f"🔴 Connection failed: {type(e).__name__} - {str(e)}")
    
    return False

if __name__ == "__main__":
    if main():
        logger.info("STATUS: ONLINE")
        sys.exit(0)
    else:
        logger.error("STATUS: OFFLINE")
        sys.exit(1)  # Fixed sys.error(1) to sys.exit(1)