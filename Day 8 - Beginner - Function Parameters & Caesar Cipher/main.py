# Video code - Functions with Inputs:
def greet():
    print("Hello")
    print("Welcome to the program")
    print("Hope you are well")

greet()

def greet_name(name):
    print(f"Hello {name}")
    print(f"Welcome to the program {name}")

greet_name("Mohammed")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is the weather like in {location}?")

greet_with("Mohammed", "Saudi Arabia")      # using positional arguments
greet_with(name="Yusuf", location="Nowhere")        # using keyword arguments

