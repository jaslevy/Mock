from authlib.integrations.starlette_client import OAuth
import os

# OAUTH situation: 
def google_oauth():
    oauth = OAuth()
    oauth.register(
        name='google',
        client_id=os.environ.get('GOOGLE_CLIENT_ID'),
        client_secret=os.environ.get('GOOGLE_CLIENT_SECRET'),
        authorize_url="https://accounts.google.com/o/oauth2/auth",
        access_token_url="https://accounts.google.com/o/oauth2/token",
        redirect_uri="http://127.0.0.1:8000/auth/callback",

        access_token_params=None,
        authorize_params=None,
        api_base_url='https://www.googleapis.com/oauth2/v1/',
        client_kwargs={'scope': 'openid email profile'},
        # server_metadata_url= 'https://accounts.google.com/.well-known/openid-configuration'
        jwks_uri = "https://www.googleapis.com/oauth2/v3/certs"
    )
    return oauth