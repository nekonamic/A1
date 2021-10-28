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
            if row[0] == "r":
                requirement += 1
    return requirement


def input_int_positive_number():
    while True:
        number = input(">>> ")
        if not number.isnumeric():
            print("Valid Number")
            continue
        if number.count('.') == 1:
            new_s = number.split('.')
            left_num = new_s[0]
            right_num = new_s[1]
            if right_num.isdigit():
                if left_num.isdigit():
                    print("Valid Number")
                    continue
                elif left_num.count('-') == 1 and left_num.startswith('-'):
                    tmp_num = left_num.split('-')[-1]
                    if tmp_num.isdigit():
                        print("Valid Number")
                        continue
        elif number.count(".") == 0:
            if number.isdigit():
                return int(number)
            elif number.count('-') == 1 and number.startswith('-'):
                ss = number.split('-')[-1]
                if ss.isdigit():
                    print("Valid Number")
                    continue


def list_albums():
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
        print(f"You need to listen to {requirement} albums.")


def main():
    print("Album Tracker 1.0 - by Roswaal Mathers")
    with open("albums.csv", "r") as albums:
        print(len(albums.readlines()), "albums loaded")
    while True:
        print("Menu:\nL - List all albums\nA - Add new album\nM - Mark an album as completed\nQ - Quit")
        choice = input(">>> ")
        if choice == "L" or choice == "l":
            list_albums()
            if count_requirement() == 0:
                print("No albums left to listen to. Why not add a new album?")
        elif choice == "A" or choice == "a":
            title = input("Title: ")
            while title.isspace():
                print("can not be blank")
                title = input("Title: ")
            artist = input("Artist: ")
            while artist.isspace():
                print("can not be blank")
                artist = input("Artist: ")
            years = input_int_positive_number()
            add_row = []
            add_row[0] = title
            add_row[1] = artist
            add_row[2] = years
            add_row[3] = "r"
            with open("albums.csv", "a", newline="") as albums:
                writer = csv.writer(albums)
                writer.writerow(add_row)
            print("{} by {} ({}) added to Album Tracker".format(title, artist, years))
        elif choice == "M" or choice == "m":

            if count_requirement() == 0:
                print("No required albums")
                continue
            list_albums()
            print("Enter the number of an album to mark as completed")
            completed_album = input_int_positive_number()
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
            break
        else:
            print("Invalid menu choice")


main()
