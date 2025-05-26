# 🔐 Substitution Cipher Library (Python Homework)

This project is a Python library that:
- Encrypts and decrypts messages using a classic **substitution cipher**.
- Performs **automatic cryptanalysis** using bigram statistics and the **Metropolis-Hastings algorithm**.
- Demonstrates functionality in a Jupyter Notebook using real encrypted text samples.

---

## 📁 Project Structure
substitution_cipher/
├── cipher.py # Encryption and decryption
├── bigram_utils.py # Bigram generation and matrix
├── mh_cracker.py # Cipher breaking using M-H algorithm
├── export_utils.py # Export decrypted results to files
├── demo.ipynb # Jupyter Notebook demo (to be created)


---

## 🚀 How to Push Code to GitHub

Use these commands from the terminal in the root of your project:

```bash
git init
git remote add origin https://github.com/DavidovaNikola/PythonHomework.git
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
