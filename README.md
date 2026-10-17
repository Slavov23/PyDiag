тест# PyDiag — Python IT Diagnostics Tool
[![PyDiag Tests](https://github.com/Slavov23/PyDiag/actions/workflows/tests.yml/badge.svg)](https://github.com/Slavov23/PyDiag/actions/workflows/tests.yml)

PyDiag is a lightweight command-line IT diagnostics tool built with Python. It provides basic network diagnostic checks and system information through an interactive menu.

This project is part of my learning journey in Python programming, computer networking, Linux, and cybersecurity.

## Features

- **DNS Lookup** — Resolves a hostname to an IP address.
- **TCP Port Checker** — Tests whether a TCP connection can be established to a specified hostname and port.
- **System Information** — Displays the operating system, hostname, and Python version.
- **Input Validation** — Handles invalid menu choices, empty hostnames, and invalid port numbers.
- **Error Handling** — Handles DNS resolution failures, refused connections, timeouts, and other connection errors.
- **Automated Tests** — Uses Python's built-in `unittest` framework to test core functionality.
- **Continuous Integration** — GitHub Actions runs automated tests on pushes and pull requests targeting the `main` branch.

## Technologies

- Python
- Socket Programming
- Unit Testing (`unittest`)
- Git and GitHub
- GitHub Actions
- Linux / Ubuntu Server

## Requirements

- Python 3.10 or newer
- Internet connection for external DNS and TCP checks

No third-party Python packages are required.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Slavov23/PyDiag.git
cd PyDiag
```

### 2. Run the application

```bash
python main.py
```

On some Linux systems, you may need to use:

```bash
python3 main.py
```

### 3. Run the tests

```bash
python -m unittest -v
```

On Linux, if needed:

```bash
python3 -m unittest -v
```

## Usage

When the application starts, select an option from the menu:

| Option | Description |
|---|---|
| 1 | Check DNS resolution |
| 2 | Check a TCP port |
| 3 | Display system information |
| 0 | Exit the application |

For example, the TCP Port Checker can test whether a connection to `google.com` on port `443` can be established.

## Learning Objectives

This project helps me develop practical skills in:

- Python functions and exception handling
- Network programming with the `socket` module
- DNS resolution and TCP connections
- Input validation and automated testing
- Git version control and GitHub collaboration workflows
- Running and testing Python applications on Linux

## Future Improvements

- Add more network diagnostic tools.
- Improve automated test coverage.
- Add structured logging.
- Improve command-line output and reporting.
- Expand cross-platform testing.

## Author

Daniel Slavov

Developed as an educational project focused on IT diagnostics, networking, and cybersecurity fundamentals.
