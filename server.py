
#Function definitions
def sort(hand):
    newHand = []
    check = 0
    while check < len(hand):
        for card in cards:
            for hold in hand:
                if hold == card:    #Search through every card in hand before moving to next card from deck
                    newHand.append(card)
                    check = check + 1
    hand = newHand
    print(hand)
    return hand
    
#Cards initialization
#Sorted from Ace to King, Clubs to Spades, with 2 Jokers listed as X1 and X2
cards = ["AC","AD","AH","AS","2C","2D","2H","2S","3C","3D","3H","3S","4C","4D","4H","4S","5C","5D","5H","5S","6C","6D","6H","6S","7C","7D","7H","7S","8C","8D","8H","8S","9C","9D","9H","9S","JC","JD","JH","JS","QC","QD","QH","QS","KC","KD","KH","KS","X1","X2"]

import socket
hostname = input("Please enter your IP address: ")
HOST = hostname  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
print("Server starting...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)