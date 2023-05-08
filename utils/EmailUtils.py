import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr
from common.log import logger
from config import conf

# 邮件服务器地址
smtp_server = 'smtp.qq.com'
# 发件人邮箱地址
my_sender = '2950596701@qq.com'
# 发件人邮箱密码或授权码
my_pass = 'tykjmnprjvvsddaa'

code = ''

# 第三方 SMTP 服务
def send_email(addr):
    ret = True

    try:
        if not code:
            time.sleep(2)



        #需要修改


        cc_list  = conf().get("master_emails",[])
        if len(cc_list) <=0:
            logger.info("没有配置邮箱地址，无需发送邮箱")
            return


        my_user= cc_list[0]
        msg = MIMEText(f'尊敬的客户，重新登录二维码地址在下，请点击扫码登录,口令为 {code}: \n\n\t {addr}', 'plain', 'utf-8')
        msg['Subject'] = "请重新登录" # 邮件的主题，也可以说是标题
        msg['Cc'] = ','.join(cc_list)
        msg['From'] = formataddr(["流云工作室", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号


        msg['To'] = formataddr(["尊敬的客户", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        logger.info("发送成功")
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        logger.error("Main program error:")
        logger.error(e)

        ret = False
    return ret
