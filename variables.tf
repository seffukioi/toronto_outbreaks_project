variable "project" {
  description = "Project"
  default = "toronto-outbreaks-project"
}

variable "location" {
  description = "location"
  default = "US"
}

variable "region" {
  description = "Region"
  default = "us-central1"
}

variable "credentials" {
  description = "Credentials"
  default = "./keys/toronto-outbreaks-project.json"
}

variable "dataset" {
  description = "Dataset"
  default = "toronto_outbreaks_dataset"
}

variable "bucket" {
  description = "Bucket"
  default = "toronto-outbreaks-bucket"
}