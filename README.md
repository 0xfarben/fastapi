# SOCIALHUB - A Basic Social Media API Web App
<div align="center">
  <a><img src="https://iili.io/dGsuZen.png" alt="LOGO"/></a>
</div>
SocialHub is a basic social media platform built using FastAPI. This web application allows users to create posts, manage their profiles, authenticate securely, and engage with other users through likes and votes. It aims to provide core social media features while maintaining simplicity and performance.

## Features

- **Post Management**: Create, update, delete, and view posts.
- **User Managementn**: Register users, retrieve user information, and manage user profiles.
- **Authentication**: Secure login system with JWT-based authentication.
- **Voting System**: Users can upvote posts, with the option for back-voting but no down-vote logic.

## Project Structure
### Main Application File: ```main.py```
- The ```main.py``` file initializes the FastAPI app and imports all necessary routes (Post, User, Auth, and Vote).
- It also sets up the database connection through SQLAlchemy.

### Configuration File: ```config.py```
- The configuration file manages environment variables using Pydantic's ```BaseSettings```.
- It loads database credentials, JWT secrets, and other configuration from a ```.env``` file.

### Database Management: ```database.py```
- Defines the PostgreSQL connection using SQLAlchemy.
- Provides a session management system for database transactions.

### Models: ```models.py```
- SQLAlchemy models for database tables: Post, User, and Vote.
- Implements relationships between the models to manage foreign keys.
  
### OAuth & Token Management: ```oauth.py```
- Handles JWT token creation and verification using the ```jose``` library.
- Secure token-based authentication for user login and session management.
  
### Schemas: schemas.py
- Pydantic models for request validation and response serialization.
- Includes models for Posts, Users, Tokens, and Votes.
  
### Utility Functions: utils.py
- Utility functions for password hashing and verification using ```bcrypt```.

### Routes
- **Post Routes**: CRUD operations for posts.
- **User Routes**: Create and retrieve user profiles.
- **Auth Routes**: Login and secure authentication.
- **Vote Routes**: Manage votes (upvote, back vote).

## Installation & Setup
### Prerequisites
- **Python 3.9+**
- **PostgreSQL**

## Clone the Repository

```python
git clone https://github.com/0xfarben/fastapi.git
cd socialhub
```

## Install Dependencies
### You can install the dependencies using the requirements.txt file. Run the following command:
```python
pip install -r requirements.txt
```

### Alternatively, you can install FastAPI and Uvicorn manually:
```java
pip install fastapi[all]
```

## Set up the Database
- Install and configure PostgreSQL.
- Create a new database for the application.
- Create a ```.env``` file in the root directory and add the following environment variables:

``` python
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_USERNAME=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_NAME=your_db_name
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

## Run the Application Locally
### After setting up the database and environment variables, you can run the application using Uvicorn:
```
uvicorn main:app --reload
```

## Access the API Documentation
### Once the application is running, you can access the interactive API documentation:

- Swagger UI: https://swagger.io/tools/swagger-ui/
- FAST API: https://fastapi.tiangolo.com/


Memory updated
Here is a detailed GitHub README file for your SOCIALHUB - A Basic Social Media API Web App project:

SOCIALHUB - A Basic Social Media API Web App
SocialHub is a basic social media platform built using FastAPI. This web application allows users to create posts, manage their profiles, authenticate securely, and engage with other users through likes and votes. It aims to provide core social media features while maintaining simplicity and performance.

Features
Post Management: Create, update, delete, and view posts.
User Management: Register users, retrieve user information, and manage user profiles.
Authentication: Secure login system with JWT-based authentication.
Voting System: Users can upvote posts, with the option for back-voting but no down-vote logic.
Project Structure
Main Application File: main.py
The main.py file initializes the FastAPI app and imports all necessary routes (Post, User, Auth, and Vote).
It also sets up the database connection through SQLAlchemy.
Configuration File: config.py
The configuration file manages environment variables using Pydantic's BaseSettings.
It loads database credentials, JWT secrets, and other configuration from a .env file.
Database Management: database.py
Defines the PostgreSQL connection using SQLAlchemy.
Provides a session management system for database transactions.
Models: models.py
SQLAlchemy models for database tables: Post, User, and Vote.
Implements relationships between the models to manage foreign keys.
OAuth & Token Management: oauth.py
Handles JWT token creation and verification using the jose library.
Secure token-based authentication for user login and session management.
Schemas: schemas.py
Pydantic models for request validation and response serialization.
Includes models for Posts, Users, Tokens, and Votes.
Utility Functions: utils.py
Utility functions for password hashing and verification using bcrypt.
Routes
Post Routes: CRUD operations for posts.
User Routes: Create and retrieve user profiles.
Auth Routes: Login and secure authentication.
Vote Routes: Manage votes (upvote, back vote).
Installation & Setup
Prerequisites
Python 3.9+
PostgreSQL
Clone the Repository
bash
Copy code
git clone https://github.com/your-username/socialhub.git
cd socialhub
Install Dependencies
You can install the dependencies using the requirements.txt file. Run the following command:

bash
Copy code
pip install -r requirements.txt
Alternatively, you can install FastAPI and Uvicorn manually:

bash
Copy code
pip install fastapi[all]
Set up the Database
Install and configure PostgreSQL.
Create a new database for the application.
Create a .env file in the root directory and add the following environment variables:
makefile
Copy code
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_USERNAME=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_NAME=your_db_name
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
Run the Application Locally
After setting up the database and environment variables, you can run the application using Uvicorn:

bash
Copy code
uvicorn main:app --reload
Access the API Documentation
Once the application is running, you can access the interactive API documentation:

Swagger UI: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc

# Example API Usage
## 1. Create a User
```json
POST /users
{
  "email": "user@example.com",
  "password": "strongpassword"
}
```

## 2. Login User
```json
POST /login
{
  "email": "user@example.com",
  "password": "strongpassword"
}
```

## 3. Create a Post
```json
POST /posts
{
  "title": "My First Post",
  "content": "This is the content of my first post!"
}
```

## 4. Upvote a Post
```json
POST /vote
{
  "post_id": 1,
  "dir": 1
}
```

