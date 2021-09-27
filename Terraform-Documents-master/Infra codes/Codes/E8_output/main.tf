provider "aws" {
    region = var.AWS_REGION
}

resource "aws_instance" "ec2_instance" {
    ami = var.AMI
    instance_type = "t2.micro"
    tags = {Name = "CASSANDRA_SERVER"}
}
