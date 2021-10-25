"""
Update this module docstring with your own details
Name:Roswaal Mathers
Date started:10/25/2021
"""
import csv


def list_albums():
    albums_in_fun = open("albums.csv", "r")
    reader_in_fun = csv.reader(albums_in_fun)
    requirement = 0
    for index, row in enumerate(reader_in_fun):
        if row[3] == "r":
            print("*{}. {:<30s}by {:<15}({})".format(index + 1, row[0], row[1], row[2]))
        else:
            print(" {}. {:<30s}by {:<15}({})".format(index + 1, row[0], row[1], row[2]))
        if row[3] == "r":
            requirement += 1
    print(f"You need to listen to {requirement} albums.")
    albums.close()


def main():
    print("Album Tracker 1.0 - by Roswaal Mathers")
    albums = open("albums.csv", "r")
    print(len(albums.readlines()), "albums loaded")
    albums.close()
    print("Menu:\nL - List all albums\nA - Add new album\nM - Mark an album as completed\nQ - Quit")
    choice = input(">>> ")
    while True:
        if choice == "L" or choice == "l":
            list_albums()

        elif choice == "A" or choice == "a":
            title = input("Title: ")
            while title.isspace():
                print("can not be blank")
                title = input("Title: ")

            artist = input("Artist: ")
            while artist.isspace():
                print("can not be blank")
                artist = input("Artist: ")

            years = input("Years: ")
            while not (years.isnumeric() and 0 < int(years) < 2022):
                years = input("Years: ")
                print("Invalid input")

            add_row = ["", "", "", ""]
            add_row[0] = title
            add_row[1] = artist
            add_row[2] = years
            add_row[3] = "r"
            albums = open("albums.csv", "a", newline="")
            writer = csv.writer(albums)
            writer.writerow(add_row)
            albums.close()
            print("{} by {} ({}) added to Album Tracker".format(title, artist, years))

        elif choice == "M" or choice == "m":
            list_albums()
            print("Enter the number of an album to mark as completed")
            completed_album = int(input(">>> "))
            while not (str(completed_album).isnumeric() and completed_album > 0):
                print("Invalid input")
                completed_album = int(input(">>> "))

            albums = open("albums.csv", "w")
            writer = csv.writer(albums)
            writer[completed_album][3] = 'c'
            albums = open("albums.csv", "r")
            reader = csv.reader(albums)
            albums.close()
            print(f"You have already listened to {reader[completed_album][0]}")

        elif choice == "Q" or choice == "q":
            albums = open("albums.csv", "r")
            print(len(albums.readlines()), " albums saved to albums.csv")
            albums.close()
            break

        else:
            print("Invalid menu choice")
        print("Menu:\nL - List all albums\nA - Add new album\nM - Mark an album as completed\nQ - Quit")
        choice = input(">>> ")


main()
