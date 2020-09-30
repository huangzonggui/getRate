import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="12CCCCXXX0085"    #用户名
mail_pass="XXXXXXX"   #口令 
 
sender = '1CCC20085@qq.com'
# sender = 'genius'
# receivers = ['sam.chan@megadatatech.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
receivers = ['1XXX0085@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

def send(_rate, _rateTableHtml):
    # MIMEText('匯率夠高啦，匯率是：'+str(_rate), 'plain', 'utf-8') 
    _str = '<div>匯率夠高啦，匯率是：'+str(_rate)+'</div>'
    message = MIMEText(_str + str(_rateTableHtml), 'html', 'utf-8')
    message['From'] = Header("genius", 'utf-8')
    message['To'] =  Header("someone who want to know", 'utf-8')
    
    subject = '換錢啦'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as err:
        print("Error: 无法发送邮件:" + err)