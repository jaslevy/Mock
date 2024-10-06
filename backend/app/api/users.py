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
    
@router.get("/users/{username}")
async def get_user_profile(username: str):
    """Get the profile details of a user."""
    try:
        user = User.objects.get(username=username)
        return JSONResponse(content={'username': user.username, 'first_name': user.first_name, 
                                     'last_name': user.last_name, 'email': user.email,
                                     'bio': user.bio, 'profile_image': user.profile_image}, 
                            status_code=200)
    except User.DoesNotExist:
        raise HTTPException(status_code=404, detail='User does not exist')

### editing endpoints
    
@router.patch("/users/{username}/bio")
async def edit_user_bio(username: str, bio: str = Form(...)):
    """Edit the bio of a user."""
    try:
        user = User.objects.get(username=username)
        user.bio = bio
        user.bio_embedding = requests.post('https://ai-service.com/embedding', json={'text': bio}).json()
        user.save()
        return JSONResponse(content={'message': 'Bio updated successfully'}, status_code=200)
    except User.DoesNotExist:
        raise HTTPException(status_code=404, detail='User does not exist')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@router.patch("/users/{username}/name")
async def edit_user_name(username: str, first_name: str = Form(...), last_name: str = Form(...)):
    """Edit the name of a user."""
    try:
        user = User.objects.get(username=username)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return JSONResponse(content={'message': 'Name updated successfully'}, status_code=200)
    except User.DoesNotExist:
        raise HTTPException(status_code=404, detail='User does not exist')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@router.patch("/users/{username}/email")
async def edit_user_email(username: str, email: str = Form(...)):
    """Edit the email of a user."""
    try:
        user = User.objects.get(username=username)
        user.email = email
        user.save()
        return JSONResponse(content={'message': 'Email updated successfully'}, status_code=200)
    except User.DoesNotExist:
        raise HTTPException(status_code=404, detail='User does not exist')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    
@router.patch("/users/{username}/availability")
async def edit_user_availability(username: str, availability: int = Form(...)):
    """Edit the availability of a user."""
    try:
        user = User.objects.get(username=username)
        if availability not in [0,1,2]:
            raise HTTPException(status_code=400, detail='Availability must be 0, 1, or 2')
        user.availability = availability
        user.save()
        return JSONResponse(content={'message': 'Availability updated successfully'}, status_code=200)
    except User.DoesNotExist:
        raise HTTPException(status_code=404, detail='User does not exist')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
