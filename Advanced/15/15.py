'''
Write a program in python to implement Railway Reservation System using file handling 
technique. System should perform below operations. 
a) Reserve a ticket for a passenger. 
b) List information all reservations done for today’s trains.
'''
# import datetime

# # File to store reservation data
# FILE_NAME = "reservations.txt"

# # Function to reserve a ticket
# def reserve_ticket():
#     name = input("Enter passenger name: ")
#     age = input("Enter passenger age: ")
#     train_number = input("Enter train number: ")
#     seat_number = input("Enter seat number: ")
#     date_of_travel = input("Enter date of travel (YYYY-MM-DD): ")
    
#     # Store the reservation in a file
#     with open(FILE_NAME, "a") as file:
#         file.write(f"{name},{age},{train_number},{seat_number},{date_of_travel}\n")
    
#     print("Ticket reserved successfully!\n")

# # Function to list all reservations for today's date
# def list_reservations():
#     today = datetime.date.today().strftime("%Y-%m-%d")
#     found = False
    
#     print(f"Reservations for {today}:")
#     with open(FILE_NAME, "r") as file:
#         for line in file:
#             data = line.strip().split(",")
#             if data[-1] == today:  # Check if reservation is for today
#                 print(f"Passenger: {data[0]}, Age: {data[1]}, Train: {data[2]}, Seat: {data[3]}")
#                 found = True
    
#     if not found:
#         print("No reservations found for today.\n")

# # Menu-driven system
# def main():
#     while True:
#         print("\nRailway Reservation System")
#         print("1. Reserve a Ticket")
#         print("2. List Today's Reservations")
#         print("3. Exit")
#         choice = input("Enter your choice: ")
        
#         if choice == "1":
#             reserve_ticket()
#         elif choice == "2":
#             list_reservations()
#         elif choice == "3":
#             print("Exiting the system. Have a nice day!")
#             break
#         else:
#             print("Invalid choice. Please try again.\n")

# if __name__ == "__main__":
#     main()

import datetime
import os

class RailwayReservation:
    def __init__(self):
        # File to store reservations
        self.reservation_file = "reservations.txt"
        # Create file if it doesn't exist
        if not os.path.exists(self.reservation_file):
            with open(self.reservation_file, 'w') as f:
                f.write("PNR,Passenger Name,Train No,Date\n")

    def generate_pnr(self):
        """Generate a unique PNR number"""
        current_time = datetime.datetime.now()
        pnr = f"PNR{current_time.strftime('%Y%m%d%H%M%S')}"
        return pnr

    def reserve_ticket(self):
        """Reserve a ticket for a passenger"""
        print("\n=== Ticket Reservation ===")
        passenger_name = input("Enter passenger name: ")
        train_no = input("Enter train number: ")
        date = datetime.datetime.now().strftime("%Y-%m-%d")

        # Generate PNR
        pnr = self.generate_pnr()

        # Store reservation in file
        reservation_data = f"{pnr},{passenger_name},{train_no},{date}\n"
        
        try:
            with open(self.reservation_file, 'a') as f:
                f.write(reservation_data)
            print(f"\nTicket reserved successfully!")
            print(f"PNR Number: {pnr}")
            print(f"Passenger: {passenger_name}")
            print(f"Train No: {train_no}")
            print(f"Date: {date}")
        except Exception as e:
            print(f"Error reserving ticket: {e}")

    def list_todays_reservations(self):
        """List all reservations for today's date"""
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        print(f"\n=== Reservations for Today ({today}) ===")
        
        try:
            with open(self.reservation_file, 'r') as f:
                lines = f.readlines()
                
                # Skip header line
                if len(lines) <= 1:
                    print("No reservations found for today!")
                    return
                
                found = False
                print("PNR\t\tPassenger Name\tTrain No\tDate")
                print("-" * 50)
                
                for line in lines[1:]:  # Skip header
                    pnr, name, train_no, date = line.strip().split(',')
                    if date == today:
                        print(f"{pnr}\t{name}\t\t{train_no}\t\t{date}")
                        found = True
                
                if not found:
                    print("No reservations found for today!")
                    
        except Exception as e:
            print(f"Error reading reservations: {e}")

def main():
    railway = RailwayReservation()
    
    while True:
        print("\n=== Railway Reservation System ===")
        print("1. Reserve a Ticket")
        print("2. List Today's Reservations")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            railway.reserve_ticket()
        elif choice == '2':
            railway.list_todays_reservations()
        elif choice == '3':
            print("Thank you for using Railway Reservation System!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()