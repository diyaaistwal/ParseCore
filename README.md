# 📦 LR Parser for Source Code Analysis: A Compiler Front-End Tool

## 📌 Project Overview
This project is a compiler front-end tool that implements an **LR parser (LALR(1))** for a simplified programming language. It includes **lexical analysis**, **parsing**, **error detection**, a **command-line interface**, and a complete **GUI-based parse tree visualizer** for real-time feedback and debugging.

---

## 👨‍💻 Team: ParseCore

- **Diya Istwal** (Team Lead) – Coordination, Testing, Integration  
- **Divyansh Chauhan** – Parser Implementation, Tree Logic  
- **Ayush Chaudhary** – Lexer, Token Definitions  
- **Ishaan Chauhan** – CLI Integration, GUI Development  

---

## 🛠️ Technologies Used

- Python 3.x  
- PLY (Python Lex-Yacc)  
- Tkinter (GUI)  
- Matplotlib / NetworkX (Tree Visualization)  
- Command-Line Interface  

---

## 📁 Project Structure

LR_Parser_Project/
│
├── lexer.py # Lexical analyzer (tokenizer)
├── parser.py # LALR(1) grammar and parse rules
├── main.py # CLI interface and integration
├── gui.py # Parse tree visualization (Tkinter)
├── examples/ # Sample expressions and inputs
├── assets/ # Screenshots and assets for README
└── README.md # This file

---

## ✅ Features Implemented

- Grammar and tokens for arithmetic expressions  
- Lexical analysis using **PLY**  
- LALR(1) parsing rules with proper precedence  
- Real-time syntax and token error detection  
- CLI-based expression parsing with result evaluation  
- Fully working **GUI with:**
  - Parse tree visualization  
  - Token display  
  - Evaluation result viewer  
  - Error diagnostics pane  
  - Animation speed control  

---

## 🖼️ Sample Parse Tree Visualization

![image](https://github.com/user-attachments/assets/1b037f3b-dee1-49dc-aabb-1ddcbee334c4)



> Expression: `2 + 3 * 4`  
> Result: **14.0**  
> The visualization shows operator precedence using a binary tree.

---

## 🧪 Sample CLI Test

![image](https://github.com/user-attachments/assets/a93f70b1-c489-4764-ab5e-8e3a14413016)



##  Phase 3 Achievements (✅ Completed)

✅ Parse tree visualization (Tkinter + Matplotlib/NetworkX)
✅ Live token stream and error diagnostics
✅ GUI integration with CLI backend
✅ Tree traversal animation
✅ User-friendly interface and result panel

##  📜 License

This project is developed under the Project-Based Learning (PBL) initiative at Graphic Era (Deemed to be) University for academic use only.

##  Acknowledgements

PLY Library by David Beazley
Python Tkinter Documentation
Our project mentors at GEU


