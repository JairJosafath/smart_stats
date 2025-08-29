def handler(event, context):
    extracted_info = f"mocked_info from image located at {event['image_location']}"
    body: dict = {
        "extracted_info": extracted_info
    }
    
    return {"statusCode": 200, "body": body}