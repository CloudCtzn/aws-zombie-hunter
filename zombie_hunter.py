import boto3
import time

# CONFIGURATION
# True = Just look and print. 
# False = Actually DELETE volumes.
DRY_RUN = True 

ec2 = boto3.client('ec2', region_name='us-east-1')

print("----- Starting Zombie Audit -----")

# 1. PREP: Create a dummy volume so we have something to test (Only in Dry Run)
if DRY_RUN:
    print("Creating a test zombie for the dry run...")
    new_vol = ec2.create_volume(AvailabilityZone='us-east-1a', Size=1, VolumeType='gp3')
    
    # THE WAITER: Forces script to pause until volume is actually ready
    print(f"Waiting for {new_vol['VolumeId']} to initialize...")
    waiter = ec2.get_waiter('volume_available')
    waiter.wait(VolumeIds=[new_vol['VolumeId']])
    print("Volume is ready! Proceeding with audit...")

# 2. AUDIT: Check all volumes in the region
data = ec2.describe_volumes()

for vol in data['Volumes']:
    if vol['State'] == 'available':
        vol_id = vol['VolumeId']
        size = vol['Size']
        
        # 3. ACTION: Decide whether to print or destroy
        if DRY_RUN:
            print(f"[DRY RUN] Found Zombie: {vol_id} ({size} GB). Would have deleted.")
        else:
            print(f"[ACTION] Deleting Zombie: {vol_id} ({size} GB)...")
            ec2.delete_volume(VolumeId=vol_id)
            print("Deleted.")

print("----- Audit Complete -----")