# Minnal Murali 

Minnal Murali is a python bot to send quick reply for your typeform responses. 

Test this Bot by filling [this form](https://programmerme.typeform.com/to/l12ftsPx) : 

## Working 
typeform webhook > flask app > MIMEMultipart > python smtp 

message.txt : contain your custom message text. Add image if you want to attach. 

Procfile : This file is needed while deploying in heroku. 


Flask modulue 

    pip install Flask



Dont forget to *allow access to unsecure app* in gmail security settings. 


Credits: https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/