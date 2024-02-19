# This programme is an email inbox, designed to store and manage emails. Including the 
# abilities to 'read an email', 'Compose an email', 'view unread emails', 'mark emails as read', 'mark as spam',
# 'view spam folder' and 'delete email'. 

# Create and initialise class taking the three arguments of 'email address', 'subject line'
# and 'email content'.
class Email:
    has_been_read = False  # Default to False.
    is_spam = False  # Default to False.

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Function to mark the email as 'read'.
    def mark_as_read(self):
        if not self.has_been_read:
            self.has_been_read = True

    # Function to mark the email as 'spam'.
    def mark_as_spam(self):
        if not self.is_spam:
            self.is_spam = True

# Function to create and return emails.
def populate_inbox():
    email1 = Email("hello1@world.com", "How are you?", "I thought I'd check in on you.")
    email2 = Email("donutsRus@gmail.com", "We've got your order!", "Thank you for your business!")
    email3 = Email("snowdays@yahoo.com", "Discounts on flights!", "Winter sale on flights now on!")
    return [email1, email2, email3]

# Function to list and print emails and if they are 'read' or 'spam'.
def list_emails(inbox):
    print("\nEmails:")
    for idx, email in enumerate(inbox):
        status = ' (Read)' if email.has_been_read else ''
        spam_status = ' (Spam)' if email.is_spam else ''
        print(f"{idx + 1}. Subject: {email.subject_line}{status}{spam_status}")
    print()

# Function to mark email as 'read'.
def mark_email_as_read(inbox, email_index):
    if 0 <= email_index < len(inbox):
        inbox[email_index].mark_as_read()
        print(f"\nMarked email {email_index + 1} as read.\n")
    else:
        print("Invalid email number.")  # Error handling.

# Function to mark email as "spam'."
def mark_email_as_spam(inbox, email_index):
    if 0 <= email_index < len(inbox):
        inbox[email_index].mark_as_spam()
        print(f"\nMarked email {email_index + 1} as spam.\n")
    else:
        print("Invalid email number.")  # Error handling.

# Function to view unread emails.
def view_unread_emails(inbox):
    unread_emails = [email for email in inbox if not email.has_been_read]
    if not unread_emails:
        print("\nNo unread emails.\n")
    else:
        print("\nUnread Emails:")
        for email in unread_emails:
            print(f"{inbox.index(email) + 1}. Subject: {email.subject_line}")
        print()

# Function to view spam folder.
def view_spam_folder(inbox):
    spam_emails = [email for email in inbox if email.is_spam]
    if not spam_emails:
        print("\nNo spam emails.\n")
    else:
        print("\nSpam Emails:")
        for email in spam_emails:
            print(f"{inbox.index(email) + 1}. Subject: {email.subject_line}")
        print()

# Function to read email and mark as 'read'.
def read_email(inbox, email_index):
    if 0 <= email_index < len(inbox):
        email = inbox[email_index]
        print(f"\nEmail Address: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")
        email.mark_as_read()
        print("\n")
    else:
        print("Invalid email number.")  # Error handling.

# Function the create email and add to inbox.
def create_email():
    email_address = input("Enter recipient's email address: ")
    subject_line = input("Enter email subject: ")
    email_content = input("Enter email content: ")

    new_email = Email(email_address, subject_line, email_content)
    inbox.append(new_email)
    print("Email created and added to the inbox.\n")

# Function to delete email.
def delete_email(inbox, email_index):
    if 0 <= email_index < len(inbox):
        deleted_email = inbox.pop(email_index)
        print(f"Deleted email with subject: {deleted_email.subject_line}\n")
    else:
        print("Invalid email number. No email deleted.\n")



# Print 'Welcome' message and present menu choices.
print("Welcome to your inbox! Please choose a following option below:")

inbox = populate_inbox()

while True:
    print("1. Read an email")
    print("2. View unread emails")
    print("3. Mark an email as spam")
    print("4. View spam folder")
    print("5. Compose email & send to Inbox")
    print("6. Delete email")
    print("7. Quit application")

    choice = input("Enter the number of the option (1, 2, 3, 4, 5, 6 or 7): ")

    if choice == '1':
        list_emails(inbox)
        email_index = int(input("Enter the number of the email to read: ")) - 1
        read_email(inbox, email_index)
    elif choice == '2':
        view_unread_emails(inbox)
    elif choice == '3':
        list_emails(inbox)
        email_index = int(input("Enter the number of the email to mark as spam: ")) - 1
        mark_email_as_spam(inbox, email_index)
    elif choice == '4':
        view_spam_folder(inbox)
    elif choice == '5':
        create_email()
    elif choice == '6':
        list_emails(inbox)
        email_index = int(input("Enter the number of the email to delete: ")) - 1
        delete_email(inbox, email_index)
    elif choice == '7':
        print("Goodbye!\n")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6 or 7.\n")  # Error handling.
