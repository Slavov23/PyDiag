def main():
    print("========================")
    print("     PyDiag v1.0")
    print("========================")
    print("1. Check DNS")
    print("2. Check TCP port")
    print("0. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        print("DNS check selected")
    elif choice == "2":
        print("TCP port check selected")
    elif choice == "0":
        print("Goodbye!")
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()