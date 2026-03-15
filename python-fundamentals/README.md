# Python DevOps Exercises

---

## 1. Disk Usage Calculation

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
* Print a human-readable summary.
* Use the `.2%` format specifier to display disk usage with two decimal places and a percent sign.

---

## 2. Lists, Tuples, and Sets

### Lists
* Create a list named `deployment_targets` with: `us-east-1`, `eu-west-1`, `ap-southeast-2`.
* Print the first target, append `us-west-2`, and change the second element to `eu-central-1`.

### Tuples
* Create a `service_endpoint` tuple with (Hostname, Port).
* Attempt to modify an element (commented out).

### Sets
* Create `required_packages` (include duplicates).
* Test for `requests` and `ansible`.
* Compare with an `installed` set to find missing, extra, and common packages.

---

## 3. Configuration Validation Exercise

### Objective
Design a function `validate_config` using a **fail-fast approach**.

### Validation Rules
* **Required Keys:** Exactly `service_name`, `env`, `port`.
* **Environment:** Must be `dev`, `staging`, or `prod`.
* **Service Name:** Must be a non-empty string.
* **Port:** Integer between `1` and `65535`.

---

## 4. Object-Oriented Deployment Manager

### Objective
Design a `Deployment` class to manage state (pending, deployed, rolled_back) and version history.

### Behavioral Requirements
* **Init:** Status `pending`, Version `None`.
* **Deploy:** Update status to `deployed` and store the previous version in history.
* **Rollback:** Revert to the immediate previous version. Return `False` if no history exists.
* **Status Check:** Return a dictionary with current metadata.

---

## 5. Flexible Resource Tagger

### Objective
Implement `manage_tags(existing_tags, *simple_tags, **key_value_tags)`.

### Rules
* **Simple Tags:** Added as keys with value `'true'`.
* **Key-Value Tags:** Overwrite any existing keys.
* **Immutability:** Must return a **new dictionary** without modifying the original.

---

## 6. Log File Line Generator

### Objective
Create a memory-efficient tool for parsing large log files. 



### Requirements
* **Function:** `read_log_lines(filepath)`
* **Type:** Must be a **generator** (uses `yield`).
* **Validation Rules:**
    * Skip empty lines or lines with only whitespace.
    * Skip comment lines (starting with `#`, even if leading whitespace exists).
    * **Sanitization:** Yielded lines must be stripped of all leading/trailing whitespace.

### Example Scenario
**Input (`sample.log`):**
```text
[INFO] Application starting...
  # This is a comment
[ERROR] Connection failed
