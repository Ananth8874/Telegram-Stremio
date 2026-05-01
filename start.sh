#!/bin/bash

set -e  # Exit immediately on any error

echo "========================================="
echo "Starting Telegram-Stremio Application"
echo "========================================="

# Validate critical environment variables
echo "Validating configuration..."

if [ -z "$BOT_TOKEN" ]; then
    echo "❌ ERROR: BOT_TOKEN environment variable is not set"
    exit 1
fi

if [ -z "$DATABASE" ]; then
    echo "❌ ERROR: DATABASE environment variable is not set"
    exit 1
fi

if [ -z "$API_ID" ] || [ "$API_ID" = "0" ]; then
    echo "❌ ERROR: API_ID environment variable is not set"
    exit 1
fi

if [ -z "$API_HASH" ]; then
    echo "❌ ERROR: API_HASH environment variable is not set"
    exit 1
fi

echo "✅ All required environment variables are set"

echo ""
echo "Running update process..."
if uv run update.py; then
    echo "✅ Update completed successfully"
else
    echo "⚠️  Update encountered an issue, but continuing with startup..."
fi

echo ""
echo "Starting application..."
echo "========================================="

# Execute the main application
exec uv run -m Backend
