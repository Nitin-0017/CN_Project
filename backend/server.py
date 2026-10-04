#!/usr/bin/env python3
"""Simple Phase 1 backend. Uses only the Python standard library."""
import argparse
import hashlib
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def do_GET(self):
        self.respond(False)

    def do_HEAD(self):
        self.respond(True)

    def respond(self, head):
        path = urlsplit(self.path).path
        cached = path == "/api/cache"
        if path == "/":
            data, status = {"backend": self.server.backend, "status": "ok", "message": "CN Phase 1 service running"}, 200
        elif path == "/api/status":
            data, status = {"backend": self.server.backend, "status": "ok"}, 200
        elif cached:
            # Same resource on A and B so conditional caching works through round-robin.
            data, status = {"project": "CN Phase 1", "resource": "shared-cache-demo", "version": 1}, 200
        else:
            data, status = {"error": "not found", "backend": self.server.backend}, 404
        body = (json.dumps(data, sort_keys=True) + "\n").encode()
        etag = '"' + hashlib.sha256(body).hexdigest() + '"'
        supplied = self.headers.get("If-None-Match", "")
        tags = [t.strip().removeprefix("W/") for t in supplied.split(",")]
        if cached and ("*" in tags or etag in tags):
            status = 304
        self.send_response(status)
        self.send_header("X-Backend", self.server.backend)
        self.send_header("Cache-Control", "public, max-age=60" if cached else "no-store")
        if cached:
            self.send_header("ETag", etag)
        if status != 304:
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if not head and status != 304:
            self.wfile.write(body)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--backend", choices=["A", "B"], required=True)
    parser.add_argument("--port", type=int, required=True)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("0.0.0.0", args.port), Handler)
    server.backend = args.backend
    print(f"Backend {args.backend} listening on 0.0.0.0:{args.port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()

if __name__ == "__main__":
    main()
