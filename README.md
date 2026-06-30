# Job Application Tracker

## Overview

Job Application Tracker is a command-line application developed in Python to help users manage their job search process. The system allows users to create accounts, manage companies, submit job applications, store data in JSON format, export data to CSV files, and generate useful statistics.

The project follows a simple layered architecture:

* **Models Layer:** Defines the data structures (`User`, `Company`, `Application`).
* **Services Layer:** Contains the business logic and data manipulation functions.
* **Presentation Layer (`main.py`):** Handles user interaction through a terminal-based menu system.

---

# Features

## User Management

* Create new users
* Login with email and password
* List all users
* Update user information
* Delete users
* Secure password storage using SHA-256 hashing

## Company Management

* Create companies
* Search companies by:

  * Name
  * Location
  * Industry
* List all companies
* Update company information
* Delete companies

## Application Management

* Apply to companies
* View all applications
* Retrieve applications by ID
* Filter applications by status
* Update application status
* Delete applications

Supported statuses:

* Applied
* Interview
* Rejected
* Accepted

## Data Persistence

The application supports:

* Saving data to JSON files
* Loading data from JSON files
* Exporting data to CSV files

Generated files:

* `users.json`
* `companies.json`
* `applications.json`
* `users.csv`
* `companies.csv`
* `applications.csv`

## Statistics

The system can generate:

* Total users
* Total companies
* Total applications
* Number of applications per status
* Average expected salary

---

# Project Structure

```text
jobTracker/
│
├── Models.py        # Data models
├── services.py      # Business logic
├── main.py          # User interface
│
├── users.json
├── companies.json
├── applications.json
│
├── users.csv
├── companies.csv
└── applications.csv
```

---

# Data Models

## User

Represents a platform user.

### Attributes

| Attribute      | Type     | Description             |
| -------------- | -------- | ----------------------- |
| id             | int      | Unique identifier       |
| name           | str      | User name               |
| email          | str      | User email              |
| pass_word_hash | str      | SHA-256 hashed password |
| created_at     | datetime | Account creation date   |

### Methods

* `to_dict()`
* `from_dict(data)`

---

## Company

Represents a company.

### Attributes

| Attribute | Type | Description       |
| --------- | ---- | ----------------- |
| id        | int  | Unique identifier |
| name      | str  | Company name      |
| website   | str  | Company website   |
| location  | str  | Company location  |
| industry  | str  | Company industry  |

### Methods

* `to_dict()`
* `from_dict(data)`

---

## Application

Represents a job application.

### Attributes

| Attribute       | Type     | Description         |
| --------------- | -------- | ------------------- |
| id              | int      | Unique identifier   |
| user_id         | int      | Applicant ID        |
| company_id      | int      | Company ID          |
| position        | str      | Job position        |
| status          | str      | Application status  |
| date_applied    | datetime | Date of application |
| salary_expected | float    | Expected salary     |
| note            | str      | Additional notes    |

### Methods

* `to_dict()`
* `from_dict(data)`

---

# Technologies Used

* Python 3
* JSON module
* CSV module
* Datetime module
* Hashlib (SHA-256)

---

# Running the Project

Clone the repository:

```bash
git clone https://github.com/ilyasouerdi/JobTracker.git
```

Move into the project directory:

```bash
cd JobTracker
```

Run the application:

```bash
python main.py
```

---

# Example Workflow

### Create a User

```text
User Management
1. Add User

Name: Ilyas
Email: ilyas@gmail.com
Password: 123456
```

### Create a Company

```text
Company Management
1. Add Company

Name: OpenAI
Website: https://openai.com
Location: San Francisco
Industry: Artificial Intelligence
```

### Apply to a Company

```text
Application Management
1. Add Application

User ID: 1
Company ID: 1
Position: Backend Developer
Expected Salary: 15000
Note: Remote position preferred
```

---

# Future Improvements

Possible enhancements include:

* Email validation
* Stronger password requirements
* Unique email constraints
* Automatic ID generation using UUIDs
* Pagination for large datasets
* Search applications by position
* Search users by name
* Data backup functionality
* Unit testing with pytest
* SQLite database integration
* REST API implementation using FastAPI
* Web interface using Flask or Django
* Docker support
* Logging system
* Authentication tokens
* Object-oriented menu system

---

# Learning Objectives

This project demonstrates practical usage of:

* Object-Oriented Programming (OOP)
* CRUD operations
* Lists and loops
* Error handling
* File handling
* JSON serialization and deserialization
* CSV generation
* Datetime manipulation
* Password hashing
* Modular project organization
* Basic software architecture principles

---

