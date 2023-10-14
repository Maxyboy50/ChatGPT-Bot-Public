resource "aws_secretsmanager_secret" "webhook_url" {
  name        = "webhookurl"
  description = "Webhook url to be used when extending past base functionality"

}
resource "aws_secretsmanager_secret" "api_key" {
  name        = "apikey"
  description = "OpenAI API key"

}
resource "aws_secretsmanager_secret" "public_key" {
  name        = "publickey"
  description = "Discord bot public key to be used to authenticate interactions"
}

resource "aws_secretsmanager_secret_version" "webhook_url" {
  secret_id     = aws_secretsmanager_secret.webhook_url.id
  secret_string = var.WEBHOOK_URL
}
resource "aws_secretsmanager_secret_version" "api_key" {
  secret_id     = aws_secretsmanager_secret.api_key.id
  secret_string = var.API_KEY
}
resource "aws_secretsmanager_secret_version" "public_key" {
  secret_id     = aws_secretsmanager_secret.public_key.id
  secret_string = var.PUBLIC_KEY
}


data "aws_secretsmanager_secret_version" "webhook_url" {
  secret_id = aws_secretsmanager_secret_version.webhook_url.id
  depends_on = [ aws_secretsmanager_secret.webhook_url ]
}
data "aws_secretsmanager_secret_version" "public_key" {
  secret_id = aws_secretsmanager_secret_version.public_key.id
  depends_on = [ aws_secretsmanager_secret.public_key ]
}
data "aws_secretsmanager_secret_version" "api_key" {
  secret_id = aws_secretsmanager_secret_version.api_key.id
  depends_on = [ aws_secretsmanager_secret.api_key ]
}