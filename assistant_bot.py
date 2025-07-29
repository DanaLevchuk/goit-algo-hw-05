contacts = {}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return wrapper

@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

@input_error
def get_phone(args):
    name = args[0]
    return contacts[name]

@input_error
def show_all(args=None):
    if not contacts:
        return "No contacts found."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def exit_bot(args=None):
    return "Good bye!"

COMMANDS = {
    "add": add_contact,
    "change": change_contact,
    "phone": get_phone,
    "all": show_all,
    "exit": exit_bot,
    "close": exit_bot,
    "good bye": exit_bot
}

def parse_command(user_input):
    parts = user_input.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_command(user_input)

        handler = COMMANDS.get(command)
        if handler:
            result = handler(args)
            print(result)
            if result == "Good bye!":
                break
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
