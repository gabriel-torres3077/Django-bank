# Django bank
Guide:
- [Install](#install)
- [Django bank API](#bank-api)
    - [User](#user)
        - [Create User](#create-user)
            - [User Register Request](#user-Register-request)
        - [Get User](#get-user)
            - [Get User Request](#get-user-request)
        - [Update User](#update-user)
            - [Update User Request](#update-user-request)
        - [Delete User](#delete-user)
            - [Delete User Request](#delete-user-request)
    - [Account](#account)
        - [Create Account](#create-account)
            - [Create Account Request](#create-account-request)
        - [Get Account](#get-account)
            - [Get Account Request](#get-account-request)
        - [Update Account](#update-account)
            - [Update Account Request](#update-account-request)
        - [Delete Account](#delete-account)
            - [Delete Account Request](#delete-account-request)
    - [Transfer](#transfer)
            - [Create Transfer](#create-transfer)
                - [Create Transfer Request](#create-transfer-request)
            - [Get Transfer](#get-transfer)
                - [Get Transfer Request](#get-transfer-request)
            - [Update Transfer](#update-transfer)
                - [Update Transfer Request](#update-transfer-request)
            - [Delete Transfer](#delete-transfer)
                - [Delete Transfer Request](#delete-transfer-request)

## Instalation guide
- Setup your python environment
```shell
Django-bank/imo_bank/>python -m venv venv
```

- Activate the environment
```shell
Django-bank/imo_bank/>.\venv\Scripts\activate
```

- install requirements
```shell
(venv) Django-bank/imo_bank/>pip install -R requirements.txt
```

- Run the project
```shell
(venv) Django-bank/imo_bank/>python .\manage.py makemigrations

(venv) Django-bank/imo_bank/>python .\manage.py migrate

(venv) Django-bank/imo_bank/>python .\manage.py runserver
```

# User
## User Register

### User Register Request

```js
POST /api/user
```

```json
{
    "email": "your@email.com.br",
    "cpf": "12345678910",
    "birth": "2023-03-07",
    "gender": "M",
    "phone": "11982203077",
    "password": "yourpassword",
    "first_name": "firstname",
    "last_name": "lastname"
}
```

### Create User Response

```js
201 Created
```

## User Login

### User Login Request

```js
POST /api/user/login/
```
```json
{
    "email": "your@email.com.br",
    "password": "yourpassword",
}
```
### User Login Response

```js
200 Ok
```

```json
set_cookie = jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTIsImV4cCI6MTY3ODMzNDkwMiwiaWF0IjoxNjc4MjQ4NTAyfQ.hpgg0Rdx-ku92n0O_0ukqNabK0DrEREpKyYQ0r_yuHw; HttpOnly; Path=/
```

## User Logout

### User Logout Request

```js
POST /api/user/logout/
```

### User Logout Response

```js
200 OK
```

## User Delete

### User Delete Request

```js
DELETE /api/user/delete/
```

### User Delete Response

```js
204 No Content
```

# Next part Under construction