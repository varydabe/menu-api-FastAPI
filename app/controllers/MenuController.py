from starlette.requests import Request
from starlette.responses import JSONResponse

from app import response
from app.models.food import Foods
from app.models.drink import Drinks
from app.transformers import MenuTransformer

class MenuController:
    @staticmethod
    async def store(request: Request) -> JSONResponse:
        try:
            body = await request.json()
            nama = body['nama']
            harga = body['harga']
            kategori = body['kategori']

            menu = Foods() if kategori == "food" else Drinks()
            menu.nama = nama
            menu.harga = harga
            menu.save()

            menus = MenuTransformer.single_transform(menu)
            return response.ok(menus, "Berhasil menambahkan menu!")

        except Exception as e:
            return response.bad_request('', f'{e}')

    @staticmethod
    async def index(request: Request, kategori: str) -> JSONResponse:
        try:
            menus = Foods if kategori == "food" else Drinks
            menus = menus.objects.all()
            menus = MenuTransformer.transform(menus)
            return response.ok(menus, '')

        except Exception as e:
            return response.bad_request('', f'{e}')

    @staticmethod
    async def show(kategori: str, id: str) -> JSONResponse:
        try:
            menu = Foods if kategori == "food" else Drinks
            menu = menu.objects(id=id).first()

            if menu is None:
                raise Exception('Menu tidak ditemukan!')

            menus = MenuTransformer.single_transform(menu)
            return response.ok(menus, "")
        except Exception as e:
            return response.bad_request('', f'{e}')

    @staticmethod
    async def update(kategori: str, id: str, request: Request) -> JSONResponse:
        try:
            body = await request.json()
            nama = body['nama']
            harga = body['harga']

            menu = Foods if kategori == "food" else Drinks
            menu = menu.objects(id=id).first()

            if menu is None:
                raise Exception('Menu tidak ditemukan!')

            menu.nama = nama
            menu.harga = harga
            menu.save()

            menus = MenuTransformer.single_transform(menu)
            return response.ok(menus, "Berhasil mengubah menu!")
        except Exception as e:
            return response.bad_request('', f'{e}')

    @staticmethod
    async def delete(kategori: str, id: str) -> JSONResponse:
        try:
            menu = Foods if kategori == "food" else Drinks
            menu = menu.objects(id=id).first()

            if menu is None:
                raise Exception('Menu tidak ditemukan!')

            menu.delete()
            return response.ok('', "Berhasil menghapus menu!")
        except Exception as e:
            return response.bad_request('', f'{e}')

