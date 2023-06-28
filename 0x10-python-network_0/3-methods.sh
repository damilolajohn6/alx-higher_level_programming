#!/bin/bash

if [ -z "$1" ]; then
  echo "Error: Please provide a URL as an argument."
  exit 1
fi

allow_methods=$(curl -sI "$1" | awk -F ": " '/Allow/ {print $2}' | tr -d '\r')

if [ -z "$allow_methods" ]; then
  echo "Error: Unable to retrieve the supported HTTP methods."
  exit 1
fi

echo "Supported HTTP Methods: $allow_methods"
