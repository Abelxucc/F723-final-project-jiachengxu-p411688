import pandas as pd
csv_file_path = 'plant seats.csv'

class SeatBooking:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.seats = pd.read_csv(csv_file_path, index_col='seats')

    def check_availability(self, seat_label):
        return self.seats.at[seat_label, 'Status'] == 'F'

    def book_seat(self, seat_label):
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


