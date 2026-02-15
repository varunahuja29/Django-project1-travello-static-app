Build Django apps named Calc and Travello.
Calc is a basic addition app accepting inputs from user and displaying results back.
Travello is a travel website built using static images and content. Base start up is from the free travello app, which is customized further using Django framework and capabilities.

The base Django project was setup with name project1 and further apps were created such as calc and travello. All parent app settings and files are stored in project1 folder.

YouTube Video/Playlist for reference: https://www.youtube.com/watch?v=SIyxjRJ8VNY&list=PLsyeobzWxl7r2ukVgTqIQcl-1T0C2mzau&index=2

#HOW TO RUN THE APP
1. Clone the git repo in a folder using command: https://github.com/varunahuja29/Django-project1-travello-static-app.git

2. Create virtual environment for execution:
    1. Create a new virtual environment: python -m venv venv1
    2. Activate the environment: venv1/Scripts/activate
        If activate environment command does not work in powershell, run this first: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
    3. Install requirements.txt: pip install -r requirements.txt
    4. List all packages: pip list

3. Run the app using command: python manage.py runserver

4. Navigate to IP address provided by server start up, mostly is http://127.0.0.1:8000/
   The root URL routes to Calc app displaying results in 2 ways - using get and post operations.

5. Navigate to Travello app - http://127.0.0.1:8000/travello

6. Navigate to default admin console - http://127.0.0.1:8000/admin
    If by any chance the admin site does not work the perform below:
    1. Stop the server
    2. Execute command: python manage.py migrate
    3. Run server again: python manage.py runserver