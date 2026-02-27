service_endpoint = ("server.dev.local", 3000)
print(f"Hostname: {service_endpoint[0]}")
print(f"Port: {service_endpoint[1]}")

# service_endpoint[1] = 443 # it will raise a TypeError because tuples are immutable