# 🔐 Secure Authentication Module for Operating Systems (Python CLI)

This project is a **secure, command-line-based authentication module** designed to simulate OS-level access control using **multi-factor authentication (MFA)**. It focuses on safe credential handling, OTP-based MFA, and protection against brute-force attacks.

---

## 📌 Features

- ✅ User Registration with bcrypt password hashing
- ✅ Secure Login with OTP verification (MFA)
- ✅ Account lockout after multiple failed login attempts
- ✅ Input hiding for passwords (`getpass`)
- ✅ Cross-platform CLI (Linux, Windows, macOS)
- ✅ Minimal dependencies & easy to set up

---

## 🛠️ Technologies Used

| Purpose                | Tool / Library     |
|------------------------|--------------------|
| Language               | Python 3.x         |
| Password Hashing       | `bcrypt`           |
| Input Hiding           | `getpass`          |
| OTP Generation         | `random`, `string` |
| Data Storage           | JSON File          |

---

## 🚀 How to Run the Project

### 1. 📥 Clone the Repository

```bash
git clone https://github.com/your-username/SecureAuthOS.git
cd SecureAuthOS
