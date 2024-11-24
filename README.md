# to-do-list

Django project for managing task and tag

## Installation

Python3 must be installed

```shell
git clone https://github.com/arsenmarkotskyi/to-do-list
cd to-do-list
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver

```

## Features
* Managing tasks & tags directly from website interface
* Complete and undo func

## Demo

![[Website Interface]](img.png)

## Models

### Task
- `content`: describes what you should do.
- `created_at`: datetime, when a task was created.
- `deadline`: optional deadline datetime if a task should be done until some datetime.
- `is_done`: the boolean field that marks if the task is done or not.
- `tags`: tags that are relevant for this task`.

### Tag
- `name`: tag symbolizes the theme of the task and consists only of a name.
