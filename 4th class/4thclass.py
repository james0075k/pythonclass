#to determine the height of person according to 
def determine_height(age):
    if age < 10:
        return "Child: Height is approximately 4 feet."
    elif 10 <= age < 18:
        return "Teenager: Height is approximately 5 to 5.5 feet."
    else:
        return "Adult: Height is approximately 5.5 to 6 feet."