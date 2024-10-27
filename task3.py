import re

def check_password_strength(password):
    # Initialize score
    score = 0
    feedback = []
    
    # Check password length
    if len(password) >= 12:
        score += 2
        feedback.append("Password length is sufficient.")
    elif 8 <= len(password) < 12:
        score += 1
        feedback.append("Password length is moderate, consider making it longer.")
    else:
        feedback.append("Password is too short. Use at least 8 characters.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("Contains uppercase letters.")
    else:
        feedback.append("Add uppercase letters for better security.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("Contains lowercase letters.")
    else:
        feedback.append("Add lowercase letters for better security.")

    # Check for numbers
    if re.search(r"[0-9]", password):
        score += 1
        feedback.append("Contains numbers.")
    else:
        feedback.append("Add numbers for better security.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        feedback.append("Contains special characters.")
    else:
        feedback.append("Add special characters for better security.")
    
    # Determine password strength level based on score
    if score >= 6:
        strength = "Strong"
    elif 4 <= score < 6:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    # Display feedback
    print("Password Strength:", strength)
    print("Feedback:")
    for item in feedback:
        print("- " + item)

# Example usage
password = input("Enter a password to check its strength: ")
check_password_strength(password)
