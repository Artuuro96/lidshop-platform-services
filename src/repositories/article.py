import time
from typing import List

from src.models.article import ArticleDetail
from fastapi import HTTPException
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from configuration import db
from src.schemas.article import ArticleSchema
from src.repositories.brand import get_brand_by_id


async def create_article(article: ArticleSchema):
    collection = db["articles"]
    article_dict = jsonable_encoder(article)
    new_article = collection.insert_one(article_dict)
    created_article = collection.find_one({"_id": new_article.inserted_id})
    return created_article


async def get_article_by_id(article_id: str) -> ArticleDetail:
    collection = db["articles"]
    article_dict = collection.find_one({
        "_id": ObjectId(article_id)
    })

    if not article_dict:
        raise HTTPException(status_code=404, detail=f'Article with id {article_id} not found')

    if 'brandId' not in article_dict:
        raise HTTPException(status_code=404, detail='Brand ID not found in article')

    brand_dict = await get_brand_by_id(article_dict['brandId'])

    article_detail = ArticleDetail(
        _id=str(article_dict['_id']),
        name=article_dict['name'],
        code=article_dict['code'],
        tax=article_dict['tax'],
        ticketPrice=article_dict['ticketPrice'],
        parcel=article_dict['parcel'],
        lidShopPrice=article_dict['lidShopPrice'],
        otherCosts=article_dict['otherCosts'],
        profit=article_dict['profit'],
        status=article_dict['status'],
        brand=brand_dict
    )

    return article_detail


async def get_all_articles():
    collection = db["articles"]
    articles = collection.find({})
    return articles


async def get_article_by_keyword(keyword: str):
    collection = db["articles"]
    articles = collection.find({
        "name": {
            "$regex": keyword,
            "$options": "i"
        }
    })
    return articles


async def update_article(article_id: str, article: ArticleSchema):
    collection = db["articles"]
    article_dict = jsonable_encoder(article)
    result = collection.update_one(
        {'_id': ObjectId(article_id)},
        {'$set': article_dict}
    )
    if result.modified_count != 1:
        raise HTTPException(status_code=500, detail=f'Unable to update the article ${article_id}')
    return result


async def delete_article(article_ids: List[str]):
    collection = db["articles"]
    result = []
    for article_id in article_ids:
        delete_result = collection.delete_one(
            {'_id': ObjectId(article_id)}
        )
        if delete_result.deleted_count == 1:
            result.append(article_id)
    return result
