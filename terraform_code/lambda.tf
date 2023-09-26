resource "aws_lambda_function" "this" {
  function_name = var.lambda_name
  description   = <<EOT
    ChatGPT Discord Bot. Interacts with the ChatGPT API as well as Discord API to provide an interface between the two.
    This Bot stores message history in DynamoDB utilizing Boto3.
    This Bot is written in Python.
    EOT
  handler       = "main.lambda_handler"
  runtime       = "python3.10"
  memory_size   = 1024
  timeout       = 300

  s3_bucket         = var.lambda_packages_bucket
  s3_key            = aws_s3_object.deployment_package.id
  s3_object_version = aws_s3_object.deployment_package.version_id
  role              = aws_iam_role.this.arn
  layers            = [aws_lambda_layer_version.this.arn]
  environment {
    variables = {
      TABLE_NAME  = aws_dynamodb_table.this.name
      API_KEY     = var.API_KEY
      PUBLIC_KEY  = var.PUBLIC_KEY
      WEBHOOK_URL = var.WEBHOOK_URL
    }
  }
}


resource "aws_lambda_permission" "this" {
  statement_id  = "AllowInvocationFromAPIGW"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.this.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.this.execution_arn}/*/*/${aws_lambda_function.this.function_name}"
}


resource "aws_lambda_layer_version" "this" {
  layer_name          = "DiscordBot"
  description         = "All the required packages to operate the ChatGPT Discord bot (may split eventually for modularity)"
  s3_bucket           = data.aws_s3_bucket.this.id
  s3_key              = aws_s3_object.general_packages.id
  s3_object_version   = aws_s3_object.general_packages.version_id
  compatible_runtimes = ["python3.10"]

}