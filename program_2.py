# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    total_tickets = 0

    while True:
        choice = input("Do you want to enter a movie? (yes/no): ").lower()
        if choice == "no":
            break

        movie = input("Enter movie name: ")
        tickets = int(input(f"How many tickets for {movie}? "))
        total_tickets += tickets

    print(f"\nTotal tickets desired: {total_tickets}")


if __name__ == '__main__':
    main()