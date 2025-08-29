class Storage:
    def __init__(self):
        pass

class LocalFile(Storage):
    def __init__(self, base_path):
        super().__init__()
        self.base_path = base_path

class S3(Storage):
    def __init__(self, bucket_name, region):
        super().__init__()
        self.bucket_name = bucket_name
        self.region = region

class ImageRetriever:
    def __init__(self, storage: Storage):
        self.storage = storage