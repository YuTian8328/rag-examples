from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes

from app.chains import llm_chain, json_chain, json_limerick_chain, salesman_chain

app = FastAPI()



from fastapi import Request, HTTPException, status
from typing import Optional

# A mock function to validate the API key and return a user object. You should replace this with your actual validation logic.
def get_user_by_api_key(api_key: str) -> Optional[User]:
    # Implement your API key validation logic here
    # For example, lookup the API key in the database and return the user if it matches
    if api_key == "your_valid_api_key":  # Replace with real logic
        return User(username="valid_user", disabled=False)  # Example user object
    return None

async def get_current_active_user_from_request(request: Request) -> User:
    """Get the current active user from the request using an API key."""
    api_key = request.headers.get("X-API-Key")  # Change to the header you use for API keys
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key missing",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user = get_user_by_api_key(api_key)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    
    return user


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

add_routes(
    app,
    llm_chain,
    path='/llm'
)

add_routes(
    app,
    json_chain,
    path='/json'
)

add_routes(
    app,
    json_limerick_chain,
    path='/limerick'
)


add_routes(
    app,
    salesman_chain,
    path='/salesman'
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
