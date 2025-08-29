from flask import Flask, Response
from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST
import psutil

app = Flask(__name__)

REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')
CPU_USAGE     = Gauge('cpu_usage_percent',   'CPU Usage Percentage')
MEMORY_USAGE  = Gauge('memory_usage_percent','Memory Usage Percent')
DISK_USAGE    = Gauge('disk_usage_percent',  'Disk Usage Percent')

@app.get('/')
def hello():
    REQUEST_COUNT.inc()
    return "Hello World!"

@app.get('/metrics')
def metrics():
    CPU_USAGE.set(psutil.cpu_percent(interval=0.0))
    MEMORY_USAGE.set(psutil.virtual_memory().percent)
    DISK_USAGE.set(psutil.disk_usage('/').percent)
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
