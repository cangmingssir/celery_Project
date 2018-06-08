from flask import Flask

import tasks
from ext import init_mail

app = Flask(__name__)
app.debug=True
app.env='development'
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_USERNAME'] = 'mu_tongwu@163.com'
app.config['MAIL_PASSWORD'] = 'wupeng109321'

init_mail(app)

@app.route('/regist/<name>/<email>')
def regist(name,email):
    print('注册用户',name,email)

    #发送邮件
    tasks.sendMsg.delay(email,'恭喜你,您没钱了.....')
    return '<h3>{}用户注册成功，请及时激活邮箱{}</h3>'.format(name,email)


if __name__ == '__main__':
    app.run()
