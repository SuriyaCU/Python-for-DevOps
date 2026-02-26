---

# Python Practice Exercises

This document contains a collection of beginner-friendly Python exercises focused on basic programming concepts such as variables, data structures, functions, and validation.

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

### 2. Sum of Even Numbers

#### Description

Create a function named `sum_even` that:

* Accepts a list of integers.
* Calculates and returns the sum of all even numbers.

#### Example

Input:

* `1, 2, 3, 4, 5, 6`

Output:

* `12`

---

### 3. Fibonacci Sequence Generator

#### Description

Create a function named `fibonacci` that returns the first `n` numbers in the Fibonacci sequence.

#### Example

Input:

* `5`

Output:

* `0, 1, 1, 2, 3`

---

