from aiogram import Router
from user.weath import router as weather_router


router = Router(name=__name__)

router.include_routers(
    weather_router
)