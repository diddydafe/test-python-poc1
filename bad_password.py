# bad_password.py

# This is an example of a hardcoded password (security issue)
# Hello
username = "admin"
password = "password"  # This should be flagged by Semgrep

# This is a safer way and should NOT be flagged
import getpass
secure_password = getpass.getpass("Enter your password: ")
