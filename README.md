# Mock
A personalized mock interview platform made for Cornell CS grad students

# Local Execution (Backend)
First you must create a virtual environment. 
1. Within the /backend directory, run 
python -m venv venv_backend
source venv_backend/bin/activate
pip install -r requirements.txt
2. To run the server, you run (within the backend directory)
uvicorn app.main:app --reload

