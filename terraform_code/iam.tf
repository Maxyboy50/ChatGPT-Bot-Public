data "aws_iam_policy_document" "this" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "this" {
  name               = "ChatGPTBotRole"
  description        = "This will provide the ChatGPT Lambda the ability to write to Cloudwatch Logs, as well as Put, Get, and Update items in DynamoDB"
  assume_role_policy = data.aws_iam_policy_document.this.json
  inline_policy {
    name = "ChatGPTPermissions"
    policy = jsonencode({
      "Version" : "2012-10-17",
      "Statement" : [
        {
          "Effect" : "Allow",
          "Action" : "logs:CreateLogGroup",
          "Resource" : "arn:aws:logs:us-east-2:912434042761:*"
        },
        {
          "Effect" : "Allow",
          "Action" : [
            "logs:CreateLogStream",
            "logs:PutLogEvents"
          ],
          "Resource" : [
            "arn:aws:logs:us-east-2:912434042761:log-group:/aws/lambda/${var.lambda_name}:*"
          ]
        },
        {
          "Effect" : "Allow",
          "Action" : [
            "dynamodb:GetItem",
            "dynamodb:UpdateItem",
            "dynamodb:PutItem"
          ],
          "Resource" : [
            "arn:aws:dynamodb:us-east-2:912434042761:table/${aws_dynamodb_table.this.id}"
          ]
        }
      ]
      }
    )
  }
}