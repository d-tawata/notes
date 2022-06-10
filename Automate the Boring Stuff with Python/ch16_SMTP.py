import yagmail
from settings import user, to

appPassword = input('Enter your app password: ')
subject = 'test subject 1'
content = ['mail body content','images/Library.jpg','images/JeffGoldblumGif.mp4']

#with yagmail.SMTP(user, appPassword) as yag:
    #yag.send(to, subject, content)