
from email.message import EmailMessage
import ssl
import smtplib
import re
import tkinter as tk
from tkinter import messagebox

def send_email():
    # obtain values from entry fields
    email_sender = sender_entry.get()
    email_password = password_entry.get()
    email_receiver = receiver_entry.get()
    email_cc = cc_entry.get()
    email_bcc = bcc_entry.get()
    subject = subject_entry.get()
    body = body_entry.get("1.0",'end').strip()

    # Validate email addresses
    if not is_valid_email(email_sender):
        messagebox.showerror("Error", "Invalid sender email address")
        return
    if not is_valid_email(email_receiver):
        messagebox.showerror("Error", "Invalid receiver email address")
        return
    if email_cc and not all(is_valid_email(email.strip()) for email in email_cc.split(',')):
        messagebox.showerror("Error", "Invalid Cc email address")
        return
    if email_bcc and not all(is_valid_email(email.strip()) for email in email_bcc.split(',')):
        messagebox.showerror("Error", "Invalid Bcc email address")
        return
    
    # creates an emailMessage object
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Cc'] = email_cc
    em['subject'] = subject
    em.set_content(body)
    recipients = email_cc.split(',') + email_bcc.split(',') + [email_receiver]

    context = ssl.create_default_context()

    try:
        #connect to SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            # login to google mail
            smtp.login(email_sender, email_password)

            # send the email
            smtp.sendmail(email_sender, recipients, em.as_string())
        messagebox.showinfo("Success", f'email sent successfully!')
        clear_window()
    except Exception as e:
        messagebox.showerror("Error",f'an error has occured: {e}')

# Regular expression pattern for validating email addresses
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# function to clear fields after successfully sending mail
def clear_window():
    receiver_entry.delete(0, 'end')
    subject_entry.delete(0, 'end')
    cc_entry.delete(0, 'end')
    bcc_entry.delete(0, 'end')
    body_entry.delete("1.0", 'end')


# Create the main application window
root = tk.Tk()
root.title("Email Sender")

# Create entry fields and labels
sender_label = tk.Label(root, text="User Email:")
sender_label.grid(row=0, column=0)
sender_entry = tk.Entry(root)
sender_entry.grid(row=0, column=1)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(root, show='*')
password_entry.grid(row=1, column=1)

receiver_label = tk.Label(root, text="To:")
receiver_label.grid(row=2, column=0)
receiver_entry = tk.Entry(root)
receiver_entry.grid(row=2, column=1)

cc_label = tk.Label(root, text="Cc:")
cc_label.grid(row=3, column=0)
cc_entry = tk.Entry(root)
cc_entry.grid(row=3, column=1)

bcc_label = tk.Label(root, text="Bcc:")
bcc_label.grid(row=4, column=0)
bcc_entry = tk.Entry(root)
bcc_entry.grid(row=4, column=1)

subject_label = tk.Label(root, text="Subject:")
subject_label.grid(row=5, column=0)
subject_entry = tk.Entry(root)
subject_entry.grid(row=5, column=1)

body_label = tk.Label(root, text="Body:")
body_label.grid(row=6, column=0)
body_entry = tk.Text(root, wrap="word", height=10)
body_entry.grid(row=6, column=1, sticky="nsew")

# allows row to expand vertically with more text
root.grid_rowconfigure(6, weight=1)

send_button = tk.Button(root, text="Send", command=send_email)
send_button.grid(row=7, columnspan=2)


# Tkinter event loop to open window
root.mainloop()

