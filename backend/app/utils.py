from fastapi import Request, HTTPException

def get_current_user(request: Request):
    user = request.session.get('user')
    print(user)
    print("Session data in get_current_user:", request.session)
    if not user:
        # Raise a 401 Unauthorized exception if the user is not authenticated
        raise HTTPException(status_code=401, detail="Not authenticated")
    google_id = user.get("sub")
    return google_id