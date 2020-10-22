# Minnal Murali 

Minnal Murali is a python bot to send quick reply for your typeform responses. 

Test this Bot by filling [this form](https://programmerme.typeform.com/to/l12ftsPx) : 

## Working 
typeform webhook > flask app > MIMEMultipart > python smtp 

message.txt : contain your custom message text. 
If you want to add images. Add your image file with name *img.jpg*

Procfile : For heroku deploy


Flask modulue 

    pip install Flask



Dont forget to *allow access to unsecure app* in gmail security settings. 
