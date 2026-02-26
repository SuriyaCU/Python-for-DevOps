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

EXERCISE
This exercise implements a robust validation function, validate_config, designed to ensure that a configuration dictionary meets specific structural and data integrity standards. It is built to "fail-fast," returning False immediately upon encountering an invalid parameter.
Validation Rules
A configuration dictionary is considered valid only if it satisfies all of the following criteria:
1.Required Keys: The dictionary must contain exactly these three keys: service_name, env, and port.
2.Environment Value: The value for the env key must be one of the following strings: 'dev', 'staging', or 'prod'.
3.Service Name: The value for service_name must be a non-empty string.
4.Port Number: The value for port must be an integer between 1 and 65535 inclusive.

FUNCTIONS
1.Greet Multiple Users
Define a function greet_users(names) that takes a list of user names and prints a personalized greeting for each.

Example input: ['Alice', 'Bob', 'Charlie']

Example output:

"Hello, Alice!"
"Hello, Bob!"
"Hello, Charlie!"
2.Sum of Even Numbers
Define a function sum_even(numbers) that takes a list of integers and returns the sum of all even numbers.
Test with [1, 2, 3, 4, 5, 6] (should return 12).
3.Fibonacci Sequence Generator
Define a function fibonacci(n) that returns a list of the first n Fibonacci numbers.
Example: fibonacci(5) should return [0, 1, 1, 2, 3].
