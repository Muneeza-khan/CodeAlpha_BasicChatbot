def chatbot():

    print("\n===================================")
    print("      Welcome to Simple Chatbot")
    print("===================================")
    print("Type 'bye' to end the conversation.\n")

    while True:

        user_input = input("You: ").strip().lower()

        # Greetings
        if user_input == "hello":
            print("Bot: Hi! How can I help you?")

        # Asking chatbot condition
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks for asking!")

        # Asking chatbot name
        elif user_input == "what is your name":
            print("Bot: I am a Python Rule-Based Chatbot.")

        # Asking creator
        elif user_input == "who created you":
            print("Bot: I was created by muneeza Khan for the CodeAlpha internship task.")

        # Goodbye condition
        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        # Unknown input
        else:
            print("Bot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()