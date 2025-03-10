import base64
import aioboto3
from decouple import config


class DOSpaces:
    def __init__(self):
        self.session = aioboto3.Session()
        self.client = None

    async def connect(self):
        if self.client is None:
            self.client = self.session.client(
                's3',
                region_name=config("LID_SHOP_BUCKET_REGION"),
                endpoint_url="https://nyc3.digitaloceanspaces.com",
                aws_access_key_id=config("LID_SHOP_BUCKET_ACCESS"),
                aws_secret_access_key=config("LID_SHOP_BUCKET_SECRET")
            )

    async def get_buckets(self):
        async with self.client as s3_client:
            response = await s3_client.list_buckets()
            spaces = [space['Name'] for space in response['Buckets']]
            return spaces

    async def get_object_by_key(self, key: str, bucket: str):
        async with self.client as s3_client:
            response = await s3_client.get_object(Bucket=bucket, Key=key)
            image_data = await response['Body'].read()
            image_base64 = base64.b64encode(image_data).decode('utf-8')
            return image_base64

    async def put_object(self, base64_image, bucket, key, content_type):
        if self.client is None:
            await self.connect()

        async with self.client as s3_client:
            response = await s3_client.put_object(
                Bucket=bucket,
                Key=f"images/{key}",
                Body=base64_image,
                ACL='public-read',
                ContentType=content_type
            )

        return response
