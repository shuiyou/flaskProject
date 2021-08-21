import os
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

mailSMTP ={
    'Mail_user':'377838595@qq.com',
    'Mail_pass':'htlwvsketgyscabc'
}

receivers = ['377838595@qq.com']
filename ='测试数据123'


def sendMail(msg):
    try:
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(mailSMTP.get('Mail_user'), mailSMTP.get('Mail_pass'))  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(mailSMTP.get('Mail_user'),receivers,msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()
        print("邮件发送成功")
    except Exception as e:
        print('发送邮件失败，错误原因'+e)



def packageMailMsg(MailSubject,MailContext,filePath):
    message = MIMEMultipart()
    message['From']=formataddr(["FromRunoob",mailSMTP.get('Mail_user')])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    message['To']=formataddr(["FK",receivers[0]])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    message['Subject']=MailSubject            # 邮件的主题，也可以说是标题
    message.attach(MIMEText(MailContext, 'plain', 'utf-8'))
    os.chdir(filePath)
    dir = os.getcwd()
    for fn in os.listdir(dir):
        attachmentFile = open(filePath+fn,'rb')
        xlsx = MIMEMultipart('alternative')
        xlsx.set_payload(attachmentFile.read())
        encoders.encode_base64(xlsx)
        xlsx.add_header('Content-Disposition','attachment',filename=filename)
        message.attach(xlsx)
    return message



if __name__ == '__main__':
    # message = MIMEMultipart()
    # message['From']=formataddr(["FromRunoob",mailSMTP.get('Mail_user')])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    # message['To']=formataddr(["FK",receivers[0]])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    # message['Subject']="菜鸟教程发送邮件测试"                # 邮件的主题，也可以说是标题
    # message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))
    # filename =r'流水文件.xls'
    # attachmentXlsx =open(r'/Users/hanxiaodi/Documents/民生2020年1-8月流水重叠.xls','rb')
    # xlsx = MIMEMultipart('alternative')
    # xlsx.set_payload(attachmentXlsx.read())
    # encoders.encode_base64(xlsx)
    # xlsx.add_header('Content-Disposition','attachment',filename=filename)
    # message.attach(xlsx)
    # server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
    # server.login(mailSMTP.get('Mail_user'), mailSMTP.get('Mail_pass'))  # 括号中对应的是发件人邮箱账号、邮箱密码
    # server.sendmail(mailSMTP.get('Mail_user'),receivers,message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    # server.quit()  # 关闭连接
    msg =packageMailMsg('测试标题','测试内容','/Users/hanxiaodi/Desktop/测试邮件/')
    sendMail(msg)

