#!/bin/bash

# Prompt the user for the required parameters
read -p "App Name: " APP_NAME
read -p "App version: " APP_VERSION
read -p "New GitHub Repo Name: " REPO_NAME

git init
git add .
git commit -s -m 'Initial commit'
gh repo create "https://github.com/NoeSamaille/$REPO_NAME" --public -s .
git push -u origin main

# Execute the command with the provided parameters
ibmcloud ce app create \
  --name "$APP_NAME" \
  --build-commit main \
  --build-source "https://github.com/NoeSamaille/$REPO_NAME" \
  --cpu 0.25 \
  --memory 500M \
  --min-scale 1 \
  --max-scale 1 \
  --image "quay.io/noesamaille0/pmo-api:$APP_VERSION" \
  --registry-secret quay-noesamaille0 \
  --env-from-secret watsonx-creds-eu-de-ns
