from google.cloud import compute_v1

def list_instance_groups(project_id, zone):
    client = compute_v1.InstanceGroupManagersClient()
    for group in client.list(project=project_id, zone=zone):
        print(f"Group: {group.name}, Size: {group.target_size}")