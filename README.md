# Package Sorting Function

This project implements a simple package sorting function for **Thoughtful’s robotic automation factory**.  
Packages are dispatched into one of three stacks depending on their size and weight.

---

## 📦 Rules

- A package is **bulky** if:
  - Its volume (Width × Height × Length) is **≥ 1,000,000 cm³**, OR
  - Any one dimension is **≥ 150 cm**.
- A package is **heavy** if:
  - Its mass is **≥ 20 kg**.
- Dispatch rules:
  - **STANDARD** → Not bulky and not heavy
  - **SPECIAL** → Bulky **or** heavy (but not both)
  - **REJECTED** → Bulky **and** heavy

---

## 🚀 How to Run

1. Clone/download the repository or copy the files into your project.
2. Make sure you have Python 3 installed.
3. Run the program:

```bash
python main.py
