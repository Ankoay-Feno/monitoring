# app.py
from flask import Flask
from prometheus_client import make_wsgi_app, Counter, Gauge
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

# Métriques Prometheus
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')
CPU_USAGE = Gauge('cpu_usage_percent', 'CPU Usage Percentage')
MEMORY_USAGE = Gauge('memory_usage_percent', 'Memory Usage Percent')
DISK_USAGE = Gauge('disk_usage_percent', 'Disk Usage Percent')

@app.route('/')
def hello():
    REQUEST_COUNT.inc()
    return "Hello World!"

@app.route('/metrics')
def metrics():
    # Simuler l'usage CPU et mémoire
    CPU_USAGE.set(psutil.cpu_percent(interval=1))
    MEMORY_USAGE.set(psutil.virtual_memory().percent)
    DISK_USAGE.set(psutil.disk_usage("/").percent)
    return make_wsgi_app()

# Application combinée
application = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})