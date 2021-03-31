import getpass
import smtplib
# enter email username
USER = input("Enter your email address: ")
# enter email password
PASSWORD = getpass.getpass(prompt="Enter your password: ", stream=None)
try:
    if "gmail" in USER:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
    else:
        server = smtplib.SMTP('smtp.csus.edu', 587)
    server.starttls()
except:
    print("Something went, if you're using gmail. Make sure to allows less secure app login within your settings.")

server.login(USER, PASSWORD)

# compose the subject/body of the email
subject = input("Subject: ")
text = input("Message: ")
message = "Subject: {}\n\n{}".format(subject, text)

# replace file.txt with the file name that has a list of email addesses
fileName = input("File name: ")
f = open(fileName, "r")

for x in f:
    recipient = x
    server.sendmail(USER, recipient, message)

print("Emails has been sent")
f.close()
server.close()
