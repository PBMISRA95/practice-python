# Python Practice Repository

A comprehensive collection of Python programming exercises, practice problems, and learning projects. This repository serves as a personal learning journey and reference for Python programming concepts.

##  Repository Structure

### Practice Sections

#### **practicepython/**
Solutions to exercises from [PracticePython.org](https://www.practicepython.org)
- `Ex1.py` - Calculate year when user turns 100
- `Ex2.py` - Check if number is odd/even and divisibility
- `Ex3.py` - Filter list elements less than given number
- `Ex4.py` - Find all divisors of a number
- `Ex5.py` - Find common elements between two lists
- `Ex6.py` - Check if string is palindrome
- `Ex7.py` - List comprehension for even numbers

#### **incedo_questions/**
Interview preparation questions and solutions (Questions 1-30)
- **q1_q10/** - Basic string, list, and number operations
  - String reversal, sum calculations, palindrome checks
  - Duplicate removal, word frequency, list joining
  - Factorial, vowel counting, max value finding
- **q11_q20/** - Intermediate algorithms
  - Character counting, list rotation, dictionary sorting
  - Square odds with list comprehensions
  - Average calculations with None handling
- **practice_days/** - Daily practice sessions organized by date
  - 10-oct/ - October practice notebooks
  - 11-nov/ - November practice notebooks

#### **play/**
Experimental scripts and mini-projects
- `calculator.py` - Simple calculator with basic operations
- `Car_game(Mosh).py` - Interactive car control game
- `list_play.py` - Experiments with lists and loops

#### **fastapi/**
FastAPI learning and API development
- `firstapp.py` - Basic FastAPI application with math operations

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.11+
```

### Installation
1. Clone the repository:
```bash
git clone https://github.com/PBMISRA95/practice-python.git
cd practice-python
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Dependencies
The project uses the following packages (see `requirements.txt`):
- **Data Science**: `numpy`, `pandas`, `scipy`, `scikit-learn`, `matplotlib`
- **Deep Learning**: `torch`, `torchvision`, `torchaudio`
- **NLP**: `transformers`, `datasets`, `accelerate`, `peft`
- **Development**: `jupyterlab`, `ipykernel`

## 📚 Key Topics Covered

- **String Manipulation**: Reversing, palindromes, character counting
- **List Operations**: Comprehensions, filtering, rotation, duplicate removal
- **Algorithms**: Factorial, prime numbers, GCD/LCM, Fibonacci
- **Data Structures**: Dictionaries, frequency counting, sorting
- **Functional Programming**: Lambda functions, map/filter operations
- **User Interaction**: Input handling, game logic

## 🛠️ Development Tools

### Code Quality
- **Black**: Code formatting (100 char line length)
- **isort**: Import sorting
- **Flake8**: Linting
- **Pylint**: Additional code analysis
- **Pre-commit hooks**: Automated quality checks

### Setup Pre-commit Hooks
```bash
pre-commit install
```

## 📖 Usage Examples

### Run a practice exercise:
```bash
python practicepython/Ex7.py
```

### Run interview question solution:
```bash
python incedo_questions/q1_q10/q1_string_reverse.py
```

### Start FastAPI server:
```bash
cd fastapi
uvicorn firstapp:app --reload
```

### Open Jupyter notebooks:
```bash
jupyter lab
# Navigate to incedo_questions/q1_q10/main.ipynb
```

## 📝 Practice Questions Reference

Quick access to question categories:
- **Q1-Q10**: Basic operations (questions.txt)
- **Q11-Q20**: Intermediate algorithms
- **Q21-Q30**: Advanced problems

## 🤝 Contributing

This is a personal learning repository, but suggestions and improvements are welcome!

## 📜 License

This project is for educational purposes.

## 🔄 Version Control

- **Platform**: GitHub
- **IDE**: Visual Studio Code
- **Project Management**: Trello Board (coordinated)

## 📅 Timeline

- **Started**: July 23, 2020
- **Active Development**: Ongoing
- **Last Updated**: November 2025

---

**Note**: This repository represents my learning journey in Python programming, from basics to advanced concepts including web APIs, data science, and machine learning.
