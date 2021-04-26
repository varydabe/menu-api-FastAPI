from fastapi import APIRouter
from starlette.requests import Request

from app.controllers.MenuController import MenuController as controller

router = APIRouter()


@router.post("", tags=["menus"])
async def action(request: Request):
    return await controller.store(request)


@router.get("/{kategori}", tags=["menus"])
async def action(request: Request, kategori: str):
    return await controller.index(request, kategori)


@router.get("/{kategori}/{id}", tags=["menus"])
async def action(kategori: str, id: str):
    return await controller.show(kategori, id)


@router.put("/{kategori}/{id}", tags=["menus"])
async def action(kategori: str, id: str, request: Request):
    return await controller.update(kategori, id, request)


@router.delete("/{kategori}/{id}", tags=["menus"])
async def action(kategori: str ,id: str):
    return await controller.delete(kategori, id)