from google.cloud import compute_v1
from google.api_core.exceptions import NotFound

def list_subnets(project_id, region):
    client = compute_v1.SubnetworksClient()
    for subnet in client.list(project=project_id, region=region):
        print(f"Subnet: {subnet.name}, CIDR: {subnet.ip_cidr_range}")
