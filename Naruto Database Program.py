import sqlite3
from unicodedata import name

con = sqlite3.connect('characters.db')

cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS characters (
    name TEXT,
    age INTEGER,
    rank INTEGER
)""")


def main():
    while True:
        print("Welcome to the program!")

        display_all_characters()

        choice = int(input("What would you like to do with the program? \n\
        Add a character(1)\n\
        Remove a character(2)\n\
        Display Certain Characters(3)\n\
        Update a Character(4)\n\
        \n\
        "))

        if choice == 1:
            add_new_character()
        elif choice == 2:
            remove_character()
        elif choice == 3:
            display_certain_characters()
        elif choice == 4:
            update_character() 
        
        keep_going = int(input("Do you want to continue? Continue (1) Stop(0): "))
        if keep_going == 0: 
            break
        
def add_new_character():
    
    # Getting the attributes of the new character 
    name = input("What is the name of the character?: ")
    age = int(input("What is the characters age?: "))
    rank = int(input("What is the rank of the character?: "))

    # Commiting the character attributes into the characters table
    cur.execute("INSERT INTO characters VALUES (?, ?, ?)", (name, age, rank))
    print("Character successfully added")

def remove_character():
    character_name = input("What character would you like to remove?: ")
    if cur.execute("DELETE from characters WHERE name = (?)", (character_name,)):
        print("Character successfully deleted!")
    else: 
        print("Invalid character name")

def display_all_characters():

        cur.execute("SELECT rowid, * FROM characters")
        characters = cur.fetchall()
        print("")
        print("ID#" + "\t" + "NAME" + "\t" + "AGE" + "\t" + "RANK")
        print("-----" + "\t" + "-----" + "\t" + "-----" + "\t" + "-----")
        for character in characters:
            print(str(character[0]) + "\t" + character[1] + "\t" + str(character[2]) + "\t" + str(character[3]))

def display_certain_characters():
    sort_type = int(input("What do you want to sort by? Age(1), Rank(2): "))

    #Sorting by the age
    if sort_type == 1:
        age_choice = int(input("What age would you like to choose?: "))
        cur.execute("SELECT rowid, * FROM characters WHERE age >= (?)", (age_choice,))
        characters = cur.fetchall()
        print("-----" + "\t" + "-----" + "\t" + "-----" + "\t" + "-----")
        
        for character in characters:
            print(str(character[0]) + "\t" + character[1] + "\t" + str(character[2]) + "\t" + str(character[3]))

    #Sorting by the rank
    elif sort_type == 2:
        rank_choice = int(input("What rank would you like to choose?: "))
        cur.execute("SELECT rowid, * FROM characters WHERE rank >= (?)", (rank_choice,))
        characters = cur.fetchall()
        print("-----" + "\t" + "-----" + "\t" + "-----" + "\t" + "-----")

        for character in characters:
            print(str(character[0]) + "\t" + character[1] + "\t" + str(character[2]) + "\t" + str(character[3]))

def update_character():
    # Choose which character to deal with give the ID #
    character_ID = input("What character are we updating? (ID#): ")
    update_choice = int(input("What would you like to update? Name(1), Age(2), Rank(3): "))

    # changing the attributes of the characters either by name, age, or rank

    # Name
    if update_choice == 1:
        new_name = input("What is the new name?: ")
        cur.execute("UPDATE characters SET name = (?) WHERE rowid = (?)", (new_name, character_ID))

    # Age
    elif update_choice == 2:
        new_age = input("What is the new age?: ")
        cur.execute("UPDATE characters SET name = (?) WHERE rowid = (?)", (new_age, character_ID))

    # Rank
    elif update_choice == 3:
        new_rank = input("What is the new rank?: ")
        cur.execute("UPDATE characters SET rank = (?) WHERE rowid = (?)", (new_rank, character_ID))
    
    else:
        print("Invalid choice. Please try again.")

    print("Character Successfully Updated!")

if __name__ == "__main__":
    main()

con.commit()
con.close()