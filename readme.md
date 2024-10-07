1> pip3 install uv
2> uv env //To create the virtual environment
3> source .venv/bin/activate(To activate the virtual environment)  //// deactivate(To deactivate the virtual environment)
4> uv pip install Django
5> django-admin startproject <* Project Name *>(To create the project)
6> cd <* Project Name *> 
7> python manage.py runserver <* Optional Port Number *>(To start the server)
8> Folder Structure
    => myProject -> myProject -> settings.py (Includes db, server port, authentication, etc)
    => myProject -> myProject -> urls.py (Defines the url for the project)
9> Basic flow
    => users -> req -> urls.py -> views.py -> (templates, db, etc) ->  response