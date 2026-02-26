required_packages = set(["python3", "pip", "requests", "boto3", "pip"])
print(required_packages)

print(f"Is 'requests' required? {"requests" in required_packages}")
print(f"Is 'ansible' required? {"ansible" in required_packages}")

required_packages.add("paramiko")
required_packages.discard("pip")
print(required_packages)

installed_packages = {"docker", "python3", "pip"}
missing_packages = required_packages - installed_packages
extra_packages = installed_packages - required_packages
common_packages = required_packages & installed_packages

print(f"Missing packages: {missing_packages}")
print(f"Extra packages: {extra_packages}")
print(f"Common packages: {common_packages}")