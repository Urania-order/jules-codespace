#!/usr/bin/env bash

set -e

echo "🧠 AI Codespace bootstrap starting..."

# Node detect/install
if ! command -v node >/dev/null 2>&1; then
    echo "⚙️ Node not found → installing..."

    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    sudo apt-get update
    sudo apt-get install -y nodejs
fi

echo "✅ Node: $(node -v)"
echo "✅ npm: $(npm -v)"

# Jules install
if ! command -v jules >/dev/null 2>&1; then
    echo "⚙️ Installing @google/jules..."
    npm install -g @google/jules || echo "⚠️ jules install failed"
fi

# workspace
mkdir -p workspace

echo "🧪 System ready"
