from google.cloud import compute_v1
from google.api_core.exceptions import NotFound

def delete_subnet_if_exists(project_id, region, subnet_name):
    client = compute_v1.SubnetworksClient()
    try:
        client.get(project=project_id, region=region, subnetwork=subnet_name)
        # Only call delete if the subnet was found
        operation = client.delete(
            project=project_id,
            region=region,
            subnetwork=subnet_name
        )
        print(f"Delete operation: {operation.name}")
    except NotFound:
        print(f"Subnet '{subnet_name}' not found. Skipping deletion.")
