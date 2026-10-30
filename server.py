#!/usr/bin/env python3
"""PWA Manifest Studio Sovereign Server Launcher."""
import os
import sys
from pathlib import Path

# Add src to pythonpath
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR / "src"))

from pwa_manifest_builder.ui_server import start_ui_server

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="PWA Manifest Studio Server")
    parser.add_argument("--host", default="127.0.0.1", help="Host interface to bind")
    parser.add_argument("--port", "-p", type=int, default=8100, help="Port to listen on (default: 8100)")
    parser.add_argument("--open", "-o", action="store_true", help="Open browser")
    args = parser.parse_args()

    print(f"Starting PWA Manifest Studio on {args.host}:{args.port}...")
    start_ui_server(host=args.host, port=args.port, open_browser=args.open)
