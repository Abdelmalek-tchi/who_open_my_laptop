import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import cv2
import random

# I used the random numbers to evade overwriting the picture

nam = random.randint(0,1000000)
cap = cv2.VideoCapture(0)
ret, frame = cap.read()



cv2.imwrite(f'C:\\agent_py\img{str(nam)}.jpg', frame)
cap.release()
cv2.destroyAllWindows()




sender_email = ""
receiver_email = ""
#not your password you need to get Gmail api key
password = ""


message = MIMEMultipart()
message['Subject'] = 'Someone on your pc'
message['From'] = sender_email
message['To'] = receiver_email
text = MIMEText(f'image{nam}.jpg')
message.attach(text)


with open(f'C:\\agent_py\img{str(nam)}.jpg', 'rb') as f:
    img_data = f.read()
image = MIMEImage(img_data, name=f'C:\\Users\malek\Desktop\pypic\img{str(nam)}.jpg')
message.attach(image)


with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

