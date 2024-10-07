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

####### Lec-3 #######
9> Basic flow
    => users -> req -> urls.py -> views.py -> (templates, db, etc) ->  response

10> templates(html) folder (To be created in main myProject folder)
    => Add index.html in templates folder
    => In settings.py add "templates" in DIRS list of TEMPLATES
    => Add in views.py using render function which is imported from django.shortcuts import render

11> static(images, js, css) folder (To be created in main myProject folder)
    => Add styles.css in static folder
    => In settings.py add "STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]" after importing os
    => Now modify index.html in templates folder to include "<link rel="stylesheet" href="{% static 'styles.css' %}">" in head and "{% load static %}" at the top of the html