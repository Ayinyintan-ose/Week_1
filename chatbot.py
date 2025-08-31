print("Chatbot: Welcome to your friendly chatbot! Below are the available questions I can answer:")

services = ["How are you today?", "What's is your name?", "What is the weather like today?", "Tell me about yourself.",
            "bye"]
for index, service in enumerate(services):
    print(f"{index + 1}. {service}")

def chatbot():
    print("What would you like to know?")
    print("P.S: ensure to add the necessary punctuation marks. ")
    while True:
        user_input = input("You: ").lower()

        if user_input == "how are you today?".lower():
            print("Bot: I'm fine and you?")
        elif user_input == "What's your name?".lower():
            print("Bot: My name is Clark")
        elif user_input == "What's the weather like today".lower():
            print("It's a beautiful day to go out.")
        elif user_input == "Tell me about yourself".lower():
            print("""I'm Clark, your friendly chat bot. what would you like me todo for you today?""")
        elif user_input == "bye".lower():
            print("We'll talk some other time. Bye for now!")
            break
        else:
            print("Sorry, i can't answer that.")


chatbot()