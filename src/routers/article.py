from typing import List
from fastapi import APIRouter, HTTPException, status, UploadFile
from src.models.article import Article, ArticleDetail
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
    print("=========>", keyword)
    articles = await get_article_by_keyword(keyword)
    return articles


@router.put("/{article_id}", response_model=Article)
async def update_by_id(article_id: str, article: ArticleSchema):
    article_updated = await update_article(article_id, article)
    print(article_updated)
    return {}


@router.delete("/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_by_id(article_id: str):
    await delete_article(article_id)
    return None
