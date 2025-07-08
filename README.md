# AWS PDF Text Extractor (Serverless Automation)

Automatically extracts text from uploaded PDFs using AWS serverless architecture.

## Architecture  
1. **S3 Trigger**: Upload PDFs to an S3 bucket  
2. **Lambda Processing**: Python function triggers automatically  
3. **Textract**: AWS AI service extracts text  
4. **DynamoDB**: Stores extracted text with timestamps  

## How to Deploy
1. Create S3 bucket: `yourname-file-upload`
2. Create Lambda with Python 3.9
3. Attach IAM roles for Textract/DynamoDB access
4. Set up S3 event trigger

## Screenshots  
![Lambda Processing Logs](images/lambda-logs.png)  
![DynamoDB Extracted Data](images/dynamodb-results.png)  
![S3 Bucket with PDFs](images/s3-bucket.png)  

## Technical Skills  
- **AWS Services**: Lambda, S3, Textract, DynamoDB  
- **Python**: Boto3 for AWS integration  
- **Serverless Design**: Zero infrastructure management

## Notes  
- Project resources deleted post-demo to optimize costs.  
- Code can be reused for document processing workflows.
  
## Quick Deployment  
1. Clone this repo  
2. Deploy `lambda_function.py` with S3/DynamoDB permissions  
3. Set up S3 bucket trigger
   
## Key Learnings  
- Serverless event-driven architectures  
- AWS service integration (Lambda, Textract)  
- Cloud cost optimization

## GDPR Considerations
- Auto-deletion policies (`force_destroy = true`)  
- No personal data processed  
- Resources destroyed post-demo  

## Nederlandse Samenvatting  
Dit project automatiseert tekstherkenning van PDFs met AWS serverless diensten.  

