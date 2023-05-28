data "aws_s3_bucket" "this" {
  bucket = var.lambda_packages_bucket
}

resource "aws_s3_object" "general_packages" {
  bucket      = data.aws_s3_bucket.this.id
  key         = "general_packages.zip"
  source      = var.lambda_layer_zip_path
  source_hash = filemd5(var.lambda_layer_zip_path)

}

resource "aws_s3_object" "deployment_package" {
  bucket = data.aws_s3_bucket.this.id
  key    = "deployment_package.zip"
  source = var.lambda_code_zip_path

}