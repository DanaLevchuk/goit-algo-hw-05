contacts = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name"
    return inner

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
    raise KeyError

@input_error
def get_phone(args):
    name = args[0]
    return contacts[name]

def show_all(_=None):
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result) if result else "No contacts found."

COMMANDS = {
    "add": add_contact,
    "change": change_contact,
    "phone": get_phone,
    "all": show_all,
}

def parser(text: str):
    parts = text.strip().split()
    cmd = parts[0].lower()
    args = parts[1:]
    return COMMANDS.get(cmd), args

def main():
    while True:
        user_input = input("Enter a command: ")
        if user_input.lower() in ["exit", "close", "good bye"]:
            print("Good bye!")
            break
        command, args = parser(user_input)
        if command:
            print(command(args))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
