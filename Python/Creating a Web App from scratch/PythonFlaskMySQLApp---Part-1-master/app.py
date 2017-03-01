from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from passlib.hash import pbkdf2_sha512

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'test'
app.config['MYSQL_DATABASE_DB'] = 'bucketlist'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:
            
            # All Good, let's call MySQL
            print("Fields Detected")
            conn = mysql.connect()
            print("DB Connected")
            cursor = conn.cursor()
            _hashed_password = pbkdf2_sha512.encrypt(_password)
            query = ("insert into tbl_user(user_name, user_username, user_password)" \
                    "values ( %s , %s, %s)")
            data = (_name, _email, _hashed_password)
            cursor.execute(query, data)
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                print("Success")
                return json.dumps({'message':'User created successfully !'})
            else:
                print("Weird Failure")
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})

if __name__ == "__main__":
    app.run(port=5000)
