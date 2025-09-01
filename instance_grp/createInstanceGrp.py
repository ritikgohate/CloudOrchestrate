from google.cloud import compute_v1

def create_instance_group(
    project_id,
    zone,
    group_name,
    instance_template,
    size
):
    client = compute_v1.InstanceGroupManagersClient()
    # Construct Instance Group Manager resource
    igm = compute_v1.InstanceGroupManager()
    igm.name = group_name
    igm.instance_template = f"projects/{project_id}/global/instanceTemplates/{instance_template}"
    # igm.instance_template = f"projects/sapient-duality-469110-d9/regions/asia-south1/instanceTemplates/standard-instance-template"
    igm.target_size = size
    igm.base_instance_name = group_name

    operation = client.insert(
        project=project_id,
        zone=zone,
        instance_group_manager_resource=igm
    )
    print(f"Create operation: {operation.name}")
    