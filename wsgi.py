import os  
import sys  

# This will automatically set the path to the project directory  
# Assuming your project structure is 'project_root/django_tts_app'  
current_dir = os.path.dirname(os.path.abspath(__file__))  
project_dir = os.path.dirname(current_dir)  
sys.path.append(project_dir)  

# Set the Django settings module  
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_tts_app.settings')  # Adjust this as needed  

# Import the WSGI application  
from django.core.wsgi import get_wsgi_application  
application = get_wsgi_application()