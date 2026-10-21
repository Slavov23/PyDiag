
import unittest
from unittest.mock import patch
import socket
from main import get_system_info, check_dns, check_tcp_port, ping_check

from main import get_system_info, check_dns, check_tcp_port


class TestPyDiag(unittest.TestCase):

    def test_system_info(self):
        info = get_system_info()

        self.assertIn("system", info)
        self.assertIn("hostname", info)
        self.assertIn("python_version", info)

    @patch("main.socket.gethostbyname", return_value="142.250.74.14")
    @patch("builtins.input", return_value="google.com")
    def test_dns_success(self, mock_input, mock_dns):
        with patch("builtins.print") as mock_print:
            check_dns()

        mock_print.assert_called_once_with(
            "[Success] google.com resolved to 142.250.74.14"
        )

    @patch("main.socket.gethostbyname", side_effect=socket.gaierror)
    @patch("builtins.input", return_value="invalid.invalid")
    def test_dns_failure(self, mock_input, mock_dns):
        with patch("builtins.print") as mock_print:
            check_dns()

        mock_print.assert_called_once_with(
            "[Error] Could not resolve hostname: invalid.invalid"
        )

    @patch("builtins.input", side_effect=["google.com", "443"])
    @patch("main.socket.create_connection")
    def test_tcp_port_open(self, mock_connection, mock_input):
        with patch("builtins.print") as mock_print:
            check_tcp_port()

        mock_connection.assert_called_once_with(
            ("google.com", 443), timeout=3
        )
        mock_print.assert_called_once_with(
            "[Success] Port 443 is OPEN on google.com"
        )

    @patch("builtins.input", side_effect=["google.com", "70000"])
    def test_invalid_port(self, mock_input):
        with patch("builtins.print") as mock_print:
            check_tcp_port()

        mock_print.assert_called_once_with(
            "[Error] Port must be between 1 and 65535"
        )

    @patch("main.subprocess.run")
    @patch("builtins.input", return_value="127.0.0.1")
    def test_ping_success(self, mock_input, mock_run):
        mock_run.return_value.returncode = 0

        with patch("builtins.print") as mock_print:
            ping_check()

        mock_run.assert_called_once()
        mock_print.assert_called_once_with(
            "[Success] Host 127.0.0.1 is reachable"
        )

    @patch("main.subprocess.run")
    @patch("builtins.input", return_value="192.0.2.1")
    def test_ping_failure(self, mock_input, mock_run):
        mock_run.return_value.returncode = 1

        with patch("builtins.print") as mock_print:
            ping_check()

        mock_run.assert_called_once()
        mock_print.assert_called_once_with(
            "[Info] Host 192.0.2.1 did not respond to ping"
        )



if __name__ == "__main__":
    unittest.main()
