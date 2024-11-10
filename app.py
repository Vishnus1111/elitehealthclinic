from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# Function to establish database connection
def get_database_connection():
    return mysql.connector.connect(
        user='root',
        password='Varutaru@2013',
        host='localhost',
        database='elite_health_clinic'
    )

@app.route('/')
def index():
    return render_template('clinic_home.html')
@app.route('/home')
def home():
    return render_template('clinic_home.html')
@app.route('/about')
def about():
    return render_template('clinic_about.html')
@app.route('/doctors')
def doctors():
    return render_template('clinic_doctors.html')
@app.route('/contacts')
def contacts():
    return render_template('clinic_contacts.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/appointment')
def appointment():
    return render_template('appointment.html')


@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Get data from form
    idpatient = request.form.get('idpatient')
    p_name = request.form.get('p_name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    dob = request.form.get('dob')
    address = request.form.get('address')
    gender = request.form.get('gender')

    # Insert form data into database
    try:
        conn = get_database_connection()
        cursor = conn.cursor()

        add_user = ("INSERT INTO patient (idpatient, p_name, phone, email, dob, address, gender) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        cursor.execute(add_user, (idpatient, p_name, phone, email, dob, address, gender))
        conn.commit()

        return render_template('success.html')

    except mysql.connector.Error as err:
        return f"Error: {err}"

    finally:
        cursor.close()
        conn.close()

@app.route('/book_form', methods=['POST'])
def book_form():
    # Get data from form
    p_id = request.form.get('p_id')
    d_id = request.form.get('d_id')
    cases = request.form.get('cases')
    day = request.form.get('day')
    time = request.form.get('time')

    # Insert form data into database
    try:
        conn = get_database_connection()
        cursor = conn.cursor()

        book_user = ("INSERT INTO appointment (p_id, d_id, cases, app_date, app_time) VALUES (%s, %s, %s, %s, %s)")
        cursor.execute(book_user, (p_id, d_id, cases, day, time))
        conn.commit()

        return render_template('success1.html')

    except mysql.connector.Error as err:
        return f"Error: {err}"

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
