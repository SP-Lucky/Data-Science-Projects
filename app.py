from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Thecloud@1234",
    database="test"
)
mycursor = mydb.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        id = request.form['id']
        company = request.form['company']
        amount = request.form['amount']
        payment_date = request.form['payment_date']
        status = request.form['status']
        due_date = request.form['due_date']
        
        # Insert data into the userdata table
        sql = "INSERT INTO userdata (id, company, amount, payment_date, status, due_date) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (id, company, amount, payment_date, status, due_date)
        mycursor.execute(sql, val)
        mydb.commit()
        return 'Data successfully submitted to the database'


@app.route('/summary')
def summary():
    mycursor.execute("SELECT * FROM userdata")
    data = mycursor.fetchall()
    return render_template('summary.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

