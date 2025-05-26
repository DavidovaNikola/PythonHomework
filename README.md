
## 🚀 How to Push Code to GitHub

Use these commands from the terminal in the root of your project:

```bash
git init
git remote add origin https://github.com/DavidovaNikola/PythonHomework.git
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main


substitution_cipher/
│
├── test.ipynb ✅ (notebook)
├── sypher.py ✅ (šifrování a dešifrování)
├── bigram_utils.py ✅ (bigramy + plausibility)
├── mh_cracker.py ✅ (Metropolis-Hastings)
├── export_utils.py ✅ (uložení výsledků)
├── data/
│   └── reference_text.txt ✅ (dlouhý český text)
├── testovaci_soubory/
│   └── text_1000_sample_1_ciphertext.txt ✅ (od učitele)
└── output/ ✅ (automaticky vznikne)