# Defensive Cybersecurity Toolbox

An educational web application built with **Python (Flask)** and a modern, cyber‑themed **HTML/CSS** interface. This tool is designed to teach **secure coding practices** by demonstrating common web vulnerabilities (such as **SQL Injection** and **Cross‑Site Scripting**) side‑by‑side with their **defensive mitigations**.

---

## Key Features

* **OWASP Top 10 Focus**
  Current modules cover:

  * **A03: Injection (SQLi)**
  * **A07: Cross‑Site Scripting (XSS)**

* **Vulnerable vs. Secure Demonstrations**
  Execute real‑world style attacks against vulnerable code and instantly observe how secure implementations prevent exploitation.

* **Prepared Statements Demo**
  Interactive demonstration showing how **parameterized queries** block SQL Injection attacks.

* **Output Encoding Demo**
  Interactive demonstration showing how **auto‑escaping and output encoding** prevent XSS.

* **Futuristic UI**
  Dark‑themed, high‑contrast cyber interface for an engaging learning experience.

---

## Setup and Installation

Follow the steps below to run the project locally.

### Prerequisites

* **Python 3.x**
* **pip** (Python package installer)

---

### 1️⃣ Clone or Download the Project

(Assuming your project folder is named `TOOLBOX_DASHBOARD`)

---

### Create and Activate a Virtual Environment

Using a virtual environment is **highly recommended**.

```bash
# Create the virtual environment
python -m venv venv

# Activate on Linux / macOS
source venv/bin/activate

# Activate on Windows
# venv\Scripts\activate
```

---

### Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

---

### Run the Application

From the project root directory:

```bash
python app.py
```

---

### Access the Toolbox

Open your browser and navigate to:

```
http://127.0.0.1:5000/
```

---

## Project Structure

The project follows standard **Flask** conventions:

```
TOOLBOX_DASHBOARD/
├── app.py                  # Main Flask application logic
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── defensive_db.sqlite     # SQLite DB for SQLi demo (created on first run)
├── static/
│   └── style.css           # Cyber‑themed futuristic styling
└── templates/
    ├── index.html          # Main dashboard
    ├── result.html         # SQL Injection demo results
    └── xss_result.html     # XSS demo results
```

---

## How to Use the Demos

### SQL Injection (OWASP A03)

**Target:** Vulnerable Login Form

**Payload:**

```
' OR 1=1 --
```

*(Note the leading space before the comment)*

**Expected Result (Vulnerable):**
Authentication is bypassed and sensitive data (e.g., the `admin` user's secret) is revealed.

**Expected Result (Secure):**
The attack fails because user input is treated as **data**, not executable SQL.

---

### Cross‑Site Scripting (XSS) (OWASP A07)

**Target:** Vulnerable Comment Form

**Payload:**

```html
<script>alert('XSS Attack!')</script>
```

**Expected Result (Vulnerable):**
A JavaScript alert executes in the browser, proving client‑side code injection.

**Expected Result (Secure):**
The script is rendered as harmless text, demonstrating effective **output encoding**.

---

## Contribution

This is an **educational project**.

You are encouraged to extend it by adding more OWASP Top 10 modules, such as:

* Broken Access Control
* Security Misconfiguration
* Identification & Authentication Failures
* Insecure Design

Each new module should include:

* A vulnerable implementation
* A secure implementation
* Clear explanation of the defense mechanism

---

**Built for learning, defense, and awareness.**
