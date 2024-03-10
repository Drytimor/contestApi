from fastapi import APIRouter

registration_router = APIRouter(
    prefix='/registration',
    tags=['registration']
)

@registration_router.post('/')
async def register():
    return {'message': 'user registration successful'}

