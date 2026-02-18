DISK USAGE CALCULATION
Given the variables below, compute the disk usage percentage.
server_name = "webserver-03"
cpu_cores = 4
memory_gb = 8.0
disk_total_gb = 500
disk_used_gb = 350
Print the raw percentage value.
Build a human‑readable summary string:
Convert the server name to uppercase.
Include the number of CPU cores and amount of RAM.
Show the disk usage percentage rounded to one decimal place.
Print a summary containing the server name in uppercase, the number of CPU cores, the memory, and the disk usage).
Finally, use the .2% format specifier in an f‑string to display the usage with two decimal places and a percent sign.

LISTS
Create a list deployment_targets with values ['us-east-1', 'eu-west-1', 'ap-southeast-2']
Print the first target
Append 'us-west-2'
Change the second element to 'eu-central-1'
Print the list after each step

TUPLES
Create a tuple service_endpoint with hostname and port values.
Print the hostname and port.
Attempt to modify an element (commented out to avoid error).

SETS
Create a set of strings named required_packages, representing possible required packages.
Include a few duplicates to practice set operations.
Test for membership of 'requests' and 'ansible' strings.
Add 'paramiko' and safely remove 'pip' from the set.
Create another set of strings, now named installed. Mention a few of the packages listed under the required set.
Given these two sets, compute missing, extra, and common packages.