terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
  }
}

provider "local" {}

resource "local_file" "devops_info" {
  filename = "devops-output.txt"

  content = "Terraform successfully created this file."
}
