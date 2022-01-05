# Owlapp : Technical test for Owlint

## Disclaimer
This is a project I did for a technical test. It will not be maintained past January 2022, and is NOT to be used in production without extensive testing, as I cannot guarantee safe nor stable functioning. 

Apart from this, please help yourself to anything in here that could help you 🙂.   Also, please feel free to send me a message if something is not clear or if you need help with my code (note that I cannot guarantee response delay).

## Documentation
This project's objective is to set up an API and a Postgresql database, with 2 main goals:
- Accept comments via the API *new_comment* endpoint, translate these comments (EN to FR or FR to EN), and store them in the database
- Retrieve comments via the API *get_comments* endpoint based on a comment attribute named **targetId**

For this, we set up two Docker containers (one for the API app, one for the database) via a docker-compose. The translation is done by the Google Translate API.

## 1 - Setup ⚙️
Clone this repo:

```
git clone git@github.com:TomsHL/owlapp.git
```

### API 

Setup a project and activate Google Translation API (follow [this tutorial](https://cloud.google.com/translate/docs/setup) until you have your JSON credentials).
Do not worry for the billing, it is free for reasonable use (translation of less than 500 000 characters a month) 😄

Once you have the JSON credentials file, copy it in the **keys** directory.

### Slack

You will need a Slack workspace and a bot to post messages in a channel in this workspace. For this, you can follow [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-build-a-slackbot-in-python-on-ubuntu-20-04) until the end of part 5.

### Postgresql database

An example database is set up in a Docker container with this repo:

![image](https://user-images.githubusercontent.com/6053046/148248738-e55f1306-7b4e-4831-8580-d2b1c5fa332f.png)

However, if you want to only use the API part and connect your own database, there are a few steps to follow:
- Make sure that your database accept external connections authentified by a password [(see here](https://www.postgresql.org/docs/9.1/auth-pg-hba-conf.html) for example).
- Make sure that your database uses a schema matching the one defined in [owlappdb_create.sql](https://github.com/TomsHL/owlapp/blob/master/owlappdb/owlappdbcreate.sql) : 

![image](https://user-images.githubusercontent.com/6053046/148254507-c71807b9-a852-45ee-af3a-51dc3cfd7511.png)

If not, you are now on your own, as you would have to change the schema in most parts of this code! 😨😨😨

- Change the database address in the .env file (see below).

### Environment variables

This project is setup with a few environment variables that you need to fill in the .env file:
- Rename the .env.copy to .env
- Fill the name of your **GOOGLE_APPLICATION_CREDENTIALS** JSON (do not change the */keys* directory)
- Fill your Slack token and your Slack channel name
- If needed, fill the address of your Postgresql database. If not, leave it as it is.

![image](https://user-images.githubusercontent.com/6053046/148248993-1d0f078d-b8f3-4592-849a-ec6539ab1e1f.png)

## 2 - Spin it up! ▶️

What do you want?

### Full package : API and Database

```
docker-compose build
docker-compose up
```
Note that this can be a bit long the first time (Docker building images).
The API is now up locally (http://localhost:8008/  or http://127.0.0.1:8008 for the root endpoint)

![image](https://user-images.githubusercontent.com/6053046/148250433-fd5b20a0-226d-4e46-b5df-0aa88a0cfdf7.png)

You can also use the *new_comment* endpoint whith a POST request and *get_comments* with a GET request. See below basic examples in Python:

POST new comment : 
```
import requests

# POST request
headers = {}
headers['Content-Type'] = 'application/json'
request_dict = {
    'text_new_comment' : 'Ceci est un test!',
    'authorId' : 'Tom',
    'targetId' : 'NewComment'}

# Send the request, get the result
req = requests.post('http://127.0.0.1:8008/new_comment',json.dumps(request_dict), headers = headers)
d= json.loads(req.content)
```

![image](https://user-images.githubusercontent.com/6053046/148250813-e65de031-0a79-4ffb-92c4-1d8c00a96350.png)

Note that the *publishedAt* and *id* fields are automatically filled by the API. However, you can manually add a *publishedAt* field in the request body if necessary.

GET comments:

```
import requests

payload = {'targetId': 'Comment_5547'}
req = requests.get('http://127.0.0.1:8008/get_comments', params=payload)
d= json.loads(req.content)
```

![image](https://user-images.githubusercontent.com/6053046/148251217-77c7279d-0b6c-411c-bc4b-1b4b9522cb20.png)


### API only

OK I see, difficult customer here. Here you go then:
- You can fill your database address in the .env (see Setup/Postgresql database above). Then, rebuild the docker-compose, and launch only the app part : 

```
docker-compose run app bash 
```

- Or directly build the app image via the dockerfile:

```
docker build -t=owlapp .
docker run -e PORT=8000 -p 8008:8000  owlapp  
```

You should now have the API running locally (http://localhost:8008/  or http://127.0.0.1:8008 for the root endpoint).

### Database only

..... but why?
Anyway, here you go:
- If you already built the docker-compose image:

```
docker-compose run db bash 
```

- Or you can build it directly :

```
cd owlappdb
docker build -t=owlappdb .
```

# The end
Hit me up if you need some help or have suggestions!
