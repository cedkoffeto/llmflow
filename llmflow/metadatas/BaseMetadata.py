class BaseMetadata:
    def __init__(self, description, tags):
        self.description = description
        self.tags = tags
    
    def __str__(self):
        return f"Description: {self.description}\nTags: {', '.join(self.tags)}"