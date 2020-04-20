import smtplib
from email.mime.text import MIMEText

# def send_mail(customer, dealer, rating, comments):
#     smtp_server ='smtp.mailtrap.io'
#     port = 2525
#     login = '8e2956fcb967ad'
#     password = 'ea590fcf6e36eb'
#     message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

#     sender_email = 'emirkovacevic92@gmail.com'
#     receiver_email = 'maksuzkal@gmail.com'

#     msg = MIMEText(message, 'html')
#     msg['subject'] = 'Lexus Feedback'
#     msg['From'] = sender_email
#     msg['To'] = receiver_email

#     # Send email
#     with smtplib.SMTP(smtp_server, port) as server:
#         server.login(login, password)
#         server.sendmail(sender_email, receiver_email, msg.as_string())

def send_mail(customer, dealer, rating, comments):

    FROM = 'maksuzkal@gmail.com'
    TO = 'emirkovacevic92@gmail.com'
    SUBJECT = 'Lexus Feedback'
    TEXT = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"
    
    msg = MIMEText(TEXT, 'html')
    msg['subject'] = 'Lexus Feedback'
    msg['From'] = FROM
    msg['To'] = TO

    # message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    # """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    user = 'maksuzkal@gmail.com'
    pwd = 'javolimigratkala'

    

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, msg.as_string())
        server.close()
        print("successfully sent the mail")
    except:
        print("failed to send mail")