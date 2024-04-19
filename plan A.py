import pandas as pd
csv_file_path = 'plant seats.csv'# Define the path to the CSV file

class SeatBooking:
    # Initialization method for the SeatBooking class
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path# Store the CSV file path
        self.seats = pd.read_csv(csv_file_path, index_col='seats')
        # Read the CSV into a pandas DataFrame and set 'seats' as the index column
    def check_availability(self, seat_label):  # Check if a seat is available (Status is 'F' for free)
        seat_label = seat_label.upper()# Convert the seat label to uppercase
        return self.seats.at[seat_label, 'Status'] == 'F'

    def book_seat(self, seat_label):# Book a seat if it is available
        seat_label = seat_label.upper()# Convert the seat label to uppercase
        if self.check_availability(seat_label):# Check if the seat is available
            self.seats.at[seat_label, 'Status'] = 'R' # Change the status to 'R' for reserved
            self.seats.to_csv(self.csv_file_path)# Save the updated DataFrame back to the CSV
            return True
        else:
            return False

    def can_not_book_seat(self, seat_label):# Method to handle a seat that cannot be booked
        if self.check_availability(seat_label):
            self.seats.at[seat_label, 'Statis'] = 'X' and 'S'
            return False

    def free_seat(self, seat_label): # Free a seat that was previously booked
        if self.seats.at[seat_label, 'Status'] == 'R':# Check if the seat is reserved
            self.seats.at[seat_label, 'Status'] = 'F'# Change the status to 'F' for free
            self.seats.to_csv(self.csv_file_path)# Save the updated DataFrame back to the CSV
            return True
        else:
            return False

    def show_booking_state(self):# Display the booking status for each seat
        for seat, row in self.seats.iterrows():# Iterate through each row in the DataFrame
            print(f"{seat}:{row['Status']}")# Print the seat label and its booking status

def main_menu(csv_file_path):# Function to display the main menu and handle user input
    booking_system = SeatBooking(csv_file_path) # Create an instance of SeatBooking

    while True:
        # Print the main menu options
        print("\nMenu:")
        print("1. Check availability of seat")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking state")
        print("5. Exit program")
        # Get the user's choice
        choice = input("Choose an option: ")
        # Handle the user's choice
        if choice == '1':
            seat_label = input("Enter seat label (e.g., '1A'): ").upper()  # Check and display the availability of a seat
            if booking_system.check_availability(seat_label):
                print("The seat is available.")
            else:
                print("The seat is not available or does not exist.")

        elif choice == '2':
            seat_label = input("Enter seat label (e.g., '1A'): ").upper()
            # Attempt to book a seat and display the result
            if booking_system.book_seat(seat_label):
                print("The seat has been booked.")
            else:
                print("The seat cannot be booked or does not exist.")

        elif choice == '3':
            seat_label = input("Enter seat label (e.g., '1A'): ").upper()
            # Attempt to free a seat and display the result
            if booking_system.free_seat(seat_label):
                print("The seat has been freed.")
            else:
                print("The seat is not booked or does not exist.")

        elif choice == '4':
            booking_system.show_booking_state()# Show the current booking state of all seats

        elif choice == '5':# Exit the program
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")# Handle invalid options
#call the main_menu function
if __name__ == "__main__":
    main_menu(csv_file_path)