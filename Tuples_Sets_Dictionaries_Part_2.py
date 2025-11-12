# Module: Tuples, Sets, Dictionaries
# Part 2

#----------------TASK_1---------------#

# Create an app that stores information about great basketball players.
# Store the player's full name and height. 
# Provide the possibility to add, delete, search, and replace data. Use a dictionary to store information.



players = {}

def add_player():
    name = input("Enter full name of the player: ")
    height = input("Enter player's height (cm): ")
    players[name] = height
    print(f"{name} was added.")


def delete_player():
    name = input("Enter full name of the player: ")
    if name in players:
        del players[name]
        print(name, "was deleted.")
    else:
        print("Player not found.")


def search_player():
    name = input("Enter full name of the player: ")
    if name in players:
        print({name : players[name]})
    else:
        print("Not found")

def replace_player():
    name =  input("Enter full name of the player: ")
    if name in players:
        players[name] = input("Enter new height: ")
    else:
        print("Not found")

def show_players():
    print(players)

while True:
    print("1 - Add player")
    print("2 - Delete player")
    print("3 - Search player")
    print("4 - Replace player height")
    print("5 - Show all players")

    choose = input("Choose: ")

    if choose == "1":
        add_player()
    elif choose == "2":
        delete_player()
    elif choose == "3":
        search_player()
    elif choose == "4":
        replace_player()
    elif choose == "5":
        show_players()
        break
    else:
        print("Invalid choice")


#----------------TASK_2---------------#

# Create an app English-French Dictionary. 
# Store a word in English and its French translation. 
# Provide the possibility to add, delete, search, and replace data. 
# Use a dictionary to store information.

dicrionary ={}

def add_word():
    word =  input("Enter English word: ")
    translation = input("Enter French translation: ")
    dicrionary[word] = translation
    print("Word added")

def delete_word():
    word = input("Delete word")
    if word in dicrionary:
        del dicrionary[word]
    else:
        print("Word not found")

def search_word():
    word = input("Search word: ")
    if word in dicrionary:
        print(word)
    else:
        print("There are no such word in dictionary")

def replace_word():
    word = input("Enter word to replace: ")
    if word in dicrionary:
        dicrionary[word] = input("Enter new word: ")
    else:
        print("Invalid")

def show_words():
    print(dicrionary)


while True:
    print("1. Add word")
    print("2. Delete word")
    print("3. Search word")
    print("4. Replace word")
    print("5. Show words")

    option = input("Select: ")

    if option == "1":
        add_word()
    elif option == "2":
        delete_word()
    elif option == "3":
        search_word()
    elif option == "4":
        replace_word()
    elif option == "5":
        show_words()
        break
    else:
        print("Invalid option")


#----------------TASK_3---------------#

# Create an app Company. 
# Store the following information about a person: 
# full name, phone number, corporate email, job title, room number, skype. 
# Provide the possibility to add, delete, search, and replace data. 
# Use a dictionary to store information.

company = {}

def add_employee():
    name = input("Enter full name: ")
    phone = input("Enter phone number: ")
    email = input("Enter corporate email: ")
    title = input("Enter job title: ")
    room_number = input("Enter room number: ")
    skype = input("Enter skype: ")
    company[name] = {
        "phone": phone,
        "email": email,
        "title": title,
        "room": room_number,
        "skype": skype
    }
    print("Employee added successfully")

def delete_employee():
    name = input("Enter full name: ")
    if name in company:
        del company[name]
        print("Employee deleted successfully")
    else:
        print("Employee not found")

def search_employee():
    name = input("Enter full name: ")
    if name in company:
        print(company[name])
    else:
        print("invalid")

def replace_employee():
    name = input("Enter full name: ")
    if name in company:
        print("What do you want to replace?")
        phone = input("Enter new phone")
        email = input("Enter the new email: ")
        title = input("Enter the new job title: ")
        room_number = input("Enter the new room number: ")
        skype = input("Enter the new skype: ")

        company[name] = {
        "phone": phone,
        "email": email,
        "title": title,
        "room": room_number,
        "skype": skype
    }
        
def show_all():
    print(company)



while True:
    print("1. Add employee")
    print("2. Delete employee")
    print("3. Search employee")
    print("4. Replace employee")
    print("5. Show all employees")

    select = input("Select an option: ")
    if select == "1":
        add_employee()
    elif select == "2":
        delete_employee()
    elif select == "3":
        search_employee()
    elif select == "4":
        replace_employee()
    elif select == "5":
        show_all()
        break
    else:
        print("Invalid")


#----------------TASK_4---------------#

# Create an app Book Collection. 
# Store the following information about books: 
# author, title, genre, year of release, publisher. 
# Provide the possibility to add, delete, search, and replace data. 
# Use a dictionary to store information.

book = {}

def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    genre = input("Enter the genre of the book: ")
    year = input("Enter the year of release: ")
    publisher = input("Enter the publisher of the book: ")
    book[title] = {
        "title": title,
        "author": author,
        "genre": genre,
        "year": year,
        "publisher": publisher
        }
    print("Book added successfully")

def delete_book():
    title = input("Enter the title of the book to delete: ")
    if title in book:
        del book[title]
        print("Book deleted successfully")
    else:
        print("Book not found")

def search_book():
    title = input("Enter the title of the book to search: ")
    if title in book:
        print(book[title])
    else:
        print("Book not found")

def replace_book():
    title = input("Add title of book: ")
    if title in book:
        print("What do you want to replace?")
        print("1. Author")
        print("2. Genre")
        print("3. Year")
        print("4. Publisher")
        choice = input("Enter your choice: ")
        if choice == "1":
            book[title]["author"] = input("Enter new author: ")
        elif choice == "2":
            book[title]["genre"] = input("Enter new genre: ")
        elif choice == "3":
            book[title]["year"] = input("Enter new year: ")
        elif choice == "4":
            book[title]["publisher"] = input("Enter new publisher: ")
        else:
            print("Invalid choice")



while True:
    print("1. Add book")
    print("2. Delete book")
    print("3. Search book")
    print("4. Replace book")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        delete_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        replace_book()
    elif choice == "5":
        break
    else:
        print("Invalid choice")