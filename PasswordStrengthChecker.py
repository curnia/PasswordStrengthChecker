import re
import argparse


def password_complexity(password):
    """
    Analyze password complexity based on criteria such as length, uppercase/lowercase letters, numbers and special characters
    """
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_error = re.search(r"\W", password) is None
    password_ok = not (length_error or uppercase_error or lowercase_error or digit_error or special_error)

    return password_ok


def password_feedback(password):
    """
    Provide feedback to user on password strength and how to make it more secure
    """
    if password_complexity(password):
        return "Your password is strong. Keep it up!"
    else:
        feedback = "Your password is weak. Here's how you can make it more secure:\n"

        if len(password) < 8:
            feedback += "- Your password should be at least 8 characters long.\n"
        if re.search(r"[A-Z]", password) is None:
            feedback += "- Your password should contain uppercase letters.\n"
        if re.search(r"[a-z]", password) is None:
            feedback += "- Your password should contain lowercase letters.\n"
        if re.search(r"\d", password) is None:
            feedback += "- Your password should contain numbers.\n"
        if re.search(r"\W", password) is None:
            feedback += "- Your password should contain special characters.\n"

        return feedback


def main():
    parser = argparse.ArgumentParser(description='Password Strength Checker')
    parser.add_argument('password', help='Input the password to be analyzed')
    args = parser.parse_args()

    feedback = password_feedback(args.password)
    print(feedback)


if __name__ == '__main__':
    main()


