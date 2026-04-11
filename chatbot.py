def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hey there!")
        elif user_input == "how are you":
            print("Chatbot: I'm doing good, just a program though!")
        elif user_input == "what is your name":
            print("Chatbot: I'm a simple Python chatbot.")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: I don't understand that yet.")

chatbot()