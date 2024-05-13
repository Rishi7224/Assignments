import smtplib

try:
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.starttls()
    sender_email ="talesarar@gmail.com" 
    sender_password = "jjzu igho fezw yofe"

    reciever_email = input("Please enter reciever email :")
    subject = input("Please enter the subject")
    body = input("Message enter kijiye : ")

    server.login(sender_email,sender_password)
    print("You have been logged in succesfully!!")

    message = f"subject :{subject}\n\n{body}"

    server.sendmail(sender_email,reciever_email,message)
    print("email succesfully send")
    server.quit()
except Exception as e:
    print(e)