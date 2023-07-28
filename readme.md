1. intall the necessary dependencies
  django, django tailwind
     pip install django 
      pip install django django-tailwind
        // install django taiwind package
          python -m pip install git+https://github.com/timonweb/django-tailwind.git

2. create a project and app
  django-admin startproject core . // I call my project core // a dot means here
    python manage.py startapp dataentry  // i call my app dataentry
      // register the app under apps in settings file in core

3. Integrate django-tailwind
    // this is for styling, i chose tailwind instead of bootstrap
    // this requires an app that will contain all dependencies & configuration
    // first initialize tailwind
      python manage.py tailwind init
    //register app name in settings
      TAILWIND_APP_NAME = 'theme'
      INTERNAL_IPS = [
          "127.0.0.1",
      ]
     // install taiwind dependencies
        python manage.py tailwind install