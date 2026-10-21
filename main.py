
import platform
import socket
import subprocess
import logging


def check_dns():
    hostname = input("Enter hostname: ").strip()

    if not hostname:
        print("[Error] Hostname cannot be empty")
        return

    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"[Success] {hostname} resolved to {ip_address}")
        logging.info("DNS resolved: %s -> %s", hostname, ip_address)
    except socket.gaierror:
        print(f"[Error] Could not resolve hostname: {hostname}")
        logging.error("DNS resolution failed: %s", hostname)

def check_tcp_port():
    hostname = input("Enter hostname: ").strip()

    if not hostname:
        print("[Error] Hostname cannot be empty")
        return

    try:
        port = int(input("Enter port (1-65535): "))

        if port < 1 or port > 65535:
            print("[Error] Port must be between 1 and 65535")
            return

    except ValueError:
        print("[Error] Port must be a number")
        return

    try:
        with socket.create_connection((hostname, port), timeout=3):
            print(f"[Success] Port {port} is OPEN on {hostname}")
            logging.info("TCP connection successful: %s:%s", hostname, port)

    except socket.gaierror:
        print(f"[Error] Could not resolve hostname: {hostname}")
    except ConnectionRefusedError:
        print(f"[Info] Connection refused on port {port}")
        logging.warning("TCP connection refused: %s:%s", hostname, port)
    except socket.timeout:
        print(f"[Info] Connection timed out on port {port}")
        logging.warning("TCP connection timed out: %s:%s", hostname, port)
    except OSError as error:
        print(f"[Error] Connection failed: {error}")



def ping_check():
    host = input("Enter hostname or IP: ").strip()

    if not host:
        print("[Error] Host cannot be empty")
        return

    # Избираме параметрите според операционната система
    if platform.system() == "Windows":
        command = ["ping", "-n", "1", "-w", "3000", host]
    else:
        command = ["ping", "-c", "1", "-W", "3", host]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode == 0:
            print(f"[Success] Host {host} is reachable")
            logging.info("Ping successful: %s", host)
        else:
            print(f"[Info] Host {host} did not respond to ping")
            logging.warning("Ping failed: %s", host)

    except subprocess.TimeoutExpired:
        print("[Error] Ping timed out")

    except FileNotFoundError:
        print("[Error] Ping command was not found")



def get_system_info():
    return {
        "system": platform.system(),
        "hostname": platform.node(),
        "python_version": platform.python_version()
    }


def get_network_info():
    hostname = socket.gethostname()

    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip_address = "Unavailable"

    return {
        "hostname": hostname,
        "ip_address": ip_address
    }


logging.basicConfig(
    filename="pydiag.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%y-%m-%d %H:%M:%S",
)


def main():
    while True:
        print("\n========================")
        print("       PyDiag v1.0")
        print("========================")
        print("1. Check DNS")
        print("2. Check TCP port")
        print("3. System information")
        print("4. Ping Check")
        print("5. Network Information")
        print("0. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            check_dns()


        elif choice == "2":
            check_tcp_port()

        elif choice == "3":
            info = get_system_info()
            print("\n--- System Information ---")
            print("Operating system:", info["system"])
            print("Hostname:", info["hostname"])
            print("Python version:", info["python_version"])

        elif choice == "4":
            ping_check()
            print("4. Ping Check")

        elif choice == "5":
            info = get_network_info()
            print("\n--- Network Information ---")
            print("Hostname:", info["hostname"])
            print("IPv4 address:", info["ip_address"])
            logging.info(
                "Network information retrieved: %s, %s",
                info["hostname"],
                info["ip_address"]
            )

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("[Error] Invalid option. Please choose 0, 1, 2 or 3.")


if __name__ == "__main__":
    main()
