# SOCIALHUB - A Basic Social Media API Web App
<h1><center>FastAPI - Social Hub</center></h1>
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
### Main Application File: main.py
- The main.py file initializes the FastAPI app and imports all necessary routes (Post, User, Auth, and Vote).
- It also sets up the database connection through SQLAlchemy.

### Configuration File: config.py
- The configuration file manages environment variables using Pydantic's BaseSettings.
- It loads database credentials, JWT secrets, and other configuration from a .env file.

### Database Management: database.py
- Defines the PostgreSQL connection using SQLAlchemy.
- Provides a session management system for database transactions.

### Models: models.py
- SQLAlchemy models for database tables: Post, User, and Vote.
- Implements relationships between the models to manage foreign keys.
  
### OAuth & Token Management: oauth.py
- Handles JWT token creation and verification using the jose library.
- Secure token-based authentication for user login and session management.
  
### Schemas: schemas.py
- Pydantic models for request validation and response serialization.
- Includes models for Posts, Users, Tokens, and Votes.
  
### Utility Functions: utils.py
- Utility functions for password hashing and verification using bcrypt.
