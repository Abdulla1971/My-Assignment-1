#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime

class Passenger:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name


class BoardingPass:
    def __init__(self, passenger_Name, flight_Num, date_Time, gate, seat_Number, ticket, departure_Airport, destination):
        self.passenger_Name = passenger_Name
        self.flight_Num = flight_Num
        self.date_Time = date_Time
        self.gate = gate
        self.seat_Number = seat_Number
        self.ticket = ticket
        self.departure_Airport = departure_Airport
        self.destination = destination


class Flight:
    def __init__(self, flight_Number, departure, destination, date, time, gate):
        self.flight_Number = flight_Number
        self.departure = departure
        self.destination = destination
        self.date = date
        self.time = time
        self.gate = gate


class BoardingPassSystem:
    def __init__(self):
        self.boarding_pass = None

    def generateBoardingPass(self, passenger, flight, seat_Number, ticket):
        # Extract time component from flight.time
        time_component = flight.time.time()
        # Combine date and time components to create a datetime object
        date_time = datetime.combine(flight.date, time_component)
        self.boarding_pass = BoardingPass(passenger.getName(), flight.flight_Number, date_time, flight.gate, 
                                          seat_Number, ticket, flight.departure, flight.destination)

    def viewBoardingPass(self):
        if self.boarding_pass:
            print("Passenger Name:", self.boarding_pass.passenger_Name)
            print("Flight Number:", self.boarding_pass.flight_Num)
            print("Date & Time:", self.boarding_pass.date_Time)
            print("Gate:", self.boarding_pass.gate)
            print("Seat Number:", self.boarding_pass.seat_Number)
            print("Ticket:", self.boarding_pass.ticket)
            print("Departure Airport:", self.boarding_pass.departure_Airport)
            print("Destination:", self.boarding_pass.destination)
        else:
            print("No boarding pass information available.")

    def update_BoardingPass(self):
        if self.boarding_pass:
            print("Select the field you want to update:")
            print("1. Passenger Name")
            print("2. Flight Number")
            print("3. Date and Time")
            print("4. Seat Number")
            print("5. Departure Airport")
            print("6. Gate")
            choice = input("Enter your choice (1/2/3/4/5/6): ")

            if choice == '1':
                new_value = input("Enter new passenger name: ")
                self.boarding_pass.passenger_Name = new_value
                print("Passenger name updated successfully.")
            elif choice == '2':
                new_value = input("Enter new flight number: ")
                self.boarding_pass.flight_Num = new_value
                print("Flight number updated successfully.")
            elif choice == '3':
                new_value = input("Enter new date and time (YYYY-MM-DD HH:MM): ")
                self.boarding_pass.date_Time = datetime.strptime(new_value, "%Y-%m-%d %H:%M")
                print("Date and time updated successfully.")
            elif choice == '4':
                new_value = input("Enter new seat number: ")
                self.boarding_pass.seat_Number = new_value
                print("Seat number updated successfully.")
            elif choice == '5':
                new_value = input("Enter new departure airport: ")
                self.boarding_pass.departure_Airport = new_value
                print("Departure airport updated successfully.")
            elif choice == '6':
                new_value = input("Enter new gate: ")
                self.boarding_pass.gate = new_value
                print("Gate updated successfully.")
            else:
                print("Invalid choice.")
        else:
            print("No boarding pass information available.")

# Main function to run the program
def main():
    boardingPassSystem = BoardingPassSystem()
    
    while True:
        print("\nMenu:")
        print("1. Generate Boarding Pass")
        print("2. View Boarding Pass")
        print("3. Update Boarding Pass")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            # Take passenger details from the user
            passenger_name = input("Enter passenger name: ")
            passenger = Passenger(passenger_name)

            # Take flight details from the user
            flight_number = input("Enter flight number: ")
            departure_airport = input("Enter departure airport: ")
            destination = input("Enter destination: ")
            date_str = input("Enter date (YYYY-MM-DD): ")
            time_str = input("Enter time (HH:MM): ")
            gate = input("Enter gate: ")

            # Convert date and time strings to datetime objects
            date = datetime.strptime(date_str, "%Y-%m-%d")
            time = datetime.strptime(time_str, "%H:%M")

            # Take seat number and ticket number from the user
            seat_number = input("Enter seat number: ")
            ticket_number = input("Enter ticket number: ")

            flight = Flight(flight_number, departure_airport, destination, date, time, gate)

            # Generate boarding pass
            boardingPassSystem.generateBoardingPass(passenger, flight, seat_number, ticket_number)
            
        elif choice == '2':
            # View boarding pass information
            print("\nView the Boarding pass:")
            boardingPassSystem.viewBoardingPass()
            
        elif choice == '3':
            # Update boarding pass information
            boardingPassSystem.update_BoardingPass()
            
        elif choice == '4':
            print("Exiting...")
            break
            
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()


# In[ ]:




