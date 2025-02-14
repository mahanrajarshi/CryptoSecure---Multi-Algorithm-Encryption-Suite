workers = 4
worker_class = 'gevent'
bind = '0.0.0.0:5000'
timeout = 120
keepalive = 5
preload_app = True

# Security settings
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# Logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'

# SSL configuration
certfile = '/etc/letsencrypt/live/example.com/fullchain.pem'
keyfile = '/etc/letsencrypt/live/example.com/privkey.pem'