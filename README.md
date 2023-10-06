# Task Manager App

The Task Manager App is a simple Python-based command-line application that allows you to manage and organize your tasks. You can create, update, list, and delete tasks using this application.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Features

- Create new tasks with titles and descriptions.
- List all tasks in your task list.
- Update the status or details of a task.
- Delete tasks that are no longer needed.
- Store task data in a text file for persistence.

## Requirements

To run the Task Manager App, you need the following:

- Python 3.x
- [Docker](https://www.docker.com/) (optional, for running in a container)

## Installation

1. Clone this repository to your local machine:

git clone https://github.com/yourusername/task_manager_app.git

Change to the project directory:

cd task_manager_app

Install the required Python packages:

pip install -r requirements.txt

If you prefer using Docker, you can build the Docker image using the provided Dockerfile:

docker build -t task_manager_app .

## Usage

Run the Task Manager App:

python task_manager.py

If you are using Docker, you can run the app in a container:

docker run -it task-manager-app
Follow the on-screen instructions to interact with the Task Manager App.
