# 🧩 Python Modules & Packages — Exercise: Library Management System

This small project is designed to help you practice how to:

- Structure your Python code using **modules** and **packages**
- Define and use a **class with methods**
- Import your custom module (`mylibrary`) in another file (`main.py`)

---

## 💡 What to Learn Here

- How to define a class (`Library`) with multiple methods (`add_book`, `remove_book`, `list_books`, etc.)
- How to split code across multiple files for better organization
- How to import your own modules and call their functions/methods
- How to build and install a local package

---

## 📁 Structure Overview

06-modules/
│
├── mylibrary/ # Package containing the Library class
│ ├── init.py
│ └── library.py
│
├── main.py # Entry point script using the Library class
├── pyproject.toml # Project and build configuration

---

## 🚀 How to Run

You can run the program using:

```bash
python main.py
```
This script creates an instance of your Library class and allows users to add, remove, list, or search for books through a simple terminal interface.

## 📦 Bonus: Building the Package (Optional)

If you're curious, you can build and install the package locally to test how Python packaging works.

``` bash
python -m build
pip install -e .
```

### ✅ Tips for Viewers

* Try adding your own methods to the Library class!
* Use this structure as a pattern for future small projects.
* Notice how separating logic (in library.py) from interface (in main.py) makes your code cleaner.

