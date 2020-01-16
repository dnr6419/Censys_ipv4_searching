import smtplib
import argparse
from email.mime.text import MIMEText
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument(
    'send_address',
    help = '보낼 메일주소를 입력합니다.'
    )
args = parser.parse_args()
def send_mail(mail_address):
    print("메일을 보냅니다. ")
    if mail_address != None:
        # 세션 생성
        gmail_id = input('id를 입력하세요(ex)abcd123) : ')
        gmail_id += '@gmail.com'
        gmail_app_password = input('google의 앱 비밀번호를 입력하세요 : ')
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # TLS 보안 시작
        s.starttls()
        # 로그인 인증
        s.login(gmail_id, gmail_app_password)
        # 보낼 메시지 설정
        text = "this is test!"
        msg = MIMEText(text)
        msg['Subject'] = 'mail_test'
        # 메일 보내기
        s.sendmail(gmail_id,mail_address, msg.as_string())
        # 세션 종료
        s.quit()
    else:
        print('error : 메일주소를 입력하세요')
        return
send_mail(args.send_address)
