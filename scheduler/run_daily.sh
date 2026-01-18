#!/bin/bash

# -----------------------------------
# Daily Bestseller Tracker Runner
# -----------------------------------

echo "Starting Bestseller Tracker..."

cd /path/to/your/project/bestseller-tracker || exit 1

source venv/bin/activate

python main.py

echo "Bestseller Tracker completed."
