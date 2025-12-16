from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
DB_NAME = 'defensive_db.sqlite'

# --- Setup: Initialize a simple database for demonstration ---
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Create a table and insert dummy data
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, secret TEXT)")
    cursor.execute("INSERT INTO users (username, secret) VALUES ('admin', 'Th3Secr3tK3y')")
    cursor.execute("INSERT INTO users (username, secret) VALUES ('alice', '12345')")
    conn.commit()
    conn.close()

# --- 2. VULNERABLE FUNCTION (DO NOT USE IN REAL APPS) ---
@app.route('/vulnerable_login', methods=['POST'])
def vulnerable_login():
    # This simulates a typical user input where the data is concatenated directly into the query
    user_input = request.form.get('username')

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # VULNERABLE: String concatenation is dangerous
    query = "SELECT secret FROM users WHERE username = '" + user_input + "';"
    
    try:
        # Example: Input of ' OR 1=1 --
        cursor.execute(query)
        result = cursor.fetchone()
        
        if result:
            return f"<h1>Vulnerable Login Success!</h1><p>Query Executed: <code>{query}</code></p><p>Secret Found: <strong>{result[0]}</strong></p>"
        else:
            return f"<h1>Vulnerable Login Failed!</h1><p>Query Executed: <code>{query}</code></p><p>No user found.</p>"
    except Exception as e:
        return f"<h1>Vulnerable Login Error!</h1><p>Error: {e}</p>"
    finally:
        conn.close()

# --- 3. SECURE FUNCTION (MITIGATION) ---
@app.route('/secure_login', methods=['POST'])
def secure_login():
    user_input = request.form.get('username')

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # SECURE: Using a Prepared Statement (parameterized query)
    # The input '?' is a placeholder; the database driver handles sanitation.
    query = "SELECT secret FROM users WHERE username = ?;"

    try:
        # Pass the input as a separate tuple/list of parameters
        cursor.execute(query, (user_input,))
        result = cursor.fetchone()
        
        if result:
            # Note: Even with ' OR 1=1 --' input, the query ONLY looks for a username literally named that.
            return f"<h1>Secure Login Success!</h1><p>Query Executed (Sanitized): <code>{query}</code></p><p>Secret Found: <strong>{result[0]}</strong></p>"
        else:
            return f"<h1>Secure Login Failed!</h1><p>Query Executed (Sanitized): <code>{query}</code></p><p>No user found with that literal username.</p>"
    except Exception as e:
        return f"<h1>Secure Login Error!</h1><p>Error: {e}</p>"
    finally:
        conn.close()

# --- 4. VULNERABLE XSS FUNCTION ---
@app.route('/vulnerable_xss', methods=['POST'])
def vulnerable_xss():
    # VULNERABLE: Retrieves user input and passes it straight to the template
    user_comment = request.form.get('comment')
    # The vulnerability will be exposed when the template renders this raw string
    return render_template('xss_result.html', 
                           status_class="vulnerable", 
                           title="Vulnerable Comment Posted", 
                           comment=user_comment)

# --- 5. SECURE XSS FUNCTION (MITIGATION) ---
@app.route('/secure_xss', methods=['POST'])
def secure_xss():
    user_comment = request.form.get('comment')
    
    # SECURE: The mitigation here is in the template (Jinja2 auto-escaping) 
    # and the developer practice of NEVER using the ' | safe ' filter.
    # For a full example, a library like Bleach would be used for sanitization.
    
    # We will demonstrate the defense by relying on Jinja2's powerful AUTO-ESCAPING feature.
    # Jinja2 automatically converts '<' to '&lt;' and '>' to '&gt;' by default.
    return render_template('xss_result.html', 
                           status_class="secure", 
                           title="Secure Comment Posted", 
                           comment=user_comment)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    init_db()  # Initialize DB on startup
    app.run(debug=True)