import random

# Define ranks and suits for the deck
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Function to create and shuffle a deck of cards
def create_deck():
    return [(rank, suit) for suit in suits for rank in ranks]

# Function to deal cards to players
def deal_cards(deck, num_cards):
    return [deck.pop() for _ in range(num_cards)]

# Function to display cards
def display_cards(cards, player_name):
    print(f"{player_name}'s cards:")
    for i, card in enumerate(cards):
        print(f"{i + 1}: {card[0]} of {card[1]}")

# Function to check if a card matches the table card
def is_match(card, table_card):
    return card[0] == table_card[0] or card[1] == table_card[1]

# Main function to run the game
def main():
    # Create and shuffle the deck
    deck = create_deck()
    random.shuffle(deck)

    # Deal cards to players
    player_hand = deal_cards(deck, 4)
    computer_hand = deal_cards(deck, 4)

    # Place one card from the deck face up on the table
    table_card = deck.pop()

    # Game loop
    while len(player_hand) < 7 and len(computer_hand) < 7:
        # Player's turn
        print("\nTable card:", table_card[0], 'of', table_card[1])
        display_cards(player_hand, "Your")
        player_input = input("Select a card to play (1-4) or press 'q' to quit: ")

        if player_input.lower() == 'q':
            print("Quitting the game.")
            break

        try:
            selected_index = int(player_input) - 1
            selected_card = player_hand[selected_index]

            if is_match(selected_card, table_card):
                table_card = selected_card
                player_hand.remove(selected_card)
                print("You matched the card on the table!")
            else:
                print("You didn't match the card on the table. Penalty!")
                player_hand.append(deck.pop())

        except (ValueError, IndexError):
            print("Invalid input. Please select a card from 1 to 4.")

        # Computer's turn
        if len(player_hand) < 7:
            computer_input = random.choice(computer_hand)
            if is_match(computer_input, table_card):
                table_card = computer_input
                computer_hand.remove(computer_input)
                print("Computer matched the card on the table!")
            else:
                print("Computer didn't match the card on the table. Penalty!")
                computer_hand.append(deck.pop())

        # Display the computer's move
        display_cards(computer_hand, "Computer")
        print("Computer selected:", computer_input[0], 'of', computer_input[1])

    # Determine the winner
    if len(player_hand) >= 7:
        print("Sorry, you lose! Please try again.")
    elif len(computer_hand) >= 7:
        print("Congratulations! You've won!")
    elif len(player_hand) == 0:
        print("Congratulations! You've won!")    
    else:
        print("It's a tie!")

# Run the game
if __name__ == "__main__":
    main()
