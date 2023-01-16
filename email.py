#An Email Simulation
# CLASSES =======================
class Email:
    # Constructor method with instance variables name and age
    def __init__(self, email_contents, from_address):
        self.has_been_read = False
        self.email_contents = email_contents
        self.is_spam = False
        self.from_address = from_address

    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True

# FUNCTIONS =======================
# create empty list to hold emails
inbox = []

# function to add a new email object to the inbox list
def add_email(contents, address):
    inbox.append(Email(contents, address))

# function to return the number of emails in inbox
def get_count():
    return len(inbox)

# function that returns the contents of the passed index
def get_email(index):
    inbox[index].mark_as_read()
    return inbox[index].email_contents

def get_unread_emails():
    unread = []
    for email in inbox:
        if email.has_been_read == False:
            unread.append(email)
    return unread

def get_spam_emails():
    spam = []
    for email in inbox:
        if email.is_spam == True:
            spam.append(email)
    return spam

def delete(choice):
    inbox.pop(choice)

# function to display all emails - reuse
def print_display():
    print("\nNo.\tFrom\t\t\tRead\tSpam")
    for pos, email in enumerate(inbox, 1):
        print(f"{pos}\t{email.from_address}\t{email.has_been_read}\t{email.is_spam}")

# function to get user choice - reuse
def get_choice(action, list, unread):
    # try / catch to ensure a number is entered
    try:
        choice = int(input(f"\nYou currently have {len(list)}{unread} emails.\nWhich one would you like to {action} (1-{len(list)})?\t"))
    except ValueError:
        choice = 0;
    return choice



# PROGRAM START =======================
# create some sample email content and addresses
content_1 = "Hi there, welcome to NewsWeek. Your first edition will be available next week. Regards, Kevin Coldwater"
content_2 = "Thank you for your purchase. It will be dispatched within the next 24 hours. Thanks, John Menzies"
content_3 = "New Year Offer. Join Activate Gym and get your first 3 months free!"
address_1 = "kevin@newsweek.com"
address_2 = "john@menzies.com"
address_3 = "offer@activate.com"

# create email objects and add to inbox
add_email(content_1, address_1)
add_email(content_2, address_2)
add_email(content_3, address_3)

#Introduction
print('\nWelcome to Email!')
print('=============================\n')
user_choice = ""
while user_choice != "e":
    user_choice = input('''Select one of the following options below:

r - Read Email
s - Send Email
d - Delete Email
m - Mark Email as Spam
u - See unread emails
p - See spam emails
e - Exit Email
: ''').lower()
    if user_choice == "r":
        if len(inbox):
            # loop through inbox and show emails
            print_display()

            # get user choice
            choice = get_choice("read", inbox, "")

            # process input and print email
            if choice >= 1 and choice <= get_count():
                print("\n" + get_email(choice-1) + "\n")
            else:
                print("\nThat email wasn't found...\n")
        else:
            print("\nInbox empty...\n")

    elif user_choice == "s":
        sender = input("\nWho is the email from:\t")
        content = input("What is the message:\t")
        add_email(content, sender)
        print("\nSuccessfully sent email...\n")

    elif user_choice == "d":
        if len(inbox):
            # loop through inbox and show emails
            print_display()

            # get user choice
            choice = get_choice("delete", inbox, "")

            # process input and mark as spam
            if choice >= 1 and choice <= get_count():
                delete(choice-1)
                print("\nSuccessfully deleted email...\n")
            else:
                print("\nThat email wasn't found...\n")
        else:
            print("\nInbox empty...\n")

    elif user_choice == "m":
        if len(inbox):
            # loop through inbox and show emails
            print_display()

            # get user choice
            choice = get_choice("mark as spam", inbox, "")

            # process input and mark as spam
            if choice >= 1 and choice <= get_count():
                inbox[choice-1].mark_as_spam()
                print("\nSuccessfully marked as spam...\n")
            else:
                print("\nThat email wasn't found...\n")
        else:
            print("\nInbox empty...\n")

    elif user_choice == "u":
        if len(get_unread_emails()):
            # loop through inbox and show emails
            print("\nNo.\tFrom\t\t\tRead\tSpam")
            for pos, email in enumerate(get_unread_emails(), 1):
                print(f"{pos}\t{email.from_address}\t{email.has_been_read}\t{email.is_spam}")
            print()
        else:
            print("\nNo unread emails...\n")

    elif user_choice == "p":
        if len(get_spam_emails()):
            # loop through inbox and show emails
            print("\nNo.\tFrom\t\t\tRead\tSpam")
            for pos, email in enumerate(get_spam_emails(), 1):
                print(f"{pos}\t{email.from_address}\t{email.has_been_read}\t{email.is_spam}")
            print()
        else:
            print("\nNo spam emails...\n")

    elif user_choice == "e":
        print("\nGoodbye\n")
    else:
        print("\nOops - incorrect input\n")
