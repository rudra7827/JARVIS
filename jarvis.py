JARVIS AI Assistant in Python (Terminal-based)

import datetime import random

class JarvisAI: def init(self): self.memory = [] self.greet()

def greet(self):
    print("\nJARVIS: Hello, how can I assist you today?\n")

def add_message(self, sender, message):
    print(f"{sender}: {message}")

def process_command(self, command):
    cmd = command.lower().strip()
    self.memory.append(cmd)

    if 'time' in cmd:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.add_message('JARVIS', f'The current time is {now}')

    elif 'date' in cmd:
        today = datetime.date.today().strftime("%B %d, %Y")
        self.add_message('JARVIS', f'Today is {today}')

    elif 'battery' in cmd:
        battery = random.randint(20, 100)
        self.add_message('JARVIS', f'Battery level is approximately {battery}%')

    elif 'memory' in cmd or 'log' in cmd:
        if self.memory:
            self.add_message('JARVIS', f"You've asked me to remember: {', '.join(self.memory)}")
        else:
            self.add_message('JARVIS', "I don't have anything in memory yet.")

    else:
        self.add_message('JARVIS', f"I'm not sure how to help with '{cmd}'. Try asking for time, date, battery, or memory.")

def run(self):
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']: 
                self.add_message('JARVIS', "Goodbye!")
                break
            self.process_command(user_input)
        except KeyboardInterrupt:
            self.add_message('JARVIS', "Session ended.")
            break

if name == "main": assistant = JarvisAI() assistant.run()

