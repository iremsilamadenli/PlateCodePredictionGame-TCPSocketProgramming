import socket
import random
import pandas as pd

# Reading the Excel file containing plate codes for cities
plate_codes_df = pd.read_excel('plate_list.xlsx')

def choose_city_and_plate():
    random_row = plate_codes_df.sample()
    city = random_row['CityName'].values[0]
    plate_code = random_row['PlateNumber'].values[0]
    return city, plate_code

def validate_input(prediction):
    return prediction.isdigit() and 1 <= int(prediction) <= 81

# Function to handle client connection and plate code prediction
def handle_client_connection(client_socket):
    city, plate_code = choose_city_and_plate()
    client_socket.send(f"What is the plate code for{city}:".encode())
    correct_answer_received = False
    while not correct_answer_received:
        prediction = client_socket.recv(1024).decode().strip()
        print(f"Received from client: {prediction}")
        if prediction.upper() == "END":
            client_socket.send("You ended the game. Game over.\n".encode())
            break
        if not prediction.isdigit():
            client_socket.send("You entered a non-numeric value. Game over.\n".encode())
            break
        if not validate_input(prediction):
            client_socket.send("Number exceeds the range. Game over.\n".encode())
            break
        if int(prediction) == plate_code:
            client_socket.send("Correct!".encode())
            correct_answer_received = True
        else:
            city_guess = plate_codes_df[plate_codes_df['PlateNumber'] == int(prediction)]['CityName'].values
            if len(city_guess) > 0:
                client_socket.send(f"You have entered the plate code of{city_guess[0]}.".encode())
            else:
                client_socket.send("Wrong! Please guess again.\n".encode())
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    
    n=1
    while True:
        print(f"Wait for {n}th client connection")
        n+=1
        print("Server waiting for connection...")
        
        client_socket, address = server_socket.accept()
        print(f"Client connected from: {address}")
        handle_client_connection(client_socket)

if __name__ == "__main__":
    main()
