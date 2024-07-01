# SCT_CYS_3
Build a tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters.

## Password Strength Assessment Tool
This repository contains a simple tool to assess the strength of a password based on several criteria, such as length, use of uppercase and lowercase letters, digits, and special characters.

### Features

- Assess the strength of a password based on the following criteria:
  - At least 8 characters long
  - Contains uppercase letters
  - Contains lowercase letters
  - Contains digits (0-9)
  - Contains special characters (!@#$%^&*(),.?":{}|<>)
- Provides a score and a strength level (Very Weak, Weak, Moderate, Strong, Very Strong).

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/password-strength-assessment-tool.git
    cd password-strength-assessment-tool
    ```

### Usage

1. **Run the script**:
    ```bash
    python task3.py
    ```

2. **Follow the prompts**:
    - Enter the password you want to assess.
    - The tool will display the strength and score of the password.

### Example

```bash
Password Strength Assessment Tool
Enter a password to assess: MyP@ssw0rd!
Password strength: Very Strong (Score: 5/5)
Criteria for a strong password:
- At least 8 characters long
- Contains uppercase letters
- Contains lowercase letters
- Contains digits (0-9)
- Contains special characters (!@#$%^&*(),.?":{}|<>)
```

### Functions

- **assess_password_strength(password)**:
  - Assess the strength of a password based on several criteria.
  - Parameters:
    - `password`: The password to be assessed.
  - Returns:
    - A tuple containing the strength description (e.g., Very Strong) and the score (out of 5).
