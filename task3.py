import re

def assess_password_strength(password):
    """
    Assess the strength of a password based on several criteria.
    """
    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Calculate the score
    score = 0
    if length_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_criteria:
        score += 1
    
    # Assess strength based on score
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    return strength, score

def main():
    print("Password Strength Assessment Tool")
    password = input("Enter a password to assess: ").strip()
    strength, score = assess_password_strength(password)
    print(f"Password strength: {strength} (Score: {score}/5)")
    print("Criteria for a strong password:")
    print("- At least 8 characters long")
    print("- Contains uppercase letters")
    print("- Contains lowercase letters")
    print("- Contains digits (0-9)")
    print("- Contains special characters (!@#$%^&*(),.?\":{}|<>)")

if __name__ == "__main__":
    main()
