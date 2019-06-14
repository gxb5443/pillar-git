# Pillar Github API

This is a simple app that displays a dashboard for github repo's statistics.

## Overview

The system will authenticate a user with github, store that token in the session
(not ideal, it should be in a database and hidden behind some opaque userid).
The front end then makes a get request to the python api using the token to get
a github repo, parse it and display the desired statistics in a component.

### Design

The design of this is simple. It first consists of a flask backend which manages user
auth with github and api requests (served with gunicorn). The api is used by a react app which is
served by an nginx instance. The nginx instance serves the static react page and
also forwards requests to the api. This decoupling should make the system much
more scalable because the app and the api operate independently. The api can
serve both a regular web front-end as well as a mobile app or any other client.
Using nginx also takes load off the python server and also allows us to scale
the python api out horizontally and let nginx load balance.

### Design Issues

Due to time constraints this app only looks up the stats for the (hardcoded)
*facebook/react* repo. Due to a production issue at the time of writing this I was
unable to make it interactive via web client. Another issue is the auth flow
should be cleaner: you shouldn't have to first navigate to the login page
manually, the system should manage basic routing. (I struggled a bit with
getting github auth flow to work). I'd also have liked to properly store the
user's credentials in a database rather than in a session cookie, but I felt
that including a database would have been overengineering for this test.
Finally, this test is missing the contributors statistic because I didn't
immediately see it in the repo object returned by github and again I ran out of
time.

## Usage
### Set up
The entire system has been dockerized. To run the system, simple run
```bash
$ docker-compose up --build
```
Then go to web browser and navigate to `http://lvh.me/api/login`

## Contributor
- Gian Biondi <gianbiondijr@gmail.com>
