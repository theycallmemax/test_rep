from admin import router as admin_router
from auth import router as auth_router
from billing import router as billing_router
from fastapi import APIRouter
from prediction import router as predicting_router

routers = APIRouter()


@routers.get(
    path="/health",
    tags=["Health"],
)
async def health() -> str:
    return "I am alive"


router_list = [admin_router, auth_router, billing_router, predicting_router]

for router in router_list:
    # router.tags = routers.tags.append("v1")
    routers.include_router(router)
