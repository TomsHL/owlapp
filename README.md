# Owlapp : Technical test for Owlint

## Disclaimer
This is a project I did for a technical test. It will not be maintained past January 2022, and is NOT to be used in production without extensive testing, as I cannot guarantee safe nor stable functioning. 

Apart from this, please help yourself to anything in here that could help you 🙂.   Also, please feel free to send me a message if something is not clear or if you need help with my code (note that I cannot guarantee response delay).

## Documentation
This project objective is to set up an API and a Postgresql database, with 2 main goals:
- Accept comments via the API *new_comment* endpoint, translate these comments (EN to FR or FR to EN), and store them in the database
- Retrieve comments via the API *get_comments* endpoint based on a comment attribute named **targetId**

For this, we set up two Docker containers (one for the API app, one for the database) via a docker-compose. The translation is done by the Google Translate API.

## 1 - Setup 
Clone this repo:

```
git clone git@github.com:TomsHL/owlapp.git
```

### API 

Setup a project and activate Google Translation API (follow [this tutorial](https://cloud.google.com/translate/docs/setup) until you have your JSON credentials).
Do not worry for the billing, it is free for reasonable use (translation of less than 500 000 characters a month) 😄

Once you have the JSON credentials file, copy it in the **keys** directory.
