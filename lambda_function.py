import boto3
from datetime import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    textract = boto3.client('textract')
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    
    # Only process PDFs
    if file_key.lower().endswith('.pdf'):
        print(f"Processing: {file_key}")
        
        # Extract text from PDF
        response = textract.detect_document_text(
            Document={'S3Object': {'Bucket': bucket, 'Name': file_key}}
        )
        
        extracted_text = "\n".join([item['Text'] for item in response['Blocks'] if item['BlockType'] == 'LINE'])
        print(f"Extracted text: {extracted_text}")
        
        # Save to DynamoDB 
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('ExtractedText')
        
        table.put_item(Item={
            'file_name': file_key,
            'text': extracted_text,
            'timestamp': str(datetime.now())
        })
        
    return {
        'statusCode': 200,
        'body': 'Text extracted successfully!'
    }
