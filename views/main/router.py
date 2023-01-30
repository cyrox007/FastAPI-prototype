from fastapi import APIRouter, status
from views.main import handlers


main_router = APIRouter(tags=['Payments'])
main_router.add_api_route(
    '/',
    methods=['GET'],
    status_code=status.HTTP_200_OK,
    endpoint=handlers.site_init
)
