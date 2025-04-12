from utility.logger import get_logger
from run_spider import run_scrapy

logger = get_logger()

def lambda_handler(event, context):
    try:
        result = run_scrapy()
        # upload_to_s3("my-bucket", "results/data.json", result)
        logger.info("Scraping and upload successful!")
        return {"statusCode": 200, "body": "Done"}
    except Exception as e:
        logger.error(f"Failed: {str(e)}")
        return {"statusCode": 500, "body": str(e)}
    

lambda_handler(None, None)
