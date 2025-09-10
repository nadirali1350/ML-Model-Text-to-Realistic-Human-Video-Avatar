#!/usr/bin/env bash
set -euo pipefail

if command -v python3 >/dev/null 2>&1; then
    PY=python3
else
    PY=python
fi
$PY -m pip install --upgrade pip
$PY -m pip install -r /workspace/requirements.txt
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
