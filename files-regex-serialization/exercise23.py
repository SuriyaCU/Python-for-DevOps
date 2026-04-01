import subprocess
import sys

def check_host_status(hostname: str) -> str:
    """
    Checks if a host is online by pinging it a limited number of times.

    Args:
        hostname (str): The hostname or IP address to ping.

    Returns:
        'online' if the host is reachable (ping exit code 0), 'offline' otherwise.
    
    Raises:
        TypeError: If hostname is not a string.
        ValueError: If hostname is not a non-empty string.
    """
    # 1. Input Validation
    if not isinstance(hostname, str):
        raise TypeError("hostname must be a string.")
    
    if not hostname.strip():
        raise ValueError("hostname cannot be an empty string.")

    # 2. Construct the ping command for Linux/macOS
    # -c 3: send 3 packets
    # -W 1: wait 1 second for a response (optional, but good practice)
    command = ["ping", "-c", "3", hostname]

    try:
        # 3. Execute the command
        # timeout=5: kill the process if it exceeds 5 seconds
        # capture_output=True: prevents output from printing to the console
        result = subprocess.run(
            command, 
            timeout=5, 
            capture_output=True, 
            text=True
        )

        # 4. Check exit code
        if result.returncode == 0:
            return "online"
        else:
            return "offline"

    except (subprocess.TimeoutExpired, Exception):
        # 5. Handle timeouts or unexpected execution errors as 'offline'
        return "offline"

# --- Example Usage ---
if __name__ == "__main__":
    # Test with Google DNS
    print(f"Status of 8.8.8.8: {check_host_status('8.8.8.8')}")
    
    # Test with a non-existent local IP
    print(f"Status of 10.255.255.1: {check_host_status('10.255.255.1')}")