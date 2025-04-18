from aiogram import Router
from user.register import router as register_router
from user.callbacks.callbacks_nav import router as navigate_router
from user.weath import router as weather_router


router = Router(name=__name__)

router.include_routers(
    weather_router,
    navigate_router,
    register_router
)