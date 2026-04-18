# Shopify Image Manager (Render Ready)

## Setup

1. Copy `.env.example` to `.env`
2. Fill Shopify credentials

## Run locally
uvicorn app.main:app --reload

## Deploy on Render
Start command:
uvicorn app.main:app --host 0.0.0.0 --port 10000
