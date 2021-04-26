from starlette.requests import Request
from starlette.responses import JSONResponse
from app import response
from app.models.drink import Drinks
from app.transformers import MenuTransformer

class DrinkController:
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

    # FOOD
    @staticmethod
    async def index_food(request: Request) -> JSONResponse:
        try:
            foods = Foods.objects.all()
            foods = MenuTransformer.transform(foods)
            return response.ok(foods, '')

        except Exception as e:
            return response.bad_request('', f'{e}')

    @staticmethod
    async def show_food(id) -> JSONResponse:
        try:
            todo = Todos.objects(id=id).first()

            if todo is None:
                raise Exception('todo tidak ditemukan!')

            todos = TodoTransformer.singleTransform(todo)
            return response.ok(todos, "")
        except Exception as e:
            return response.badRequest('', f'{e}')

    @staticmethod
    async def update_food(id: str, request: Request) -> JSONResponse:
        try:
            body = await request.json()
            title = body['title']
            description = body['description']

            todo = Todos.objects(id=id).first()

            if todo is None:
                raise Exception('todo tidak ditemukan!')

            todo.title = title
            todo.description = description
            todo.save()

            todos = TodoTransformer.singleTransform(todo)
            return response.ok(todos, "Berhasil Mengubah Todo!")
        except Exception as e:
            return response.badRequest('', f'{e}')

    @staticmethod
    async def delete_food(id: str) -> JSONResponse:
        try:
            todo = Todos.objects(id=id).first()

            if todo is None:
                raise Exception('todo tidak ditemukan!')

            todo.delete()
            return response.ok('', "Berhasil menghapusTodo!")
        except Exception as e:
            return response.badRequest('', f'{e}')

    # DRINK
    @staticmethod
    async def index_drink(request: Request) -> JSONResponse:
        try:
            drinks = Drinks.objects.all()
            drinks = MenuTransformer.transform(drinks)
            return response.ok(drinks, '')

        except Exception as e:
            return response.bad_request('', f'{e}')

    @staticmethod
    async def show_food(id) -> JSONResponse:
        try:
            todo = Todos.objects(id=id).first()

            if todo is None:
                raise Exception('todo tidak ditemukan!')

            todos = TodoTransformer.singleTransform(todo)
            return response.ok(todos, "")
        except Exception as e:
            return response.badRequest('', f'{e}')

    @staticmethod
    async def update_food(id: str, request: Request) -> JSONResponse:
        try:
            body = await request.json()
            title = body['title']
            description = body['description']

            todo = Todos.objects(id=id).first()

            if todo is None:
                raise Exception('todo tidak ditemukan!')

            todo.title = title
            todo.description = description
            todo.save()

            todos = TodoTransformer.singleTransform(todo)
            return response.ok(todos, "Berhasil Mengubah Todo!")
        except Exception as e:
            return response.badRequest('', f'{e}')

