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

####### Lec-4 #######
12> jinja2 (Best Template Engine for django) => Used for rendering html templates and insert variables  in html
13> Creating app in django (one root folder/project and can have multiple app folders) 
    => python manage.py startapp <* app_name *> (To create the app) => mainly used to aware main project that we have new app.
    => add <* app_name *> in settings.py inside [INSTALLED_APPS] (To add the app to the project)
    => create new templates folder in <* app_name *> (best practice to create seperate templates folder for each app)
    => create views.py in <* app_name *> folder and render function in views.py
    => create urls.py in <* app_name *> folder and add url what defined in views.py (For this we have to url mapping in urls.py file of root project by using include function)
    => now we can run python manage.py runserver and get by adding what we have added in mapping (ex- localhost:8000/secondApp/......)
14> More on jinja2
    => Created common layout.html in root project templates and used this layout.html in all html file inside templates folder of root project and secondApp