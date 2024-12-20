# Mock
A personalized mock interview platform made for Cornell CS grad students

# Local Execution (Backend)
First you must create a virtual environment. 
1. Within the /backend directory, run 
`python -m venv venv_backend` -> 
`source venv_backend/bin/activate` ->
`pip install -r requirements.txt`

2. To run the server, you run (within the backend directory)
uvicorn app.main:app --reload

# Local Execution (Frontend)
First you need to ensure you install the dependencies
1. Within the /frontend directory, run
`npm install `
Note: this will install the required packages. Don't worry these packages wont be pushed to github (.gitignore) 
2. Ensure that the backend is running already, then run 
`npm start`



