---

# Python

---

## Disk Usage Calculation

Given the following variables:

* Server Name: `webserver-03`
* CPU Cores: `4`
* Memory: `8.0 GB`
* Total Disk Space: `500 GB`
* Used Disk Space: `350 GB`


### Tasks

* Compute the disk usage percentage.
* Print the raw percentage value.
* Convert the server name to uppercase.
* Include the number of CPU cores and amount of RAM.
* Display the disk usage rounded to one decimal place.
* Print a human-readable summary including:

  * Server name in uppercase
  * Number of CPU cores
  * Memory size
  * Disk usage percentage
* Use the `.2%` format specifier to display disk usage with two decimal places and a percent sign.

---

## Lists

### Tasks

* Create a list named `deployment_targets` with the following values:

  * `us-east-1`
  * `eu-west-1`
  * `ap-southeast-2`
* Print the first target.
* Append `us-west-2` to the list.
* Change the second element to `eu-central-1`.
* Print the list after each modification.

---

## Tuples

### Tasks

* Create a tuple named `service_endpoint` containing:

  * Hostname
  * Port number
* Print the hostname and port.
* Attempt to modify one element (keep it commented to avoid errors).

---

## Sets

### Tasks

* Create a set named `required_packages` containing package names.
* Include duplicate values to observe automatic removal.
* Test whether the following packages exist in the set:

  * `requests`
  * `ansible`
* Add `paramiko` to the set.
* Safely remove `pip` from the set.
* Create another set named `installed` with some package names.
* Compare both sets to find:

  * Missing packages
  * Extra packages
  * Common packages

---

## Configuration Validation Exercise

### Objective

Design a function named `validate_config` that checks whether a configuration dictionary is valid.

The function must follow a **fail-fast approach**, returning `False` immediately when any rule is violated.

### Validation Rules

A configuration dictionary is valid only if:

1. Required Keys

   * Must contain exactly:

     * `service_name`
     * `env`
     * `port`

2. Environment Value

   * Must be one of the following:

     * `dev`
     * `staging`
     * `prod`

3. Service Name

   * Must be a non-empty string.

4. Port Number

   * Must be an integer between `1` and `65535` (inclusive).

---

## Functions

### 1. Greet Multiple Users

#### Description

Create a function named `greet_users` that accepts a list of user names and prints a personalized greeting for each.

#### Example

Input:

* `Alice`
* `Bob`
* `Charlie`

Output:

* Hello, Alice!
* Hello, Bob!
* Hello, Charlie!

---
## Exercise 4: Object-Oriented Deployment Manager

### Objective
Design a `Deployment` class that models a software deployment lifecycle. This class encapsulates state management (pending, deployed, rolled_back) and maintains a version history to support multi-step rollbacks.



### Behavioral Requirements

#### 1. Initialization (`__init__`)
* **Status**: Set to `'pending'`.
* **Version**: Initially set to `None`.
* **Attributes**: Store `service_name` and `environment` as strings.
* **History**: Initialize an internal structure to track previous versions.

#### 2. Deploy (`deploy`)
* **State Change**: Update status to `'deployed'`.
* **Version Update**: Set `new_version` as the current version.
* **History**: The version that was active *before* this call must be stored to allow for future rollbacks.

#### 3. Rollback (`rollback`)
* **Logic**: Revert the current version to the one immediately preceding it in history.
* **Validation**: If no historical version exists, the method must return `False`.
* **Success**: 
    * Update status to `'rolled_back'`.
    * Update the current version to the reverted version.
    * Return `True`.

#### 4. Status Check (`check_status`)
* **Return Value**: A dictionary containing the following keys:
    * `service_name`: The name of the service.
    * `environment`: The deployment environment (e.g., prod, staging).
    * `status`: The current state (`pending`, `deployed`, or `rolled_back`).
    * `version`: The currently active version string (or `None`).

---
## Exercise 5: Flexible Resource Tagger

As a cloud engineer, maintaining consistent metadata across infrastructure is critical for cost allocation, security, and automation. This exercise focuses on creating a robust Python utility to manage resource tags dynamically.

---

### Problem Description

Your task is to implement the `manage_tags` function in `exercise.py`. This function must process an existing dictionary of tags and apply updates based on a flexible set of additional arguments, following strict precedence and immutability rules.



### Behavioral Requirements

The function signature is:  
`def manage_tags(existing_tags, *simple_tags, **key_value_tags):`

#### 1. Initial Tags (`existing_tags`)
The first argument is a dictionary representing the resource's current tags.

#### 2. Simple Tags (`*simple_tags`)
* The function accepts any number of positional string arguments.
* Each simple tag must be added to the dictionary as a key with the string value `'true'`.
* If a simple tag is provided multiple times (e.g., `'billable'`, `'billable'`), it should only be added once.

#### 3. Key-Value Tags (`**key_value_tags`)
* The function accepts any number of keyword arguments.
* These pairs should be added to the result dictionary.
* **Precedence:** If a key from a keyword argument already exists (either in the initial tags or the simple tags), its value **must** be overwritten by the keyword argument value.

#### 4. Immutability
* The function **must not modify** the original `existing_tags` dictionary.
* It must return a **new dictionary** containing the merged result.

---

### Example Usage

```python
initial = {'owner': 'dev-team', 'env': 'dev'}

final_tags = manage_tags(
    initial,
    'billable',              # A simple tag
    'critical',              # Another simple tag
    env='staging',           # Overwrites 'env' from initial
    cost_center='xyz-123'    # A new key-value tag
)

---

## Exercise 6: Log File Line Generator

### The Task
Create a memory-efficient tool for parsing large log files using a **Python Generator**.



### Requirements
* **Function:** `read_log_lines(filepath)`
* **Memory Efficiency:** Must be a **generator** using the `yield` keyword.
* **Validation Rules:**
    * Skip empty lines or lines with only whitespace.
    * Skip comment lines (starting with `#`, even if indented).
    * Each yielded line must be stripped of leading/trailing whitespace.

### Example Scenario
**Input (`sample.log`):**
```text
[INFO] Application starting...
# Configuration section
  # A nested comment
[ERROR] Failed to process request id: 123
