# app.py
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

# Create table if not exists
def init_db():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100),
                phone VARCHAR(20),
                address TEXT
            )
        ''')
        conn.commit()
        cursor.close()
        conn.close()

# Home route - Display all contacts
@app.route('/')
def index():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM contacts')
        contacts = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('index.html', contacts=contacts)
    return render_template('index.html', contacts=[])

# Add new contact
@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO contacts (name, email, phone, address)
                    VALUES (%s, %s, %s, %s)
                ''', (name, email, phone, address))
                conn.commit()
                flash('Contact added successfully!')
            except Error as e:
                flash(f'Error adding contact: {e}')
            finally:
                cursor.close()
                conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

# Edit contact
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_contact(id):
    conn = get_db_connection()
    if not conn:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        
        try:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE contacts 
                SET name=%s, email=%s, phone=%s, address=%s 
                WHERE id=%s
            ''', (name, email, phone, address, id))
            conn.commit()
            flash('Contact updated successfully!')
        except Error as e:
            flash(f'Error updating contact: {e}')
        finally:
            cursor.close()
            conn.close()
        return redirect(url_for('index'))
    
    # GET request - show edit form
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts WHERE id=%s', (id,))
    contact = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('edit.html', contact=contact)

# Delete contact
@app.route('/delete/<int:id>')
def delete_contact(id):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM contacts WHERE id=%s', (id,))
            conn.commit()
            flash('Contact deleted successfully!')
        except Error as e:
            flash(f'Error deleting contact: {e}')
        finally:
            cursor.close()
            conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()  # Initialize database when app starts
    app.run(debug=True)