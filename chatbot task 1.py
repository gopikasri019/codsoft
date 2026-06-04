from colorama import init, Fore, Style
from datetime import datetime
import random

# Initialize colorama
init(autoreset=True)

# -----------------------------
# Chatbot Information
# -----------------------------
BOT_NAME = "SmartBot"

# -----------------------------
# Response Database
# -----------------------------

greetings = [
    "Hello! Nice to meet you.",
    "Hi! How can I assist you today?",
    "Greetings! What can I do for you?"
]

how_are_you = [
    "I'm doing great. Thanks for asking!",
    "I'm functioning perfectly.",
    "Everything is running smoothly."
]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did Python go to school? To improve its class!",
    "Debugging: Being the detective in a crime movie where you are also the criminal."
]

motivations = [
    "Success is the sum of small efforts repeated daily.",
    "Believe in yourself and keep learning.",
    "Every expert was once a beginner."
]

# -----------------------------
# Utility Functions
# -----------------------------

def print_bot(message):
    print(Fore.CYAN + Style.BRIGHT + f"\n{BOT_NAME}: {message}")

def current_time():
    return datetime.now().strftime("%I:%M:%S %p")

def current_date():
    return datetime.now().strftime("%d-%m-%Y")

def show_help():
    commands = """
Available Commands:
--------------------------
hello / hi
how are you
your name
time
date
joke
motivate me
python
ai
help
bye
"""
    print_bot(commands)

# -----------------------------
# Chatbot Logic
# -----------------------------

def process_message(user_input):

    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey"]:
        return random.choice(greetings)

    elif "how are you" in user_input:
        return random.choice(how_are_you)

    elif "your name" in user_input:
        return f"My name is {BOT_NAME}. I am a Python chatbot."

    elif user_input == "time":
        return f"Current Time: {current_time()}"

    elif user_input == "date":
        return f"Today's Date: {current_date()}"

    elif user_input == "joke":
        return random.choice(jokes)

    elif "motivate" in user_input:
        return random.choice(motivations)

    elif "python" in user_input:
        return ("Python is a high-level programming language "
                "used in AI, Data Science, Web Development, "
                "Automation, and more.")

    elif user_input == "ai":
        return ("Artificial Intelligence enables machines "
                "to learn, reason, and make decisions.")

    elif user_input == "help":
        show_help()
        return None

    elif user_input == "bye":
        return "EXIT"

    else:
        return ("I don't understand that command. "
                "Type 'help' to see available commands.")

# -----------------------------
# Main Function
# -----------------------------

def chatbot():

    print(Fore.GREEN + "=" * 60)
    print(Fore.YELLOW + Style.BRIGHT +
          "      PROFESSIONAL PYTHON CHATBOT SYSTEM")
    print(Fore.GREEN + "=" * 60)

    print_bot("Hello! Welcome to SmartBot.")
    print_bot("Type 'help' to view available commands.")
    print_bot("Type 'bye' to exit.")

    while True:

        user_input = input(
            Fore.MAGENTA + Style.BRIGHT + "\nYou: "
        )

        response = process_message(user_input)

        if response == "EXIT":
            print_bot("Thank you for chatting. Goodbye!")
            break

        elif response:
            print_bot(response)

# -----------------------------
# Program Entry Point
# -----------------------------

if __name__ == "__main__":
    chatbot()