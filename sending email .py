import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)# smtp session
s.starttls() # security
s.login("shivakrishnanangunuri@gmail.com","lbcqvwgkxjhmkeb")#sender mail.id
msg=input("enter ur message")
s.sendmail("shivakrishnanangunuri@gmail.com","18p61a1240@vbithyd.ac.in",msg)
s.quit()
