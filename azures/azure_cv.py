from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

import config

class AzureComputerVision:
    subscription_key = config.SUBSCRIPTION_KEY
    endpoint = config.ENDPOINT
    remote_url = "https://lmh0storage.blob.core.windows.net/"
    
    def __init__(self, image_url):
        self.image_url = image_url
        # Authenticates your credentials and creates a client.
        self.computervision_client = ComputerVisionClient(self.endpoint, CognitiveServicesCredentials(self.subscription_key))

    # Tag an Image - remote
    def tag_image(self):
        tags_result_remote = self.computervision_client.tag_image(self.image_url)
        return tags_result_remote.tags

    # Describe an Image - remote
    def description_image(self):
        description_results = self.computervision_client.describe_image(self.image_url)
        return description_results

    # Categorize an Image - remote
    def categorize_image(self, image_features):
        categorize_results_remote = self.computervision_client.analyze_image(self.image_url , image_features)
        return categorize_results_remote.categories


remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"
azure_cv = AzureComputerVision(remote_image_url)

print("===== Tag an image - remote =====")
#for tag in azure_cv.tag_image():
    #print(tag)
#    print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))

print("===== Describe an image - remote =====")
#for caption in azure_cv.description_image():
#    print(caption)

print("===== Categorize an image - remote =====")
# remote_image_features = ["categories"]
# for category in azure_cv.categorize_image(remote_image_features):
#     print(category)
