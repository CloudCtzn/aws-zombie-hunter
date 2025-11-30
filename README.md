![Role](https://img.shields.io/badge/Role-Cloud_Engineer-red)


# AWS EBS Zombie Hunter
![Python](https://img.shields.io/badge/Python-3.9-blue)
![AWS](https://img.shields.io/badge/AWS-SDK-orange)

## Overview 
**Zombie Assests** are Cloud resources that are running (or existing) but not doing any work. They silently drain your budget.

This tool is a Python-based automation script that:
1. Connects to your AWS account.
2. Scans for unattached EBS volumes.
3. Removes them safely.

---

## Features
| Feature | Description | 
| :--- | :--- |  
|**Auto Discovery:** | Scans a specific AWS region for all EBS volumes. | 
|**Safety Switch:** | Includes a 'DRY_RUN' flag. If 'True', it only prints out what *would* happen |
|**Race Handling:** | Uses 'boto3.waiters' to ensure volumes exist before deletion attempts. |

---

## Prerequisites
1. Python 3.x
2. Boto3 Library ('pip install boto3')
3. AWS CLI configured with appropiate permissions ('EC2FullAccess' or similar)

## How to run 
1. Clone the repo 
2. Open 'zombie_hunter.py' and configure the 'DRY_RUN' variable (True/False)
3. Run the script:
    '''bash python3 zombie_hunter.py