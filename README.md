# EX01 Developing a Simple Webserver
## Date: 02/10/2025

## AIM:
To develop a simple webserver to serve html pages and display the Device Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = 'localhost'
PORT = 8080

HTML_CONTENT = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Web Server Experiment</title>
</head>
<body>
    <h1 align="center">Specifications of my Laptop</h1>
    <p> My Laptop is Asus VivoBook 15 F1504VA. It has the following specifications:</p>
    <ul>
        <li>Processor: Intel Core i5-1334U</li>
        <li>RAM: 8GB DDR4(Expandable)</li>
        <li>Storage: 512GB SSD</li>
        <li>Display: 15.6-inch Full HD</li>
        <li>Operating System: Windows 11</li>
    </ul>
    <p>It is a lightweight and portable laptop suitable for everyday tasks and light gaming.</p>
    
    <p>Thank you!</p>


</body>
</html>

"""

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(HTML_CONTENT.encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer((HOST, PORT), SimpleHandler)
    print(f"Serving on http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        server.server_close()
```

## OUTPUT:
![alt text](<Screenshot 2025-10-02 193800.png>)    
![alt text](<Screenshot 2025-10-02 193739.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
