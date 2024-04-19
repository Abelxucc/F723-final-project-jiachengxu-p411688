import pandas as pd
import random
import string
# Define the path
csv_file_path = 'plant seats for plan b2.csv'
file_path = 'plant seats for plan b2.csv'
class BookingReferenceGenerator:
    def __init__(self):
        self.generated_references = set()# Keep track of generated references to ensure uniqueness

    def generate_unique_reference(self):
        # Generate a random 8-character string until a unique one is found
        while True:
            reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            if reference not in self.generated_references:
                self.generated_references.add(reference)
                return reference

# This class manages the seat booking logic
class SeatBooking:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        # Read the seats from the CSV file into a DataFrame and set the 'seats' column as the index
        self.seats = pd.read_csv(csv_file_path)
        # If the 'reference' column doesn't exist, add it
        if 'reference' not in self.seats.columns:
            self.seats['reference'] = ''
        self.seats.set_index('seats', inplace=True)
        self.reference_generator = BookingReferenceGenerator()
        self.booking_details = {}  # A dictionary to store booking details

    def check_availability(self, seat_label):# Check if a specific seat is available
        seat_label = seat_label.upper()# Convert the seat label to uppercase
        return self.seats.at[seat_label, 'Status'] == 'F'

    def book_seat(self, seat_label, customer_data):# Book a seat if it is available
        seat_label = seat_label.upper()# Convert the seat label to uppercase
        if self.check_availability(seat_label):# Check if the seat is available
            reference = self.reference_generator.generate_unique_reference()
            self.seats.at[seat_label, 'Status'] = 'R'# Change the status to 'R' for reserved
            self.seats.at[seat_label, 'CustomerName'] = customer_data['name']# store data
            self.seats.at[seat_label, 'CustomerEmail'] = customer_data['email']
            self.seats.at[seat_label, 'reference'] = reference
            self.booking_details[seat_label] = {
                'reference': reference,
                'customer_data': customer_data
            }
            self.seats.to_csv(self.csv_file_path)# Save the updated DataFrame back to the CSV
            print(f"Booking complete. Reference: {reference}")
            return True
        else:
            return False

    def free_seat(self, seat_label): # Free a seat that was previously booked
        seat_label = seat_label.upper()
        if self.seats.at[seat_label, 'Status'] == 'R':# Check if the seat is reserved
            self.seats.at[seat_label, 'Status'] = 'F'# Change the status to 'F' for free
            self.booking_details.pop(seat_label, None)  # Remove booking details
            self.seats.to_csv(self.csv_file_path)# Save the updated DataFrame back to the CSV
            return True
        else:
            return False

    def show_booking_state(self):# Display the booking status for each seat
        for seat_label, details in self.booking_details.items():# Iterate through each row in the DataFrame
            status = self.seats.at[seat_label, 'Status']
            print(f"Seat {seat_label} is {status}. Booking reference: {details['reference']}")# Print the seat label and its booking status


def main_menu(csv_file_path):# Function to display the main menu and handle user input
    booking_system = SeatBooking(csv_file_path)# Create an instance of SeatBooking

    while True: # Print the main menu options
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
            seat_label = input("Enter seat label (e.g., '1A'): ").upper()
            # Check and display the availability of a seat
            if booking_system.check_availability(seat_label):
                print("The seat is available.")
            else:
                print("This seat is not available.")

        elif choice == '2':
            seat_label = input("Enter seat label (e.g., '1A'): ").upper()
            # Attempt to book a seat and display the result
            if booking_system.check_availability(seat_label): #check the availability first
                name = input("Enter the customer's name: ")
                email = input("Enter the customer's email: ")
                customer_data = {'name': name, 'email': email}
                if booking_system.book_seat(seat_label, customer_data):
                    print("The seat has been booked.")
                else:
                    print("This seat has already been booked or does not exist.")

        elif choice == '3':
            seat_label = input("Enter seat label (e.g., '1A'): ").upper()
            # Attempt to free a seat and display the result
            if booking_system.free_seat(seat_label):
                print("The seat has been freed.")
            else:
                print("Sorry this seat is not booked or does not exist.")

        elif choice == '4':
            booking_system.show_booking_state()# Show the current booking state of all seats

        elif choice == '5':# Exit the program
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")# Handle invalid option
#call the main_menu function
if __name__ == "__main__":
    main_menu(csv_file_path)