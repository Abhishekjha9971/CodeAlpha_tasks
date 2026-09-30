"""
CodeAlpha Python Internship - Task 4: Basic Chatbot
A simple rule-based chatbot that responds to predefined user inputs.
"""

import random


RESPONSES = {
    "hello": ["Hi!", "Hello there!", "Hey! How can I help you?"],
    "hi": ["Hi!", "Hello!", "Hey there!"],
    "how are you": ["I'm fine, thanks!", "Doing great, how about you?"],
    "what is your name": ["I'm a simple chatbot built in Python!", "You can call me PyBot."],
    "what can you do": ["I can chat with you about a few basic things. Try saying 'hello' or 'bye'!"],
    "thank you": ["You're welcome!", "No problem!", "Anytime!"],
    "thanks": ["You're welcome!", "Glad to help!"],
    "bye": ["Goodbye!", "Bye! Have a great day!", "See you later!"],
}

DEFAULT_RESPONSES = [
    "Sorry, I didn't understand that. Can you rephrase?",
    "I'm not sure how to respond to that yet.",
    "Hmm, I don't know about that. Try asking something else!",
]

EXIT_KEYWORDS = {"bye", "goodbye", "exit", "quit"}


def get_response(user_input):
    # Match user input against predefined patterns and return a reply.
    text = user_input.strip().lower()

    # Strip common punctuation for easier matching
    text = text.strip("!?.,")

    for key, replies in RESPONSES.items():
        if key in text:
            return random.choice(replies)

    return random.choice(DEFAULT_RESPONSES)


def is_exit(user_input):
    text = user_input.strip().lower().strip("!?.,")
    return any(word in text for word in EXIT_KEYWORDS)


def chat():
    print("=" * 50)
    print("  SIMPLE CHATBOT (type 'bye' to exit)")
    print("=" * 50)
    print("Bot: Hi! Talk to me. (say 'hello', 'how are you', 'bye', etc.)\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Bot: Please type something.\n")
            continue

        if is_exit(user_input):
            print(f"Bot: {random.choice(RESPONSES['bye'])}")
            break

        response = get_response(user_input)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    chat()
