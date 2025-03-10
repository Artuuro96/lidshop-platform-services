from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from pymongo.errors import DuplicateKeyError, PyMongoError
from src.auth.auth import auth_request
from src.routers import article, client, brand, sale, payment
from fastapi.middleware.cors import CORSMiddleware

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


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PUT"],
    allow_headers=["*"],
)

app.include_router(article.router, prefix="/articles", tags=["Articles"], dependencies=[Depends(auth_request)])
app.include_router(client.router, prefix="/clients", tags=["Clients"], dependencies=[Depends(auth_request)])
app.include_router(brand.router, prefix="/brands", tags=["Brands"], dependencies=[Depends(auth_request)])
app.include_router(sale.router, prefix="/sales", tags=["Sales"], dependencies=[Depends(auth_request)])
app.include_router(payment.router, prefix="/payments", tags=["Payments"], dependencies=[Depends(auth_request)])
