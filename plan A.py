import pandas as pd
csv_file_path = 'plant seats.csv'

class SeatBooking:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.seats = pd.read_csv(csv_file_path, index_col='seats')

    def check_availability(self, seat_label):
        seat_label = seat_label.upper()
        return self.seats.at[seat_label, 'Status'] == 'F'

    def book_seat(self, seat_label):
        seat_label = seat_label.upper()
        if self.check_availability(seat_label):
            self.seats.at[seat_label, 'Status'] = 'R'
            self.seats.to_csv(self.csv_file_path)
            return True
        else:
            return False

    def can_not_book_seat(self, seat_label):
        if self.check_availability(seat_label):
            self.seats.at[seat_label, 'Statis'] = 'X' and 'S'
            return False

    def free_seat(self, seat_label):
        if self.seats.at[seat_label, 'Status'] == 'R':
            self.seats.at[seat_label, 'Status'] = 'F'
            self.seats.to_csv(self.csv_file_path)
            return True
        else:
            return False

    def show_booking_state(self):
        for seat, row in self.seats.iterrows():
            print(f"{seat}:{row['Status']}")

def main_menu(csv_file_path):
    booking_system = SeatBooking(csv_file_path)

    while True:
        print("\nMenu:")
        print("1. Check availability of seat")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking state")
        print("5. Exit program")
        choice = input("Choose an option: ")

        if choice == '1':
            seat_label = input("Enter seat label (e.g., '1A'): ")
            if booking_system.check_availability(seat_label):
                print("The seat is available.")
            else:
                print("The seat is not available or does not exist.")

        elif choice == '2':
            seat_label = input("Enter seat label (e.g., '1A'): ")
            if booking_system.book_seat(seat_label):
                print("The seat has been booked.")
            else:
                print("The seat cannot be booked or does not exist.")

        elif choice == '3':
            seat_label = input("Enter seat label (e.g., '1A'): ")
            if booking_system.free_seat(seat_label):
                print("The seat has been freed.")
            else:
                print("The seat is not booked or does not exist.")

        elif choice == '4':
            booking_system.show_booking_state()

        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu(csv_file_path)