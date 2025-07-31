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
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    raise KeyError

@input_error
def get_phone(args, contacts):
    name = args[0]
    return contacts[name]

def show_all(_, contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def parser(text: str):
    parts = text.strip().split()
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args

def main():
    contacts = {}

    COMMANDS = {
        "add": add_contact,
        "change": change_contact,
        "phone": get_phone,
        "all": show_all,
    }

    while True:
        user_input = input("Enter a command: ")
        if user_input.lower() in ["exit", "close", "good bye"]:
            print("Good bye!")
            break

        cmd, args = parser(user_input)
        handler = COMMANDS.get(cmd)

        if handler:
            print(handler(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
