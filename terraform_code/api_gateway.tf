resource "aws_apigatewayv2_api" "this" {
  name                         = "ChatGPTDiscordAPI"
  protocol_type                = "HTTP"
  disable_execute_api_endpoint = false
  cors_configuration {
    allow_origins = toset(["*"])
  }
}
resource "aws_apigatewayv2_stage" "this" {
  api_id      = aws_apigatewayv2_api.this.id
  name        = "deployment"
  auto_deploy = true

}

resource "aws_apigatewayv2_integration" "this" {
  api_id           = aws_apigatewayv2_api.this.id
  integration_type = "AWS_PROXY"

  connection_type      = "INTERNET"
  description          = "Invoke ChatGPT Lambda with events from API Gateway"
  integration_method   = "POST"
  integration_uri      = aws_lambda_function.this.invoke_arn
  passthrough_behavior = "WHEN_NO_MATCH"
}

resource "aws_apigatewayv2_route" "POST" {
  api_id    = aws_apigatewayv2_api.this.id
  route_key = "POST /${aws_lambda_function.this.function_name}"

  target = "integrations/${aws_apigatewayv2_integration.this.id}"
}

resource "aws_apigatewayv2_route" "GET" {
  api_id    = aws_apigatewayv2_api.this.id
  route_key = "GET /${aws_lambda_function.this.function_name}"

  target = "integrations/${aws_apigatewayv2_integration.this.id}"
}