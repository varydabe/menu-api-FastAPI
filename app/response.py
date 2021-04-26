from starlette import status
from starlette.responses import JSONResponse


def ok(values, message):
    return JSONResponse(status_code=status.HTTP_200_OK, content={"values": values, "message": message})


def bad_request(values, message):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"values": values, "message": message})