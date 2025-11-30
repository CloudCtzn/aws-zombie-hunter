# AWS EBS Zombie Hunter

## Overview 
This is a Python automation tool designed to audit and manage AWS EBS (Elastic Block Store) volumes. It specifically targets "Zombie Assets" (unattached volumes) that are incurring costs without being used.

## Features 
**Auto Discovery:** Scans a specific AWS region for all EBS volumes.
**State Filtering:** Identifies volumes with a state of 'available' (unattached)
**Safety Mechanisms:**
    **Dry Run Mode:** 'DRY_RUN = True' prevents accidental deletions. Switch to 'DRY_RUN = False' to delete zombies.
    **Waiters:** Uses Boto3 waiters to handle API race conditions during resource creation.

## Prerequisites
Python 3.x
Boto3 Library ('pip install boto3')
AWS CLI configured with appropiate permissions ('EC2FullAccess' or similar)

## How to run 
1. Clone the repo 
2. Open 'zombie_hunter.py' and configure the 'DRY_RUN' variable (True/False)
3. Run the script:
    '''bash python3 zombie_hunter.py