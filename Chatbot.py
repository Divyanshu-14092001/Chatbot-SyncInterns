import random

# Define the responses for the chatbot
responses = {
    "hello": "Hello! How can I assist you?",
    "how are you": "I'm doing well, thank you!",
    "what's your name": "I am a simple chatbot.",
    "bye": "Goodbye! Have a great day!",
}


def get_response(user_input):
    """
    Get the chatbot's response based on user input.
    """
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return "I'm sorry, I don't understand that. Can you please try something else?"


def main():
    """
    Main function to run the chatbot.
    """
    print("Chatbot: Hi there! I'm a simple chatbot. You can start a conversation with me.")
    print("Chatbot: Type 'bye' to exit the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            response = get_response(user_input)
            print("Chatbot:", response)


if __name__ == "__main__":
    main()
