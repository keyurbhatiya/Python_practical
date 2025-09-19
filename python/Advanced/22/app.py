from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flash messages

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'address_book_db'
}

# Function to connect to database
def get_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Initialize database and create table
def init_db():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS registrations (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                event_name VARCHAR(100) NOT NULL,
                registration_date DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        cursor.close()
        conn.close()

# Home route - Display all registrations
@app.route('/')
def index():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM registrations ORDER BY registration_date DESC')
        registrations = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('index.html', registrations=registrations)
    return render_template('index.html', registrations=[])

# Register for event
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        event_name = request.form['event_name']
        
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO registrations (name, email, event_name)
                    VALUES (%s, %s, %s)
                ''', (name, email, event_name))
                conn.commit()
                flash('Registration successful!')
            except Error as e:
                flash(f'Error during registration: {e}')
            finally:
                cursor.close()
                conn.close()
        return redirect(url_for('index'))
    return render_template('register.html')

# Cancel registration
@app.route('/cancel/<int:id>')
def cancel_registration(id):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM registrations WHERE id=%s', (id,))
            if cursor.rowcount > 0:
                conn.commit()
                flash('Registration cancelled successfully!')
            else:
                flash('Registration not found!')
        except Error as e:
            flash(f'Error cancelling registration: {e}')
        finally:
            cursor.close()
            conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()  # Initialize database when app starts
    app.run(debug=True)