
from fastapi import FastAPI
from .routes import auth_routes, inventory_routes

app = FastAPI()

app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(inventory_routes.router, prefix="/inventory", tags=["inventory"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Food Inventory API"}
