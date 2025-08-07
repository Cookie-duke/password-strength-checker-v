import re

def load_common_passwords():
    with open('common_passwords.txt', 'r') as f:
        return set(p.strip() for p in f.readlines())

def check_strength(password, common_passwords):
    if password in common_passwords:
        return "Very Weak - Commonly used password!"

    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?":{}|<>]", password):
        score += 1

    feedback = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Extremely Weak"
    }

    return feedback.get(score, "Invalid")

if __name__ == "__main__":
    common_passwords = load_common_passwords()
    password = input("Enter a password to check: ")
    result = check_strength(password, common_passwords)
    print(f"Password Strength: {result}")
