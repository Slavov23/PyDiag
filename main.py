
import platform
import socket


def check_dns():
    hostname = input("Enter hostname: ").strip()

    if not hostname:
        print("[Error] Hostname cannot be empty")
        return

    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"[Success] {hostname} resolved to {ip_address}")
    except socket.gaierror:
        print(f"[Error] Could not resolve hostname: {hostname}")


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

    except socket.gaierror:
        print(f"[Error] Could not resolve hostname: {hostname}")
    except ConnectionRefusedError:
        print(f"[Info] Connection refused on port {port}")
    except socket.timeout:
        print(f"[Info] Connection timed out on port {port}")
    except OSError as error:
        print(f"[Error] Connection failed: {error}")


def get_system_info():
    return {
        "system": platform.system(),
        "hostname": platform.node(),
        "python_version": platform.python_version()
    }


def main():
    while True:
        print("\n========================")
        print("       PyDiag v1.0")
        print("========================")
        print("1. Check DNS")
        print("2. Check TCP port")
        print("3. System information")
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

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("[Error] Invalid option. Please choose 0, 1, 2 or 3.")


if __name__ == "__main__":
    main()
