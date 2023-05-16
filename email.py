# An Email Simulation


class Email():
    # The Class that will be the blueprint for email objects in our simulation. 
    def __init__(self, email_contents, from_address = "joe@noemail.com", 
                has_been_read = False, is_spam = False):
        self.email_contents = email_contents
        self.from_address = from_address
        self.has_been_read = has_been_read
        self.is_spam = is_spam
    
    def mark_as_read(self):
        self.has_been_read = True
    
    def mark_as_spam(self):
        self.is_spam = True


def add_email():
    """ Function receives input from user with email contents and address,
    makes a new object with this input and adds it to the 'inbox' list.
    Parameters: None
    Returns: None """
    
    email_contents = input("Enter contents from the received email: ")
    from_address = input("From what email address was it sent? ")
    
    new_email = Email(email_contents, from_address)
    inbox.append(new_email)
    
    print(f"\n{GREEN}Success{ENDC}.",
            f"Email \'{email_contents}\' from {from_address} was added.")


def get_count():
    """ Function returns the number of emails in the 'inbox' list.
    Parameters: None
    Returns: length of inbox (int) """
    
    return len(inbox)


def get_email(ind):
    """Function returns the contents of the email stored at position 'ind' in 
    the list 'inbox', as well as marking the email as read.
    Parameters: the index (int)
    Returns: the email contents (str) """
    
    inbox[ind].mark_as_read()
    return inbox[ind].email_contents


def get_unread_emails():
    """Function returns a list of all the emails that haven't been read.
    Parameters: None
    Returns: unread emails (list) """
    
    unread_emails = []
    for email in inbox:
        if email.has_been_read == False:
            unread_emails.append(email)
    return unread_emails


def get_spam_emails():
    """Function returns a list of all the emails that have been marked as spam.
    Parameters: None
    Returns: spam emails (list) """
    
    spam_emails = []
    for email in inbox:
        if email.is_spam == True:
            spam_emails.append(email)
    return spam_emails


def delete():
    """Function removes an item from the 'inbox' list.
    Parameters: None
    Returns: None """
    
    show_all_inbox()
    while True:
        try:
            index = int(input("Enter the email index you want to delete: "))
            if index not in range(len(inbox)):
                raise Exception(f"{RED}'{index}' is not a valid index.{ENDC}")
            break
        except ValueError:
            print(f"\n{RED}You need to enter a number.{ENDC}")
        except Exception as error:
            print(f"\n{RED}{error}{ENDC} Let's try again.")
        # The try except block makes sure user enters a valid index number.
    
    inbox.pop(index)
    print(f"{GREEN}\nSuccess{ENDC}. Email #{index} was {RED}deleted{ENDC}.")


def show_all_inbox():
    """Function prints out a preview of all email contents in 'inbox' list.
    Parameters: None
    Returns: None """
    
    print(f"{PINK}")
    print("Inbox preview:")
    for index, email in enumerate(inbox):
        print(f"\t{index}: {email.email_contents[:15]}...")
    print(f"{ENDC}")


def show_inbox_without_spam():
    """Function prints a preview of emails from 'inbox' list that aren't spam.
    Parameters: None
    Returns: None """
    
    print(f"{BLUE}\nInbox preview {ENDC}(spam-free){BLUE}:")
    for index, email in enumerate(inbox):
        if email.is_spam == False:
            print(f"\t{index}: {email.email_contents[:15]}...")
    print(f"{ENDC}")


RED = '\033[31m'
GREEN = '\033[92m'
PINK = '\033[95m'
CYAN = '\033[96m'
BLUE = '\033[94m'
ENDC = '\033[0m'


email_1 = Email("Hi from the Netherlands. We're having a great time.")
email_2 = Email("The weather is bad tomorrow, should we cancel?")
email_3 = Email("I'm under the weather, can't make it to our meeting.")
email_4 = Email("Delivery address was changed, please advise.")
email_5 = Email("No news on his whereabouts, will keep you posted.")

inbox = [email_1, email_2, email_3, email_4, email_5]

while True:
    print(f"{'─'*60}")
    user_choice = input(f"""What would you like to do? Here are your options: 
    {CYAN}1. Preview emails:
        a. show the inbox
        b. show inbox without spam emails
        c. show unread emails
        d. show spam emails
    2. Display email contents
    3. Mark an email as spam
    4. Delete an email
    5. Add email
    6. Quit\n{ENDC}{'─'*60}
    Your choice (1-6): """).lower().strip('.')
    
    if user_choice == '1':
        # Lets user preview emails and choose from the 4 options.
        
        preview = input(f"""\n{GREEN}Previewing emails...{ENDC}
        a. show the inbox
        b. show inbox without spam emails
        c. show unread emails
        d. show spam emails
        \b\bEnter what to preview (a-d): """).lower().strip('.')
        
        if preview == "a":
            print(f"{'─'*60}\nInbox has {PINK}{get_count()}{ENDC} emails.")
            show_all_inbox()
        
        elif preview == "b":
            show_inbox_without_spam()
        
        elif preview == "c":
            all_unread_emails = get_unread_emails()
            if len(all_unread_emails) == 0:
                print(f"{GREEN}\nYou have no unread emails.{ENDC}")
            else:
                print(f"\n{PINK}Unread emails:")
                for index, email in enumerate(all_unread_emails):
                    print(f"\t{index}: {email.email_contents[:15]}...")
            print(f"{ENDC}")
        
        elif preview == "d":
            all_spam = get_spam_emails()
            if len(all_spam) == 0:
                print(f"{GREEN}\nYou have no spam.{ENDC}")
            else:
                print(f"\n{RED}Spam:")
                for index, email in enumerate(all_spam):
                    print(f"\t{index}: {email.email_contents[:15]}...")
                print(f"{ENDC}")
        
        else:
            print(f"{RED}\nSorry, not a valid option.{ENDC}")
    
    elif user_choice == "2":
        # Lets user choose an index and display email contents from that index.
        
        show_all_inbox()
        while True:
            try:
                index = int(input("Enter the email index you want to view: "))
                if index not in range(len(inbox)):
                    raise Exception(f"'{index}' is not a valid index.")
                break
            except ValueError:
                print(f"\n{RED}You need to enter a number.{ENDC}")
            except Exception as error:
                print(f"\n{RED}{error}{ENDC} Let's try again.")
            # The try except block makes sure user enters a valid index number.
        
        print(f"\n{GREEN}Opening email #{index}... \n{'─'*70}{ENDC}", 
                f"\n\'{get_email(index)}\' \n{GREEN}{'─'*70}{ENDC}")
    
    elif user_choice == "3":
        show_all_inbox()
        while True:
            # Lets user enter an index and mark that email as spam.
            try:
                index = int(input(f"Enter the email index to mark as spam: "))
                if index not in range(len(inbox)):
                    raise Exception(f"'{index}' is not a valid index.")
                break
            except ValueError:
                print(f"\n{RED}You need to enter a number.{ENDC}")
            except Exception as error:
                print(f"\n{RED}{error}{ENDC} Let's try again.")
            # The try except block makes sure user enters a valid index number.
        inbox[index].mark_as_spam()
        print(f"\nEmail #{index} was {BLUE}marked as spam{ENDC}.")
    
    elif user_choice == "4":
        # Lets the user remove an email from the inbox list.
        delete()
    
    elif user_choice == "5":
        # Lets the user enter contents and email address of a received email.
        add_email()
    
    elif user_choice == "6":
        print("Goodbye!")
        break
    
    else:
        print(f"{RED}\nOops - incorrect input.{ENDC} Let's try again.")