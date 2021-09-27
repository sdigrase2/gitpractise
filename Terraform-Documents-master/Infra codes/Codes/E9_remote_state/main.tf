# Provider :
provider "aws" {
    region = var.AWS_REGION
}

resource "aws_instance" "http" {
    ami = "ami-052c08d70def0ac62"
    instance_type = "t2.micro"
    tags = {Name = "HTTPS_SERVER_PROD"}
}