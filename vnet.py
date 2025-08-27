from google.cloud import compute_v1

def create_subnet(
    project_id, 
    region, 
    network, 
    subnet_name, 
    ip_cidr_range
):
    client = compute_v1.SubnetworksClient()

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

def list_subnets(project_id, region):
    client = compute_v1.SubnetworksClient()
    for subnet in client.list(project=project_id, region=region):
        print(f"Subnet: {subnet.name}, CIDR: {subnet.ip_cidr_range}")

def delete_subnet(project_id, region, subnet_name):
    client = compute_v1.SubnetworksClient()
    operation = client.delete(
        project=project_id,
        region=region,
        subnetwork=subnet_name
    )
    print(f"Delete operation: {operation.name}")

# Usage example:
# Set these values according to your environment
project_id = "sapient-duality-469110-d9"
region = "us-central1"
network = "default"
subnet_name = "test-subnet"
ip_cidr_range = "10.0.1.0/24"

create_subnet(project_id, region, network, subnet_name, ip_cidr_range)
list_subnets(project_id, region)
# delete_subnet(project_id, region, subnet_name)
