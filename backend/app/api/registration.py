from fastapi import APIRouter, Request, Form
from fastapi.responses import JSONResponse
from fastapi import HTTPException
import boto3
import requests
from backend.app.models.user_model import User

router = APIRouter()

# Set up S3 client
s3 = boto3.client('s3', aws_access_key_id='YOUR_ACCESS_KEY',
                         aws_secret_access_key='YOUR_SECRET_KEY')

# Define the endpoint
@router.post("/users/")
async def create_user(
    username: str = Form(...),
    first_name: str = Form(...),
    last_name: str = Form(...),
    email: str = Form(...),
    bio: str = Form(...),
    profile_image: UploadFile = File(...),
    # ... other form fields ...
):
    try:
        # Call AI service to generate embedding
        embedding = requests.post('https://ai-service.com/embedding', json={'text': bio}).json()

        # Validate data
        if not validate_data(username, first_name, last_name, email, bio):
            raise HTTPException(status_code=400, detail='Invalid data')

        # Upload profile image to S3
        s3.put_object(Body=profile_image.file, Bucket='your-bucket', Key='profile-image.jpg')
        profile_image_url = f'https://s3.amazonaws.com/your-bucket/profile-image.jpg'

        # Store data in database
        user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            bio=bio,
            bio_embedding=embedding,
            profile_image=profile_image_url,
            interests=interests,
            interest_embedding=interest_embedding,
            availability=availability,
            interview_schedule=interview_schedule,
            friends=friends,
            number_of_mocks=number_of_mocks,
            created_at=datetime.now()
        )
        user.save()
        return JSONResponse(content={'message': 'User created successfully'}, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
