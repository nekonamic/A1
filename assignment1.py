"""
Update this module docstring with your own details
Name:Roswaal Mathers
Date started:10/25/2021
"""
import csv


def count_requirement():
    with open("albums.csv", "r") as albums:
        reader = csv.reader(albums)
        requirement = 0
        for row in reader:
            if row[3] == "r":
                requirement += 1
    return requirement


def input_int_positive_number(data_name):
    while True:
        number = input(data_name)
        if not number.isnumeric():
            print("Enter a number")
            continue
        elif number.count('.') == 1:
            print("Enter an integrate number")
        elif number.count(".") == 0:
            if number.isdigit():
                if int(number) > 0:
                    return int(number)
                else:
                    print("Enter a positive number")
                    continue
        else:
            print("Valid input")
            continue


def list_albums(choice):
    with open("albums.csv", "r") as albums:
        reader = csv.reader(albums)
        requirement = 0
        for index, row in enumerate(reader):
            if row[3] == "r":
                print("*{}. {:<30s}by {:<15}({})".format(index + 1, row[0], row[1], row[2]))
            else:
                print(" {}. {:<30s}by {:<15}({})".format(index + 1, row[0], row[1], row[2]))
            if row[3] == "r":
                requirement += 1
        if count_requirement() == 0:
            if choice == "l":
                print("No albums left to listen to. Why not add a new album?")
            else:
                print("No required albums")
                return True
        else:
            print(f"You need to listen to {requirement} albums.")


def main():
    print("Album Tracker 1.0 - by Roswaal Mathers")
    with open("albums.csv", "r") as albums:
        print(len(albums.readlines()), "albums loaded")
    choice = ""
    while choice != "Q" and choice != "q":
        print("Menu:\nL - List all albums\nA - Add new album\nM - Mark an album as completed\nQ - Quit")
        choice = input(">>> ")
        if choice == "L" or choice == "l":
            list_albums("l")
        elif choice == "A" or choice == "a":
            title = input("Title: ")
            while title.isspace():
                print("can not be blank")
                title = input("Title: ")
            artist = input("Artist: ")
            while artist.isspace():
                print("can not be blank")
                artist = input("Artist: ")
            years = input_int_positive_number("years: ")
            add_row = [title, artist, years, "r"]
            with open("albums.csv", "a", newline="") as albums:
                writer = csv.writer(albums)
                writer.writerow(add_row)
            print("{} by {} ({}) added to Album Tracker".format(title, artist, years))
        elif choice == "M" or choice == "m":
            if list_albums("m"):
                continue
            print("Enter the number of an album to mark as completed")
            completed_album = input_int_positive_number(">>> ")
            with open("albums.csv", "r") as albums:
                reader = csv.reader(albums)
                li = list(reader)
            li[completed_album - 1][3] = "c"
            with open("albums.csv", "w", newline="") as albums:
                writer = csv.writer(albums)
                writer.writerows(li)
            print("You have already listened to {}".format(li[completed_album - 1][0]))
        elif choice == "Q" or choice == "q":
            with open("albums.csv", "r") as albums:
                print(len(albums.readlines()), " albums saved to albums.csv")
        else:
            print("Invalid menu choice")


main()
