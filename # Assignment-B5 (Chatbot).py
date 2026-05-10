# Assignment-B5 (Chatbot)

import datetime


def restaurant_chatbot():

    print("Welcome to the K's Restaurant!")
    print("You can ask me about the menu, prices, contact details, reservations, timings, etc.")

    while True:

        user_input = input("\nYou: ").lower()

        # Greetings
        if "hi" in user_input or "hello" in user_input or "hey" in user_input:

            print("Chatbot: Hello! Welcome to K's Restaurant. How can I help you today?")

        # Menu
        elif "menu" in user_input:

            print("\nChatbot: Our Menu:")
            print("1. Pasta      - Rs.250")
            print("2. Pizza      - Rs.350")
            print("3. Salads     - Rs.200")
            print("4. Desserts   - Rs.150")

        # Cost / Price
        elif "cost" in user_input or "price" in user_input or "how much" in user_input:

            print("\nChatbot: Menu Prices:")
            print("Pasta      -> Rs.250")
            print("Pizza      -> Rs.350")
            print("Salads     -> Rs.200")
            print("Desserts   -> Rs.150")
            print("Average cost per person is around Rs.500.")

        # Contact
        elif "contact" in user_input or "phone" in user_input:

            print("Chatbot: You can contact us at +91-1234567890")

        # Reservation
        elif "reservation" in user_input or "book" in user_input:

            print("Chatbot: To make a reservation, please call us at +91-1234567890")

        # Restaurant Hours
        elif "hours" in user_input or "timing" in user_input:

            print("Chatbot: We are open from 11 AM to 10 PM, Monday to Sunday.")

        # Date and Time
        elif "date" in user_input or "time" in user_input:

            now = datetime.datetime.now()

            print(f"Chatbot: Today's date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}")

        # How are you
        elif "how are you" in user_input or "how's it going" in user_input or "sup" in user_input:

            print("Chatbot: I'm just a bot, but I'm here to help you!")

        # Funny Response
        elif "meow" in user_input:

            print("Chatbot: Meow meow meow!")

        # Exit
        elif "exit" in user_input or "quit" in user_input:

            print("Chatbot: Thank you for chatting with us! Have a great day!")
            break

        # Unknown Input
        else:

            print("Chatbot: I'm sorry, I didn't understand that. Can you ask something else?")


restaurant_chatbot()