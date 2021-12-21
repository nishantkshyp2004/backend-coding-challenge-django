# Backend Coding Challenge

[![Build Status](https://github.com/Thermondo/backend-code-challenge/actions/workflows/main.yml/badge.svg?event=push)](https://github.com/Thermondo/backend-code-challenge/actions)

A backend REST API for a simple note-taking app. Below you will find a list of tasks and limitations.


### Application:

* Users can add, delete and modify their notes
* Users can see a list of all their notes
  Sample request: http://127.0.0.1:8000/notetaking/
* Users can filter their notes via tags.
  Sample request http://127.0.0.1:8000/notetaking/?tags=true&search=study
* Users must be logged in, in order to view/add/delete/etc. their notes

### The notes are plain text and should contain:

* Title
* Body
* Tags

### Optional Features 🚀
#### Please note: these features are tested and marked as done.

* [x] Search contents of notes with keywords
* Search can be done using the filter functionality in the browseable api.
* But default it takes the search params and they are supporting to do search on notes title and body.
* Sample request: http://127.0.0.1:8000/notetaking/?search=Meeting
* [x] Notes can be either public or private
    * Public notes can be viewed without authentication, however they cannot be modified
* [x] User management API to create new users

### Run the Note Taking App.
For the time time build the docker image and run the container.
```bash
docker-compose up --build
```
For the next run:

```bash
docker-compose up
```

### code style complaint
* [x] The code is flake8 compliant.

### Username and Password to login.
```python
username:admin
password:password
```
