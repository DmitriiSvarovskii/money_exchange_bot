__all__ = (
    'router'
)

from aiogram import Router

from .base_handler import router as start_router
from .fsm_base import router as fsm_base_router
from .currency_handlers import router as currency_router
from .fsm_rub_handler import router as fsm_rub_router
from .fsm_inr_handler import router as fsm_inr_router
from .fsm_inr_usdt_handler import router as fsm_inr_usdt_router
from .fsm_usdt_inr_handler import router as fsm_usdt_inr_router

router = Router(name=__name__)

router.include_routers(
    start_router,
    currency_router,
    fsm_base_router,
    fsm_rub_router,
    fsm_inr_router,
    fsm_inr_usdt_router,
    fsm_usdt_inr_router,
)
