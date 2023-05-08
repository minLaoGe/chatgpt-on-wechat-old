import smtplib
from email.mime.text import MIMEText
from email.header import Header
from config import conf

# 邮件服务器地址
smtp_server = 'smtp.qq.com'
# 发件人邮箱地址
from_addr = '2950596701@qq.com'
# 发件人邮箱密码或授权码
password = 'tykjmnprjvvsddaa'



def send_email(qr_api3):

    master_emails = conf().get("master_emails",[])

    last_emails = []
    if len(master_emails)<=0:
        return


    for email in master_emails:
        last_emails.append(email.strip())



    # 邮件内容
    message = MIMEText(f'尊敬的用户，最新登录地址为: \n\n\t{qr_api3}', 'plain', 'utf-8')
    message['From'] = Header('流云工作室', 'utf-8')
    message['To'] = Header('尊敬的客户', 'utf-8')
    message['Subject'] = Header('重新登录提醒', 'utf-8')

    # 发送邮件
    try:
        server = smtplib.SMTP(smtp_server, 25)
        server.starttls()
        server.login(from_addr, password)
        server.sendmail(from_addr, last_emails, message.as_string())
        print('邮件发送成功')
    except Exception as e:
        print('邮件发送失败')
    finally:
        server.quit()


