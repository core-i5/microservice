# microservice
Django application with microservice architecture and rabbitMQ message broker.


Pre-requisites:
1) rabbitMQ-server should be installed on your machine
2) Latest Python3 should be installed on your machine
3) install requirements using below command
    /microservice$ pip install -r requirements.txt


Keys details:

1) name 
    description: Name of user
    type: String
    example:
            {
                "name" : "example"
            } 

2) age
    description: Age of user
    type: Integer
    example:
            {
                "age" : 25
            }

3) fever
    description: how much fever user have?
    type: Float
    example:
            {
                "fever" : 98.78
            }

4) body_pain
    description: how much body pain user have?
    type: Integer
    possible values: 
                    {
                        0 : No Pain,
                        1 : Severe Pain
                    }
    example:
            {
                "body_pain" : 1
            }

5) runny_nose
    description: does user have runny nose?
    type: Integer
    possible values:
                    {
                        0 : No,
                        1 : yes
                    }
    example:
            {
                "runny_nose" : 1
            }

6) diff_breath
    description: how much difficulty user have in breathing?
    type: Integer
    possible values:
                    {
                        -1 : No Difficulty,
                        0 : Medium Difficulty,
                        1 : Severe Difficulty
                    }
    example:
            {
                "diff_breath": 1
            }

7) infection_prob:
    description: user's probability to be covid positive.
    type: Float
    default value: 0.0



_________app Instructions_________

Run server using below command:
    /app$ python3 manage.py runserve

Run consumer application using below command:
    /app$ python3 consumer.py

APIs:

1) Create User
    description: create user api creates a user and also creates the same user in app2 application using rabbitMq.
    endpoint: http://127.0.0.1:8000/app/user/create-user/
    payload format: json
    payload example: 
                    {
                        "name" : "example",
                        "age" : 24,
                        "fever" : 98.76,
                        "body_pain" : 1,
                        "runny_nose" : 1,
                        "diff_breath" : 1
                    }
    response:
            {
                "data": {
                    "id": 31,
                    "name": "example",
                    "age": 24,
                    "fever": 98.76,
                    "body_pain": 1,
                    "runny_nose": 1,
                    "diff_breath": 1,
                    "infection_prob": 0.0
                },
                "code": 201,
                "message": "User Created Successfully!"
            }

2) Get User
    description: get user api returns the user with specified id.
    endpoint: http://127.0.0.1:8000/app/user/get-user/<int:pk>/
    payload format: None
    payload example: None
    response:
            {
                "data": {
                    "id": 31,
                    "name": "a3wsdfsdfsdfdscsr33",
                    "age": 24,
                    "fever": 98.76,
                    "body_pain": 1,
                    "runny_nose": 1,
                    "diff_breath": 1,
                    "infection_prob": 65.92
                },
                "code": 200,
                "message": "OK"
            }

3) Get User List
    description: get user list api returns a list all the existing users.
    endpoint: http://127.0.0.1:8000/app/user/get-user-list/
    payload format: None
    payload example: None
    response:
            {
                "data": [
                    {
                        "id": 31,
                        "name": "examplsde2fe11",
                        "age": 24,
                        "fever": 98.76,
                        "body_pain": 1,
                        "runny_nose": 1,
                        "diff_breath": 1,
                        "infection_prob": 0.0
                    }
                ],
                "code": 200,
                "message": "OK"
            }

4) Update User
    description: update user api updates the user with specified id and also updates the same user in app2 application using rabbitMq.
    endpoint: http://127.0.0.1:8000/app/user/update-user/<int;pk>/
    payload format: json
    payload example: 
                    {
                        "name" : "example",
                        "age" : 24,
                        "fever" : 98.76,
                        "body_pain" : 1,
                        "runny_nose" : 1,
                        "diff_breath" : 1
                    }
    response:
            {
                "data": null,
                "code": 200,
                "message": "User Details Updated Successfully!"
            }

5) Delete User
    description: deleteuser api delete the user with specified id and also delete the same user in app2 application using rabbitMQ.
    endpoint: http://127.0.0.1:8000/app/user/delete-user/<int:pk>/
    payload format: None
    payload example: None
    response:
            {
                "data": null,
                "code": 200,
                "message": "User Deleted Successfully!"
            }


________app2 Instructions_________

Run server using below command:
    /app2$ ./runserver

Run consumer application using below command:
    /app2$ python3 consumer.py

APIs:

1) Get User List
    description: get user list api returns a list of all the existing user.
    endpoint: http://127.0.0.1:8000/app/user/get-user-list/
    payload format: None
    payload example: None
    response:
            {
                "data": [
                    {
                        "id": 31,
                        "name": "example",
                        "age": 24,
                        "fever": 98.76,
                        "body_pain": 1,
                        "runny_nose": 1,
                        "diff_breath": 1
                    }
                ],
                "code": 200,
                "message": "OK"
            }

2) Update user infection probability
    description: update user infection probability api calculate the infection probabity for the user with specified id using a machine
    learning model at backend and call the update user api, from the app application internally to update the infection probability of 
    same user in the app application using rabbitMQ. For detailed description about about machine learning model and the concept please
    check my "Covid-Solution" project, I had made 2 years back at the link https://github.com/Rupesh-Pro/covid_solution.
    endpoint: http://127.0.0.1:8001/app2/user/update-user-infection-probability/31/
    payload format: None
    payload example: None
    response:
            {
                "data": null,
                "code": 200,
                "message": "OK"
            }