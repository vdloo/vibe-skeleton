First steps & setup
===================

This document describes the first steps and setup for this project.

## Project set-up

To set up the project, use the following steps:
```
git clone https://github.com/vdloo/vibe-skeleton
cd vibe-skeleton
```

Then install the requirements in a virtual env:
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements/dev.txt
```

Next, make sure to create the sqlite database:
```
./manage.py migrate
```

And to make sure all is OK, you can run the `pytest` unit tests using `tox`:

```
$ tox
py3.11: commands[0]> python manage.py test --verbosity=1 --parallel
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.494s

OK
Destroying test database for alias 'default'...
  py3.11: OK (1.26=setup[0.06]+cmd[1.21] seconds)
  congratulations :) (1.35 seconds)
```

Then to run the webserver of the application, you can run the following
command:
```
./manage.py runserver
```

And then you'll be able to view the web output like so:
```
curl http://127.0.0.1:8000/some_model/
```

For access to the Django admin, see `http://127.0.0.1:8000/admin/`.  There 
are no log-in credentials, authentication has been removed for ease of use.
