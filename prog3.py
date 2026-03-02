import random
import string

def run_captcha():
    captcha = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    print(f"System CAPTCHA: {captcha}")
    user_input = input("Enter the CAPTCHA exactly as shown to prove you are human: ")
    return user_input == captcha

def simple_turing_test():
    bot_responses = [
        "That is an interesting perspective.",
        "Could you elaborate on that?",
        "I understand. What else is on your mind?",
        "Why do you feel that way?",
        "Fascinating."
    ]
    
    print("\nAccess Granted. Initiating Turing Test Module.")
    print("Type 'exit' to end the conversation.\n")
    
    while True:
        user_text = input("Human: ")
        if user_text.lower() == 'exit':
            print("Terminating session.")
            break
        print(f"Agent: {random.choice(bot_responses)}")

if __name__ == "__main__":
    if run_captcha():
        simple_turing_test()
    else:
        print("CAPTCHA failed. Access Denied.")