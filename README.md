# 🛡️ Project Title: Python File Encryptor/Decryptor Utility

**Project by:** martincalta1539

---

## 🎯 Purpose and Ethical Use

This software is provided **strictly for educational purposes, simulations, and data security research**. The primary goal is to demonstrate the principles of symmetric data encryption within a folder structure and support ethical research in cybersecurity.

**❌ Prohibition of Misuse (Anti-Abuse Clause):**
* **It is strictly forbidden** to use this code for the development, testing, or execution of **actual malware** or for carrying out **unauthorized actions** against third-party systems.
* **Violation of this ethical code** constitutes a breach of the MIT License and applicable laws.

---

## ⚠️ Security Warning (Extended)

**!!! EXTREME CAUTION IS REQUIRED !!!**

* **Never run** these scripts (`encrypt.py`, `decrypt.py`) on a computer containing sensitive data you cannot afford to lose. Always use an **isolated testing environment (sandbox) or a Virtual Machine (VM)**.
* **IMPORTANT:** The code encrypts **all data in the current directory and all its subdirectories**.
* **THE KEY:** The file **`thekey.key`** is the critical encryption key. **DO NOT DELETE** it and **NEVER share it publicly**. Data cannot be decrypted without this key! (We recommend backing up the key to a safe, offline location after testing).

---

## ⚙️ Requirements and Installation

This project requires Python 3.x and the necessary libraries (e.g., `cryptography`).

1.  **Create a Virtual Environment** (Recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/macOS
    .\venv\Scripts\activate   # For Windows
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(**Note:** This assumes you have a `requirements.txt` file listing all required libraries).*

---

##  How to Use

For correct operation, **all files** (`encrypt.py`, `decrypt.py`, and `thekey.key`) must be in the same folder.

### 1. Key Generation (If Key is Missing)

If the `thekey.key` file does not exist, you must generate it first (Please detail this step if your code includes a key generation feature).

### 2. Encrypt

Initiates the encryption of files in the current folder and subfolders.

```bash
python encrypt.py