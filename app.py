from flask import Flask, render_template, jsonify
from db_connect import get_db_connection
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/test')
def test():
    return "render_template('login.html')"


@app.route('/test0')
def test00():
    db = get_db_connection()
    curs = db.cursor()
    curs.execute("""CREATE TABLE Customers (CustomerName varchar(255), ContactName varchar(255),FirstName varchar(255),Address varchar(255),City varchar(255));""")
    curs.execute("""INSERT INTO Customers (CustomerName, ContactName, Address, City)
VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger');""")
    curs.execute("""SELECT * FROM Customers""")
    data_test = curs.fetchall()
    db.commit()
    curs.close()
    db.close()
    return jsonify(msg=data_test)


if __name__ == '__main__':
    app.run()
