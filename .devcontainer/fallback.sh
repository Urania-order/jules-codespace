#!/usr/bin/env bash

echo "🚨 FALLBACK MODE ACTIVATED"

curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get update
sudo apt-get install -y nodejs npm

npm install -g @google/jules

echo "✅ fallback ready"
bash
