# 💳 Customer Transactions ETL Data Validation Project

## 📖 Description
This project focuses on validating **customer transaction data** between **source** and **target CSV files**.  
It ensures **data accuracy, completeness, and consistency** during ETL migration.  
Multiple test scenarios have been implemented using **Python** and **Pytest** to verify column structure, data types, and transaction integrity.

---

## 📂 Folder Structure
| Folder | Description |
|---------|--------------|
| `.vscode/` | VS Code configuration files |
| `data/` | Contains source and target CSV files |
| `tests/` | Includes the Python test script `test_source_target_validation.py` |

---

## ⚙️ Installation Steps
| Step | Command | Purpose |
|------|----------|----------|
| 1️⃣ | `git clone https://github.com/SushmitaETL/Myfirstproject.git` | Clone the repository from GitHub |
| 2️⃣ | `pip install -r requirements.txt` | Install required Python packages |
| 3️⃣ | `pip install pytest` | Install Pytest for running automated tests |
| 4️⃣ | `git init` & `git remote add origin <repo-url>` | Initialize and connect to GitHub repository |

---

## 🚀 Usage
Run all test scenarios using:
```bash pytest -v

## 🧪 Test Scenarios
| No. | Scenario Name | Description |
|-----|----------------|-------------|
| 1️⃣ | Column Validation | Ensures column names in source and target files match exactly. |
| 2️⃣ | Data Type Validation | Confirms each column’s data type is consistent between source and target. |
| 3️⃣ | Positive Amount Validation | Checks that all transaction amounts are positive and valid. |

---

## 🧠 Technologies Used
| Technology | Purpose |
|-------------|----------|
| Python | Core programming language for ETL validation logic |
| Pandas | Used for reading and manipulating CSV data |
| Pytest | Framework for writing and executing automated test cases |

---

## 🔍 Assert Keyword Explanation
The `assert` keyword is used to **verify test conditions**.  
If the condition evaluates to `True`, the test passes; if `False`, Pytest raises an **AssertionError**.  
Example:
```python
assert expected_columns == actual_columns, "Column mismatch between source and target"


Sushmita  
Data Quality Engineer  
Focused on ETL automation testing and data validation using Python and GCP.