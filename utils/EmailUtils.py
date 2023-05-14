import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr
from common.log import logger
from config import conf
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import qrcode
import io
import os
import glob


# 邮件服务器地址
smtp_server = 'smtp.qq.com'
# 发件人邮箱地址
my_sender = conf().get("mail_sender","2950596701@qq.com")
my_pass = conf().get("mail_password","tykjmnprjvvsddaa")


code = ''

# 第三方 SMTP 服务
def send_email(addr):
    ret = True

    try:
        if not code:
            time.sleep(2)



        cc_list  = conf().get("master_emails",[])
        if len(cc_list) <=0:
            logger.info("没有配置邮箱地址，无需发送邮箱")
            return

            # 创建二维码图片
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(addr)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # 将二维码图片转换为字节流
        img_io = io.BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)

        # 创建一个 MIMEImage 对象
        msg_image = MIMEImage(img_io.read(), _subtype='png')

        # 给图片一个标识符，可以在HTML文本中引用
        msg_image.add_header('Content-ID', '<image1>')
        # 需要修改


        my_user= cc_list[0]
        msg = MIMEMultipart('related')
        # 获取当前Python项目的根目录
        root_dir = os.getcwd()
        # 获取以"app_bot"开头的文件
        files = glob.glob(os.path.join(root_dir, 'app_robot*'))

        botname = ''
        # 去除"app_bot"前缀并打印文件名
        for file in files:
            botname=os.path.basename(file).replace('app_robot', '').replace(".py",'')

        text_part  = MIMEText(f'尊敬的客户机器人昵称为:{botname}，需要重新登录二维码地址在下，请点击扫码登录,口令为 {code}: \n\n\t {addr} \n\n 或者扫描一下二维码 <br><img src="cid:image1">', 'html', 'utf-8')
        msg.attach(text_part)
        msg.attach(msg_image)

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

def send_email_str(text,sub):
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
        msg = MIMEText(f'尊敬的客户，重新登录二维码地址在下，请点击扫码登录,口令为 {code}: \n\n\t ', 'plain', 'utf-8')
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
