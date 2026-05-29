

import random
from datetime import datetime


def greet_user():
    print("CyberBot: Hello! I'm CyberBot, your beginner AI chatbot.")
    print("CyberBot: You can ask me about cybersecurity, passwords, school, or just chat.")
    print("CyberBot: Type 'bye' to exit.\n")


def get_time():
    current_time = datetime.now().strftime("%I:%M %p")
    return f"The current time is {current_time}."


def password_tip():
    tips = [
        "Use at least 12 characters in your password.",
        "Mix uppercase letters, lowercase letters, numbers, and symbols.",
        "Avoid using your name, birthday, or common words.",
        "Use a different password for every important account.",
        "Consider using a password manager to store strong passwords."
    ]
    return random.choice(tips)


def cybersecurity_tip():
    tips = [
        "Never click suspicious links in emails or text messages.",
        "Turn on two-factor authentication whenever possible.",
        "Keep your software and apps updated.",
        "Do not share personal information with unknown websites.",
        "Use secure Wi-Fi and avoid logging into accounts on public networks."
    ]
    return random.choice(tips)


def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm doing good! Thanks for asking. How are you?"

    elif "your name" in user_input:
        return "My name is CyberBot. I was created as a beginner Python chatbot."

    elif "time" in user_input:
        return get_time()

    elif "password" in user_input:
        return password_tip()

    elif "cyber" in user_input or "security" in user_input or "hack" in user_input:
        return cybersecurity_tip()

    elif "school" in user_input or "college" in user_input:
        return "School can be challenging, but staying organized and consistent makes a big difference."

    elif "career" in user_input or "job" in user_input or "internship" in user_input:
        return "A good career move is to build projects, improve your resume, and keep applying consistently."

    elif "python" in user_input:
        return "Python is a great programming language for beginners, automation, cybersecurity, and AI projects."

    elif "help" in user_input:
        return "You can ask me about passwords, cybersecurity tips, Python, school, jobs, or the current time."

    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        return "Goodbye! Thanks for chatting with me."

    else:
        responses = [
            "That's interesting. Tell me more.",
            "I am still learning, but I can try to help.",
            "Can you explain that another way?",
            "That sounds important. What made you ask that?",
            "I do not fully understand yet, but I am learning from the conversation."
        ]
        return random.choice(responses)


def main():
    greet_user()

    while True:
        user_input = input("You: ")

        response = chatbot_response(user_input)
        print("CyberBot:", response)

        if user_input.lower() in ["bye", "exit", "quit"]:
            break


if __name__ == "__main__":
    main()
