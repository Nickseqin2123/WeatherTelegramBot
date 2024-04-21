from aiogram import Router
from register import router as register_router
from weather import router as weather_router
from delete_punct import router as delete_router
from fact import router as fact_router
from weather_for_ten import router as weather_for_ten_router


router = Router(name=__name__)

router.include_routers(
    register_router,
    weather_router,
    delete_router,
    fact_router,
    weather_for_ten_router
    )