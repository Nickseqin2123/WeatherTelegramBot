from aiogram import Router
from user.register import router as register_router
from user.weath import router as weather_router
from user.callbacks.user_callbacks import router as navigate_callback_router
from user.support import router as support_router
from user.callbacks.support_callback import router as support_callback_router


router = Router(name=__name__)

router.include_routers(
    weather_router,
    register_router,
    navigate_callback_router,
    support_router,
    support_callback_router
    )