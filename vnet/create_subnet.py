from google.cloud import compute_v1
from google.api_core.exceptions import NotFound

def create_subnet(
    project_id, 
    region, 
    network, 
    subnet_name, 
    ip_cidr_range
):
    client = compute_v1.SubnetworksClient()
    try:
        client.get(project=project_id, region=region, subnetwork=subnet_name)
        print(f"Subnet '{subnet_name}' already exists.")
    except NotFound:
        subnetwork = compute_v1.Subnetwork()
        subnetwork.name = subnet_name
        subnetwork.network = f"projects/{project_id}/global/networks/{network}"
        subnetwork.ip_cidr_range = ip_cidr_range
        subnetwork.region = f"projects/{project_id}/regions/{region}"

        operation = client.insert(
            project=project_id,
            region=region,
            subnetwork_resource=subnetwork
        )

        print(f"Creation operation: {operation.name}")

