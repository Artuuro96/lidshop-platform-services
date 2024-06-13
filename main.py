from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pymongo.errors import DuplicateKeyError, PyMongoError
from src.routers import article, client, brand

app = FastAPI(
    title='Lid Shop Rest API',
    description='Documentation of the REST API services for Lid Shop platform',
    version='0.0.1',
    dependencies=[]
)


@app.exception_handler(DuplicateKeyError)
async def duplicate_key_exception_handler(request: Request, exc: DuplicateKeyError):
    return JSONResponse(
        status_code=400,
        content={"message": f"Duplicate key error: {exc.details}", "statusCode": 400}
    )


@app.exception_handler(PyMongoError)
async def pymongo_exception_handler(request: Request, exc: PyMongoError):
    return JSONResponse(
        status_code=500,
        content={"message": "An error occurred with the database"}
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": f"An unexpected error occurred: {str(exc)}", "statusCode": 500}
    )


@app.exception_handler(HTTPException)
async def global_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail, "statusCode": exc.status_code}
    )


app.include_router(article.router, prefix="/articles", tags=["Articles"])
app.include_router(client.router, prefix="/clients", tags=["Clients"])
app.include_router(brand.router, prefix="/brands", tags=["Brands"])
