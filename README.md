# Smart Expense Tracker + Budget AI

Smart Expense Tracker is a Python-based tool that helps you track your income and expenses, categorize spending, and generate monthly visual reports. The project is perfect for personal finance management and demonstrates full-stack Python skills with data visualization and reporting.

---

## Features

- Record income and expenses with categories
- Generate monthly reports with summary tables
- Visualize spending via pie charts
- Export PDF reports including tables and charts
- Optional AI integration for budget suggestions
- Runs entirely on Ubuntu/Linux

---

## Prerequisites

- Ubuntu or Linux-based OS
- Python 3
- Required Python packages:
  - `sqlite3` (usually comes with Python)
  - `matplotlib`
  - `fpdf`
  - `tabulate`

Optional for AI suggestions:

- `openai` or any AI model package

---

## Installation

1. Update your system and install dependencies:

```bash
sudo apt update
sudo apt install python3-pip
pip3 install matplotlib fpdf tabulate
pip3 install openai   # optional, for AI-based suggestions
