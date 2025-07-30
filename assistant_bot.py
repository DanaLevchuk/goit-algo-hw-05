def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command"
    return wrapper

def main():
    contacts = {}

    @input_error
    def add_contact(args):
        name, phone = args
        contacts[name] = phone
        return "Contact added."

    @input_error
    def change_contact(args):
        name, phone = args
        contacts[name] = phone
        return "Contact updated."

    @input_error
    def show_phone(args):
        name = args[0]
        return contacts[name]

    @input_error
    def show_all():
        if not contacts:
            return "No contacts found."
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()

    def exit_bot():
        return "Good bye!"

    COMMANDS = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
        "exit": exit_bot,
        "close": exit_bot,
        "good bye": exit_bot
    }

    def parse_command(user_input):
        parts = user_input.strip().split()
        if not parts:
            raise IndexError
        command = parts[0].lower()
        args = parts[1:]
        return command, args

    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, args = parse_command(user_input)
            handler = COMMANDS.get(command)
            if handler:
                result = handler(args) if args else handler()
                print(result)
                if result == "Good bye!":
                    break
            else:
                print("Unknown command. Try again.")
        except IndexError:
            print("Enter the argument for the command")

if __name__ == "__main__":
    main()
