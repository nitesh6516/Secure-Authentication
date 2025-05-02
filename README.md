Secure Authentication Module
A CLI-based secure authentication system developed as part of CSE 316 - Operating Systems coursework. This Python-based project implements multi-factor authentication (MFA), account lockout mechanisms, and encrypted password storage using industry-standard libraries.

🔐 Features
Secure CLI Login using username and password

Multi-Factor Authentication (MFA) with OTP (simulated)

Password Encryption using bcrypt with salting

Account Lockout after 3 failed login attempts

Masked Password Input for secure credential entry

Simulated OTP Delivery for MFA testing

Modular design for future integration with:

Vulnerability scanner

System monitor

Web dashboard (Flask/Django compatible)

🛠️ Technologies Used
Language: Python 3.9+

Libraries:

bcrypt – Password hashing

json – Lightweight data storage

getpass – Secure input handling

random, string – OTP generation

os – File system interaction

Tools: Git, GitHub, Visual Studio Code

📋 Core Modules Overview
Module	Description
register()	Registers users with encrypted passwords
login()	Authenticates users with MFA and lockout logic
generate_otp()	Creates a 6-digit OTP
simulate_otp_send()	Simulates OTP delivery for testing
get_secure_password()	Handles secure password input
main()	CLI interface for user interaction

🧠 System Workflow
User Registration with secure password hashing.

Login Attempt:

Verify username and password.

Send simulated OTP.

Validate OTP.

Track failed login attempts.

Lock account after 3 failures.

🔮 Future Enhancements
Real OTP delivery via email or SMS

Web-based interface for user/admin control

Integration with relational databases (e.g., PostgreSQL)

Real-time threat detection and logging

Support for advanced protocols (FIDO2, WebAuthn)

📁 File Structure
bash
Copy
Edit
Secure-Authentication/
├── users.db          # JSON-based user database
├── auth_module.py    # Main Python authentication code
└── README.md         # Project overview
🧑‍💻 Contributors
Hritik Kumar – 12317140

Nitesh Kumar – 12323263

Aditya Choudhary – 12321604
Under guidance of Dr. Richa Sharma

📎 GitHub Repository