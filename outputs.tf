output "lambda_function_name" {
  value = aws_lambda_function.lambda_func.function_name
}

output "s3_bucket_name" {
  value = aws_s3_bucket.upload_bucket.bucket
}

output "api_endpoint" {
  value = aws_apigatewayv2_api.lambda_api.api_endpoint
  description = "API Gateway URL"
}

