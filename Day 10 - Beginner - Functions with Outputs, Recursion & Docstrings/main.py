# Day 10 - Functions with outputs:
# Video code - Functions with Outputs:

def format_name(f_name, m_name, l_name):
    """Takes the first middle and last names and capitlizes the first letter if each"""
    if f_name == "" or m_name == "" or l_name == "":
        return "You didn't enter your name"     # function with multiple with multiple returns

    formatted_f_name = f_name.title()
    formatted_m_name = m_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_m_name} {formatted_l_name}"

print(format_name(input("What is your first name? "), input("What is your middle name? "), input("What is your last name? ")))
