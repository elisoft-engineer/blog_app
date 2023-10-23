# Blog App

The Blog App is a web application built with Django that allows users to create, read, update, and delete blog posts.

## Features

- User authentication: signup, signin, and signout.
- Create, read, update, and delete blog posts.
- Password reset functionality.
- User-friendly interface.
- Responsive design for mobile and desktop.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (3.7 or higher)
- Pipenv
- Git

### Installation

1. Create a virtual environment on your machine

Windows
-------

Using Command Prompt:

Open Command Prompt.
Navigate to your project directory.
Install virtualenv (if not installed): pip install virtualenv
Create a virtual environment: python -m venv envname
Activate the virtual environment: .\\envname\\Scripts\\activate
Using PowerShell:

Open PowerShell.
Follow the same steps as Command Prompt.

macOS and Linux
---------------

Open the Terminal.

Navigate to your project directory.

Create a virtual environment: python -m venv envname

Activate the virtual environment: source envname/bin/activate

For macOS M1 (Apple Silicon), use: source envname/bin/activate.csh if needed.

Remember to deactivate the virtual environment when done using: deactivate (for all environments).

2. Clone the repository:

change the directory to your virtual environment before cloning
```bash
git clone https://github.com/elisoft-engineer/blog_app.git
cd blog_app

