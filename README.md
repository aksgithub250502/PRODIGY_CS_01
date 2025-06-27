# Caesar Cipher - Cyber Security Internship (Task 01)

This is a simple implementation of the **Caesar Cipher**, one of the oldest and most well-known encryption techniques, developed as part of the **Prodigy InfoTech Cyber Security Internship**.

## 🔐 What is Caesar Cipher?

The **Caesar Cipher** is a **substitution cipher** where each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a shift of 3, `A` becomes `D`, `B` becomes `E`, and so on.

This implementation allows you to:
- **Encrypt** a plaintext message using a given shift.
- **Decrypt** an encrypted message using the same shift.

---

## 🧠 How it Works

- **Encryption** shifts each letter forward by the specified key (shift value).
- **Decryption** reverses this by shifting the letters backward using the same key.
- Special characters (like spaces, punctuation, numbers) remain unchanged.

---

## 🚀 How to Run

1. Run the program in a Python environment.
2. You will be prompted to:
   - Choose whether to **Encrypt (e)** or **Decrypt (d)**
   - Enter your **message**
   - Enter the **shift value** (an integer)

3. The result (encrypted or decrypted message) will be displayed.

---

## 🛠 Installation
### 1. Clone the Repository or Download the File
```bash
git clone https://github.com/aksgithub250502/PRODIGY_CS_01.git
```

## ▶️ How to Use
1. Open your terminal and navigate to the project directory:

```bash
   cd PRODIGY_CS_01
```

2. Run the script:

```bash
   python caesar_cipher.py
```

## 📦 Sample Usage

### Example 1: Encryption

```

Caesar Cipher Program
Do you want to Encrypt or Decrypt? (e/d): e
Enter your message: Hello! Welcome to Cyber Security!!
Enter shift value: 7

Encrypted message: Olssv! Dltjvtl av Jfily Zljbyapz!!

```

### Example 2: Decryption

```

Caesar Cipher Program
Do you want to Encrypt or Decrypt? (e/d): d
Enter your message: Olssv! Dltjvtl av Jfily Zljbyapz!!
Enter shift value: 7

Decrypted message: Hello! Welcome to Cyber Security!!

```

---

## 🛠️ Code Structure

- `encrypt(text, shift)` – Encrypts a message by shifting letters forward.
- `decrypt(text, shift)` – Decrypts a message by reversing the shift.
- `main()` – Handles user input and runs the program.

---
## 📸 Screenshots
> ![Caesar Cipher Program](https://github.com/user-attachments/assets/a33ed31f-d048-4646-bbe7-56ffa9e7ce0f)

> ![Caesar Cipher Output](https://github.com/user-attachments/assets/cdabafb5-a075-4428-a0c4-acdc79181b60)
ead5e93aa46)

---
## 📂 Project Structure

```

PRODIGY_CS_01/ 
├── caesar_cipher.py    #The main Python file containing the Caesar Cipher logic.
└── README.md           # Project documentation

```

---
## 👨‍💻 Author
**AMAN KUMAR SINGH**
* Cyber Security Intern – Prodigy InfoTech
* GitHub: [@aksgithub250502]**(https://github.com/aksgithub250502/)**
* Email - [aman.aks1402@gmail.com]

---
## ✅ Internship Task Completed

This project fulfills **Task 01: Implement Caesar Cipher** of the **Prodigy InfoTech Cyber Security Internship**.
