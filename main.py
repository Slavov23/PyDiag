import platform
import socket


def check_tcp_port():
    hostname = input("Enter hostname: ")

    try:
        port = int(input("Enter port: "))

        with socket.create_connection((hostname, port), timeout=3):
            print(f"[Success] Port {port} is OPEN on {hostname}")

    except ValueError:
        print("[Error] Port must be a number")

    except socket.gaierror:
        print(f"[Error] Could not resolve hostname: {hostname}")

    except ConnectionRefusedError:
        print(f"[Error] Port {port} is CLOSED on {hostname}")

    except TimeoutError:
        print(f"[Error] Connection timed out")

    except OSError as error:
        print(f"[Error] Connection failed: {error}")


def check_dns():
    hostname = input("Enter hostname: ")

    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"[Success] {hostname} resolved to {ip_address}")
    except socket.gaierror:
        print(f"[Error] {hostname} not resolved")

def get_system_info():
    system = platform.system()
    hostname = platform.node()

    return {
        "system": system,
        "hostname": hostname
    }


def main():
    print("========================")
    print("     PyDiag v1.0")
    print("========================")
    print("1. Check DNS")
    print("2. Check TCP port")
    print("3. System information")
    print("0. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        check_dns()
    elif choice == "2":
        check_tcp_port()
    elif choice == "3":
        info = get_system_info()
        print("Operating system:", info["system"])
        print("Hostname:", info["hostname"])
    elif choice == "0":
        print("Goodbye!")
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
