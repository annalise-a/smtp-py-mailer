# smtp-py-mailer

smtp-py-mailer is a Python application that allows users to send emails securely using the SMTP protocol through Google's servers. It provides a graphical user interface (GUI) built with Tkinter for ease of use.

## Features

- Securely sends emails using SMTP protocol.
- Validates sender, receiver, Cc, and Bcc email addresses.
- Encrypts communication with SMTP server using SSL/TLS.
- User-friendly GUI for entering email details such as sender, receiver, subject, body, etc.

## Prerequisites

- Python 3.x
- tkinter library (included in standard Python distribution)
- `smtplib` library (included in standard Python distribution)
- `ssl` library (included in standard Python distribution)
- a Gmail account with App Passwords enabled

## Installation

No installation is required. Simply download or clone the repository to your local machine.

## Usage

1. Run the script `main.py`.
2. Fill in the required fields: User Email, Password, To, Cc, Bcc, Subject, and Body.
3. Click the "Send" button to send the email.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
