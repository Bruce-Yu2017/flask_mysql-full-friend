from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friends')

@app.route('/')
def index():
  query = "select * from friend"
  friend = mysql.query_db(query)
  print friend
  return render_template('full_friend.html', all_friends = friend)

@app.route('/friends', methods = ['POST'])
def create():
  query = "INSERT INTO friend (name, age) VALUES (:name, :age)"
  data = {
          'name': request.form['name'],
          'age': request.form['age']
         }
  mysql.query_db(query, data)
  return redirect('/')

app.run(debug=True)
