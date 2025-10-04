provider "aws" {
    region = "us-east-1"
}

resource "aws_s3_bucket" "cryptoData" {
    bucket = "gg-crypto-data"
    acl = "private"
}