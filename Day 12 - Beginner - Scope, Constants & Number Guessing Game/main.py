# Video code - Namespaces: Local vs. Global Scope: 
player_health = 10      # vairable with global scope, not within a function
def health():
    health_potion = 2   # variable with local scope, not accessible outside this function

print(player_health)
# print(health_potion)

# Separating code - Does Python Have Block Scope?
# Python does not have block scope
# if a variable is created within an if-statement or while-loop it is accessible anywhere within the same function

enemies = ["Skeleteons", "Zombies", "aliens"]
level = 3
if level < 5:
    new_enemy = enemies[0]
print(new_enemy)


no_enemies = 1
def increase_enemies():
    global no_enemies       # it's a bad practice modify a vairbale with global scope within a function

    no_enemies += 1
    print(f"enemies inside the function {no_enemies}")
increase_enemies()
print(f"enemies outside the function {no_enemies}")

# Constants are variables that don't change throughout the program, the naming convention for defining constants is to use all UPPERCASE
PI = 3.14159
GOOGLE_URL = "https://www.google.com"
