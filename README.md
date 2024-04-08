# Plate Code Prediction Game - TCP Socket Programming 

## Introduction

This project implements a plate code prediction game using Python socket programming. The game involves a client-server architecture where the server selects a city randomly, and the client predicts the associated license plate code. The assignment aims to enhance understanding of socket programming concepts, improve network communication skills, and refine problem-solving abilities in real-world application development scenarios.

The assignment requires the development of a plate code prediction game using Python and socket programming. The project comprises two main components: server.py and client.py. The server utilizes the socket and pandas modules to manage client connections, select random cities and their plate codes, and validate client predictions. The client establishes a connection with the server using TCP sockets, receives prompts from the server, makes predictions, and handles game termination conditions. Both server and client operate on localhost using port 12345.


## Project Structure

- `server.py`: Contains the server-side code responsible for handling client connections, choosing a random city, and validating plate code predictions.
- `client.py`: Implements the client-side code, which connects to the server, receives city information, and allows the user to make predictions.
- `plate_list.xlsx`: Excel file containing a list of plate codes for various cities.

## Requirements

- Python 3.x
- pandas library (for reading Excel files)

  
## Usage

1. Clone the repository
2.  Navigate to the project directory
3. Start the server:

> python3 server.py

4. In a separate terminal or command prompt, start the client:

> python3 client.py

5.  Follow the instructions in the client terminal to make predictions and play the game.

## Implementation Results

Image 1: Output when input is non-numeric value

<img src="https://raw.githubusercontent.com/iremsilamadenli/PlateCodePredictionGame-TCPSocketProgramming/main/PlateCodePrediction/nonnumeric.png" height="200" />

Image 2: Output when input is over 81

<img src="https://raw.githubusercontent.com/iremsilamadenli/PlateCodePredictionGame-TCPSocketProgramming/main/PlateCodePrediction/range.png" height="200" />

Image 3: Output when input is “END”

<img src="https://raw.githubusercontent.com/iremsilamadenli/PlateCodePredictionGame-TCPSocketProgramming/main/PlateCodePrediction/end.png" height="200" />

Image 4: Output when input is correct

<img src="https://raw.githubusercontent.com/iremsilamadenli/PlateCodePredictionGame-TCPSocketProgramming/main/PlateCodePrediction/correct.png" height="200" />

Image 5: Seeing the server part when more than one client connection


<img src="https://raw.githubusercontent.com/iremsilamadenli/PlateCodePredictionGame-TCPSocketProgramming/main/PlateCodePrediction/moreclient.png" height="200" />


## Conclusion

In conclusion, the Plate Code Prediction Game successfully demonstrates the implementation of a client-server application using Python socket programming. Through this project, we gained valuable insights into network communication, socket handling, and data exchange between clients and servers.

The game's architecture, with the server randomly selecting cities and clients predicting their associated license plate codes, provided an engaging user experience. By adhering to best practices and assignment requirements, we ensured robust error handling, smooth communication, and graceful termination conditions.

This project served as an excellent opportunity to apply theoretical knowledge into practical implementation, fostering a deeper understanding of socket programming concepts. Moving forward, the skills acquired through this project will be invaluable in tackling more complex networking challenges and real-world application development tasks.

## References

- Real Python Socket Programming Tutorial: [Link](https://realpython.com/python-sockets/)
- Sarker & Washington (2015), Learning Python Network Programming. Packt Publishing.


## Contributors

- Feride Betül Çuhadar 
- Doğa Durmaz
- İrem Sıla Madenli

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
