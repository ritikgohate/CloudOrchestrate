from google.cloud import compute_v1

def delete_instance_group(project_id, zone, group_name):
    client = compute_v1.InstanceGroupManagersClient()
    operation = client.delete(
        project=project_id,
        zone=zone,
        instance_group_manager=group_name
    )
    print(f"Delete operation: {operation.name}")