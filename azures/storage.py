from azure.storage.blob import BlobServiceClient
#from .. import config
import config

class BlobStorage:
    connect_str = config.AZURE_STORAGE_CONNECTION_STRING 
    container_name = "photos" 
    remote_url = "https://lmh0storage.blob.core.windows.net/"
    
    def __init__(self):
        self.blob_service_client = BlobServiceClient.from_connection_string(conn_str=self.connect_str) # create a blob service client to interact with the storage account
        self.container_client  = self.connect_azure_storage()

    def connect_azure_storage(self):
        try:
            container_client = self.blob_service_client.get_container_client(container=self.container_name) # get container client to interact with the container in which images will be stored
            container_client.get_container_properties() # get properties of the container to force exception to be thrown if container does not exist
        except Exception as e:
            print(e)
            print("Creating container...")
            container_client = self.blob_service_client.create_container(self.container_name)
        return container_client

    def get_blob_items(self):
        images = []
        blob_items = self.container_client.list_blobs()
        for blob in blob_items:
            blob_client = self.container_client.get_blob_client(blob=blob.name)
            images.append(blob_client.url)
        return images

    def upload_blob(self, file):
        self.container_client.upload_blob(file.filename, file)

    def image_url(self, file):
        return self.remote_url + self.container_name + '/' + file.filename
