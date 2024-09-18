# Mock
A personalized mock interview platform made for Cornell CS grad students

### Setup

Follow these steps to set up the project locally (for mac):

1. **Project Setup Steps**:
    Within Directory, create virtual enviornment

    ```bash
    python -m venv .venv
    ```

    Activate virtual environment

    ```bash
    source .venv/bin/activate
    ```
    
    On Windows:

     ```bash
     .venv\Scripts\activate
     ```

   Install the dependencies  `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

# Google OAuth Credentials
GOOGLE_CLIENT_ID=47956808419-av54hlrva3685lpalum20dr73e183qg5.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=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

# Session Secret (used by SessionMiddleware)
SESSION_SECRET=your-secure-random-secret