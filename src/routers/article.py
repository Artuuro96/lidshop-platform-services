from typing import List, Optional, Literal

from fastapi import APIRouter, HTTPException, status, UploadFile, Query, Form, File
from src.models.article import Article, ArticleDetail, ArticleResponseDeleted
from src.schemas.article import ArticleSchema
from src.repositories.article import (
    create_article,
    get_all_articles,
    get_article_by_id,
    get_article_by_keyword,
    update_article,
    delete_article
)
from src.repositories.brand import (
    get_brand_by_id
)
from src.services.spaces import DOSpaces

router = APIRouter()


@router.post("", response_model=Article, status_code=status.HTTP_201_CREATED)
async def create(article: ArticleSchema):
    brand = await get_brand_by_id(article.brand_id)

    if not brand:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, f"Brand {article.brand_id} does not exist")

    new_article = await create_article(article)
    return new_article


@router.post("/bulk")
async def create_many(file: UploadFile):
    return {"filename": file.filename}


@router.post("/image", status_code=status.HTTP_201_CREATED)
async def post_image(file: UploadFile = File(...)):
    dos_space_service = DOSpaces()
    await dos_space_service.put_object(file.file, "lid-shop", file.filename, file.content_type)
    return {
        "url": f"https://lid-shop.nyc3.digitaloceanspaces.com/images/{file.filename}"
    }


@router.get("", response_model=List[Article])
async def get_all():
    articles = await get_all_articles()
    return articles


@router.get("/{article_id}", response_model=ArticleDetail)
async def get_by_id(article_id: str) -> ArticleDetail:
    article = await get_article_by_id(article_id)
    return article


@router.get("/", response_model=List[Article])
async def get_by_keyword(keyword: str):
    articles = await get_article_by_keyword(keyword)
    return articles


@router.put("/{article_id}", response_model=Article)
async def update_by_id(article_id: str, article: ArticleSchema):
    article_updated = await update_article(article_id, article)
    print(article_updated)
    return {}


@router.delete("/", status_code=status.HTTP_200_OK, response_model=ArticleResponseDeleted)
async def delete_by_ids(article_ids: List[str] = Query(...)):
    deleted_ids = await delete_article(article_ids)
    return {
        "deletedIds": deleted_ids
    }
