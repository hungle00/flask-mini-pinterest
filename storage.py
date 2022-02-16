from azure.storage.blob import BlobServiceClient
import config

connect_str = config.AZURE_STORAGE_CONNECTION_STRING # retrieve the connection string from the environment variable
container_name = "photos" # container name in which images will be store in the storage account

def connect_azure_storage():
    blob_service_client = BlobServiceClient.from_connection_string(conn_str=connect_str) # create a blob service client to interact with the storage account
    try:
        container_client = blob_service_client.get_container_client(container=container_name) # get container client to interact with the container in which images will be stored
        container_client.get_container_properties() # get properties of the container to force exception to be thrown if container does not exist
    except Exception as e:
        print(e)
        print("Creating container...")
        container_client = blob_service_client.create_container(container_name)
    return container_client

def get_blob_items():
    container_client = connect_azure_storage()
    images = []
    blob_items = container_client.list_blobs()
    for blob in blob_items:
        blob_client = container_client.get_blob_client(blob=blob.name)
        images.append(blob_client.url)
    return images

def upload_blob(file):
    container_client = connect_azure_storage()
    container_client.upload_blob(file.filename, file)