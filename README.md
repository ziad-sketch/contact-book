
# 📒 Contact Book (Python Project)

## 📌 Overview
This is a simple command-line Contact Book application built using Python.  
It allows users to store, view, search, update, and delete contacts.  
All data is saved using a JSON file, so contacts are not lost after closing the program.

---

## 🚀 Features
- Add new contact (name + number)
- View all saved contacts
- Search for a contact
- Update existing contact
- Delete contact
- Automatic data saving using JSON

---

## 🛠️ Technologies Used
- Python 🐍
- JSON (for data storage)

---

## 📂 How It Works
Contacts are stored in a dictionary format:

```python
{
  "Ahmed": "0123456789",
  "Sara": "0109876543"
}
```

- Key → Contact name  
- Value → Phone number  

---

## ▶️ How to Run
1. Make sure Python is installed on your system
2. Download the project files
3. Run the program:

```bash
python main.py
```

---

## 📋 Menu Options
```
1 Add contact
2 View contacts
3 Search contact
4 Delete contact
5 Update contact
6 Exit
```

---

## 💡 Example Usage
```
Choose option: 1
Enter contact name: Ahmed
Enter contact number: 0123456789
Contact added
```

---

## ⚠️ Notes
- Data is stored in `contacts.json`
- Contacts are automatically saved after every change
- Do not delete the JSON file if you want to keep your data

---

## 📈 Future Improvements
- Add phone number validation
- Add GUI version using Tkinter
- Export contacts to CSV file
- Add contact groups (friends, work, etc.)

---

## 👨‍💻 Author
Beginner Python Project – built for learning and portfolio practice
```
