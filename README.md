CS50 PROJECT 5 - TASKS (CAPSTONE)

PROJECT STATUS
--------------
This project is currently UNFINISHED and under active development. 
Not all features may be fully implemented or tested.

OVERVIEW
--------
Tasks is a task management web application built with Django and Python. 
This capstone project allows users to create, organize, and track tasks with 
due dates, descriptions, and completion status.  The application provides a 
sortable task list interface with expandable task details.

FEATURES
--------
Implemented:
- User Authentication:  Register, login, and logout functionality
- Create Tasks: Users can create tasks with title, description, and due date
- Task Completion: Toggle task completion status
- Delete Tasks: Remove tasks from the list
- Sortable Task List: Sort tasks by title, author, start time, or due date
- Expandable Task Details: Click task titles to view descriptions
- Task Forms: Django forms for task creation with validation
- Responsive UI: Grid-based layout with hover effects

Partially Implemented:
- Comment System: Models and forms exist but may not be fully integrated

TECHNOLOGIES
------------
- Python (47. 9%)
- HTML (42.0%)
- CSS (10.1%)
- Django Web Framework
- Django Forms for data validation
- Django ORM for database management
- JavaScript for dynamic interactions and sorting

PROJECT STRUCTURE
-----------------
capstone/
  - models.py: Database models (User, Task, Comment)
  - views.py: Application logic and view functions
  - urls.py: URL routing configuration
  - forms.py: Django forms (TaskForm, CommentForm)
  - templates/: HTML templates
  - static/: CSS stylesheets
  - migrations/:  Database migrations
  - admin.py: Django admin configuration

manage.py: Django management script
project5/:  Django project configuration

DATABASE MODELS
---------------
User:  Extended Django AbstractUser
Task:  Stores tasks with author, title, description, due_date, completed status, 
      and start_time
Comment: Stores comments on tasks (defined but may not be fully functional)

INSTALLATION
------------
1. Install Python 3.x
2. Install Django:  pip install django
3. Navigate to project directory
4. Run migrations: python manage.py makemigrations && python manage.py migrate
5. Create superuser (optional): python manage.py createsuperuser
6. Start development server: python manage.py runserver

USAGE
-----
1. Navigate to http://localhost:8000
2. Register a new account or login
3. Create tasks using the task form
4. Click on task titles to expand and view descriptions
5. Use column headers to sort tasks by different criteria
6. Mark tasks as complete or delete them using action buttons
7. View tasks in a sortable grid layout

URL ENDPOINTS
-------------
/ - Homepage with task list\
/login - User login page\
/logout - Logout user\
/register - New user registration\
/task/create - Create a new task\
/task/<task_id>/toggle - Toggle task completion status\
/task/<task_id>/delete - Delete a task

FEATURES
--------
Task List Display:
- Grid layout with columns:  checkbox, title, author, actions, start date, due date
- Sortable columns with ascending/descending indicators
- Expandable task descriptions on title click
- Hover effects on task rows and buttons

Task Actions:
- Complete button (appears on hover, turns green)
- Delete button (appears on hover, turns red)
- Both actions use AJAX for seamless updates

Task Form:
- Title input (max 128 characters)
- Description textarea (optional)
- Due date picker (optional)
- Form validation through Django forms

NOTES
-----
- This is a CS50 Web Programming with Python and JavaScript capstone project
- Tasks are displayed with real-time sorting capabilities
- Only authenticated users can create and manage tasks
- Task action buttons appear on hover for cleaner interface
- Uses JavaScript for client-side sorting and UI interactions
