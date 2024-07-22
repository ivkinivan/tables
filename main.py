from flask import Flask, render_template, request, flash
from functions import sendEmail

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'asdfashjdashdgvasduaertyui'

mail = 'codium@bk.ru'

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        tel = request.form.get('telephone')
        message = request.form.get('message')
        sendEmail(mail, render_template('mail.html', name = name, telephone = tel, message = message), "Новая заявка")
        flash('Заявка отправлена')
    return render_template('index.html')

