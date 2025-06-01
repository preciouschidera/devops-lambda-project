import json

def lambda_handler(event, context):
    print("Event received.")
    print(json.dumps(event))

    # If S3 upload triggered this
    if 'Records' in event and 's3' in event['Records'][0]:
        s3_info = event['Records'][0]['s3']
        bucket = s3_info['bucket']['name']
        key = s3_info['object']['key']

        message = (
            f"📁 File Upload Notification:\n"
            f"🪣 Bucket: {bucket}\n"
            f"📄 File Name: {key}\n"
            f"🚀 Triggered via AWS Lambda & Terraform by Precious\n"
            f"💜 Built with love."
        )

        print(message)
        return {
            'statusCode': 200,
            'body': json.dumps('Lambda executed for file upload. Check logs.')
        }

    # If accessed via HTTP (API Gateway)
    return {
        'statusCode': 200,
        'body': json.dumps('🎉 Hello from Precious! Lambda is working with API Gateway.')
    }



