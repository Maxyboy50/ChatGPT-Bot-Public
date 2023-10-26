variable "lambda_name" {
  description = "This will be the name that lambda function is assigned"
  type        = string
}

variable "lambda_packages_bucket" {
  description = "S3 bucket where lambda deployment packages and layer zips are stored"
  type        = string
}

variable "dynamodb_table_name" {
  description = "Name of DynamoDB table to create"
  type        = string
}

variable "lambda_layer_zip_path" {
  description = "Path to the lambda_layers zip"
  type        = string
}

variable "lambda_code_zip_path" {
  description = "Path to lambda_code zip"
  type        = string
}

variable "PUBLIC_KEY" {
  description = "Discord application public key (used to verify signatures from interactions)"
  type        = string
  default     = ""
  sensitive   = true
}

variable "API_KEY" {
  description = "OpenAI API Key used for making API calls"
  type        = string
  default     = ""
  sensitive   = true
}

variable "WEBHOOK_URL" {
  description = "Webhook URL to send discord messages to."
  type = string
  default = ""
  sensitive = true
}