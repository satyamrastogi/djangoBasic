
from flask import Flask, render_template, request, redirect
# from flask_mysqldb import MySQL
# import yaml
import numpy as np
import cv2
from capturevideo import importFunction as iF
# import MySQLdb
app = Flask(__name__)


@app.route('/')
def hello():
     return render_template('index.html')

# @app.route("/reg", methods=['GET', 'POST'])
# def reg():

#     name = request.form['name']
#     roll = request.form['roll']
#     email = request.form['email']
#     collegename = request.form['collegename']
#     branch = request.form['branch']
#     qualification = request.form['qualification']
#     mobile = request.form['mobile']

#     db = MySQLdb.connect(user='root', password='', host='localhost', database='myfirst')
#     query = "INSERT INTO registration(name,roll,email,collegename,branch,qualification,mobile) VALUES(%s, %s, %s, %s, %s, %s, %s)"
#     val = (name, roll, email, collegename, branch, qualification, mobile)
#     ob = db.cursor()
#     ob.execute(query, val)
#     db.commit()
#     ob.close()
#     return render_template("thankyou.html")


# @app.route('/student')
# def users():
#     cur = MySQLdb.connection.cursor()
#     resultValue = cur.execute("SELECT * FROM registration")
#     if resultValue > 0:
#         userDetails = cur.fetchall()
#         return render_template('student.html',userDetails=userDetails)



@app.route('/instructions')
def ins():
    cap=cv2.VideoCapture(0)
    fourcc=cv2.VideoWriter_fourcc(*'XVID')
    out=cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while (cap.isOpened()):
        ret, frame=cap.read()
        if ret == True:
            frame=cv2.flip(frame, 180)
            out.write(frame)

            # cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

@app.route('/demoTest')
def demoTest():
    pass
    iF()


if __name__ == '__main__':
    app.run(debug=True)
