#!/bin/bash
# 🎁 arranca la app generada en 1 comando
pip install fastapi uvicorn -q
python -m uvicorn api:app --port 8000 &
echo "API: http://localhost:8000/docs · UI: abre index.html"
