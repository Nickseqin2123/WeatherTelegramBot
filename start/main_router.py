from aiogram import Router
from user.register import router as register_router
from user.weath import router as weather_router
from user.callbacks.navigate import router as navigate_callback_router


router = Router(name=__name__)

router.include_routers(
    weather_router,
    register_router,
    navigate_callback_router
)