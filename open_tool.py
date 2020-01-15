import censys.certificates
import censys.ipv4
import censys
import sys
import cli
import os
import time
import smtplib

api_id = 'your censys_api_id'
api_secret = 'your censys_api_secret'
from email.mime.text import MIMEText
import censys_search_ipv4
if __name__ == "__main__":
    args = cli.parser.parse_args()
    ck_num = 0
    print(args)
    censys_api_id = api_id
    censys_api_secret = api_secret
    if "CENSYS_API_ID" in os.environ and "CENSYS_API_SECRET" in os.environ:
        censys_api_id = os.environ['CENSYS_API_ID']
        censys_api_secret = os.environ['CENSYS_API_SECRET']
    if args.censys_api_id and args.censys_api_secret:
        censys_api_id = args.censys_api_id
        censys_api_secret = args.censys_api_secret
    if None in [censys_api_id,censys_api_secret]:
        if censys_api_id == None:
            print("error : Censys_api_id를 입력하지 않았습니다.\n")
            ck_num = 1
        if censys_api_secret == None:
            print("error : Censys_api_secret를 입력하지 않았습니다.\n")
            ck_num = 1
    if ck_num == 1:
        exit(1)

def save_li(li,output_file):
    if output_file is None or len(li) is 0:
        return 
    try:
        with open(output_file,'w') as f:
            for line in li:
                f.write(line+"\n")
        print("해당 파일에 저장되었습니다.")
    except Exception as ex:
        print('error',ex)
def send_mail(mail_address,li,domain):
    print("메일을 보냅니다. ")
    if args.mail_address != None:
        # 세션 생성
        gmail_id = input('id를 입력하세요(ex)abcd123) : ')
        gmail_id += '@gmail.com'
        gmail_app_password = input('google의 앱 비밀번호를 입력하세요 : ')
        send_mail = args.mail_address
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # TLS 보안 시작
        s.starttls()
        # 로그인 인증
        s.login(gmail_id, gmail_app_password)
        # 보낼 메시지 설정
        text = ""
        for i in li:
            text += i+"\n"
        msg = MIMEText(text)
        msg['Subject'] = 'Censys_ipv4_searching_results('+domain+')'
        # 메일 보내기
        s.sendmail(gmail_id,send_mail, msg.as_string())
        # 세션 종료
        s.quit()
    else:
        return
def main(domain,output_file,censys_api_id,censys_api_secret,mail_address):
    print("censys_ipv4 searching start! (limit 1000 counts)")
    start_time = time.time()
    results = censys_search_ipv4.search_domain_ipv4(domain,censys_api_id,censys_api_secret)
    ans = input("filtering (ip, protocol/ports)? (y/n,default=y) : ")
    count = 0
    if ans == 'n' or ans == 'N':
        li,count = censys_search_ipv4.nonconvert(results)
    else:
        li,count = censys_search_ipv4.convert(results)
    end_time = time.time()
    time_ellaped = round(end_time-start_time,1)
    print(domain,' searching time is ',time_ellaped)
    print("total counts : ",count)
    for i in li:
        print(i)
    save_li(li,output_file)
    send_mail(args.mail_address,li,domain)
     
main(args.domain,args.output_file,censys_api_id, censys_api_secret,args.mail_address)        

