def display_notes(notes):
    if not notes:
        print("***No notes found.***")
    else:
        print("Your notes:")
        for index, notes in enumerate(notes, 1):
            print(f"{index}. {notes['title']} - {notes['description']}")


def add_notes(notes):
    title = input("Enter notes title: ")
    description = input("Enter notes description: ")
    new_notes = {'title': title, 'description': description}
    notes.append(new_notes)
    print("**Notes added successfully.**")


def delete_notes(notes):
    display_notes(notes)
    try:
        index = int(input("Enter the number of the notes you want to delete: ")) - 1
        deleted_notes = notes.pop(index)
        print(f"Notes '{deleted_notes['title']}' deleted successfully.")
    except (IndexError, ValueError):
        print("***Invalid input. Please enter a valid note number.***")


def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Display notes")
    print("2. Add a new note")
    print("3. Delete a notes")
    print("0. Exit")


def main():
    notes = []
    while True:
        show_menu()
        choice = input("Enter your choice (0-3): ")
        if choice == '0':
            break
        elif choice == '1':
            display_notes(notes)
        elif choice == '2':
            add_notes(notes)
        elif choice == '3':
            delete_notes(notes)
        else:
            print("Invalid choice. Please enter a number between 0 and 3.")

if __name__ == "__main__":
    main()
