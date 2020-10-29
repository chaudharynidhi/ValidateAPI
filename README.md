# ValidateAPI

APP for receiving the validations for the POST Requests.

Built in DJango Framework and Postgresql DB with docker containerization

Steps to use this API:

1. Install docker if not installed earlier using Docker documentation(https://docs.docker.com/get-docker/)

2. Install docker-compose also using the Docker Documentation(https://docs.docker.com/compose/install/)

3. Then clone this project.

4. In the terminal(since I have used the Linux OS), use these steps:

5. Go to the projects directory which has the manage.py file(newapp), in terminal.

```docker-compose build```
(This will install all the required libraries in loading this APP.)

``` docker-compose up -d ```
(This will make the status up for the app and the db)

``` 
docker-compose run web python3 manage.py makemigrations
docker-compose run web python3 manage.py migrate
docker-compose run web python3 manage.py runserver 
```

There are 4 links which we can traverse through:

For APIs:
1. http://127.0.0.1:8000/api/age/  -> for Age API
2. http://127.0.0.1:8000/api/id/   -> for ID API

For validation results from APIs:
1. http://127.0.0.1:8000/id/       -> for ID validated results
2. http://127.0.0.1:8000/age/      -> for Age validated results

### The fields for IDModel is:  

'invalid_trigger' //String

'key'  //String

'name' //String

'reuse'  //Boolean

'support_multiple'  //Boolean

'pick_first'  //Boolean

'support_values'  //List

'type1' //List 

'validation_parser'  //String

'values' //List of Dictionary




### The fields for AgeModel is:  

'invalid_trigger' //String

'key'  //String

'name' //String

'reuse'  //Boolean

'constraint' //String 

'support_multiple'  //Boolean

'pick_first'  //Boolean

'var_name' //String

'type1' //List 

'validation_parser'  //String

'values' //List of Dictionary

#### The image size used in this APP is 940MB

