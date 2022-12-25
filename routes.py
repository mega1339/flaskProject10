from app import app, db
from flask import request, render_template
from models import User


poluheno = '', '', '', ''


def check(mail, login, password, pass_def):

   r = "%$#@&*^|\/~[]{}"
   d = "QWERTYUIOPASDFGHJKLZXCVBNM"
   p = "qwertyuiopasdfghjklzxcvbnm"
   l = "_"
   f = "1234567890"

   flag1 = 0
   flag2 = 0
   flag3 = 0
   flag4 = 0


   if len(password) < 8:
       print("not password1")
       return False

   for i in password:
       if i not in d:
           flag1 += 1
       if flag1 == len(password):
           print("not password2")
           return False

   for i in password:
       if i not in p:
           flag2 += 1
       if flag2 == len(password):
           print("not password3")
           return False

   for i in password:
       if i not in f:
           flag3 += 1
       if flag3 == len(password):
           print("not password4")
           return False

   for i in password:
       if i not in r:
           flag4 += 1
       if flag4 == len(password):
           print("not password5")
           return False


   if not '@' in mail:
       print('not mail')
       return False


   if len(login) < 6:
       print('not login')
       return False
   if (login[0] not in p) and (login[0]not in d):
       print('not login2')
       return False
   for i in (login):
       if (i not in l) and (i not in f) and (i not in p) and (i not in d):
           print('not login3')
           return False


       if pass_def != password:
           print("not password_def")
           return False

   return True


@app.route('/', methods=['GET', 'POST'])
def create_user():
   result = "Введите данные"
   if request.method == "POST":
       global poluheno

       email = request.form.get("Data_email")
       login = request.form.get("Data_login")
       password = request.form.get("Data_pass")
       pass_def = request.form.get("Data_pass_def")

       poluheno = email, login, password

       user_test_mail = User.query.filter_by(email=poluheno[0]).first()
       user_test_login = User.query.filter_by(login=poluheno[1]).first()

       if check(email, login, password, pass_def) and user_test_login == None and user_test_mail == None and poluheno[0] != '':
           User.add(poluheno[0],
                    poluheno[1],
                    poluheno[2])
           result = "Аккаунт создан"
       else:
           result = "Неудовлетворяет требованиям"
   res = db.engine.execute('SELECT * FROM user;')

   return render_template("try.html", table=res, result=result)



@app.route('/login', methods=['GET', 'POST'])
def login():
   result1 = "Введите логин и пароль"
   if request.method == "POST":

       login = request.form.get("Data_login")
       password = request.form.get("Data_pass")

       user_test_login = User.query.filter_by(login=login).first()
       user_test_password = User.query.filter_by(password=password).first()

       if user_test_login == None and user_test_password == None:
           result1 = "Не существует такого пользователя"
       else:
           result1 = "Успешно!"

   return render_template("nby.html", result1=result1)
