
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

resource "aws_instance" "devserver" {
  ami           = "ami-09e67e426f25ce0d7"
  instance_type = "t2.micro"

  tags = {
    Name = "dev_server"
  }
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}