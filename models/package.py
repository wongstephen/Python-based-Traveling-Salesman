class Package:
    def __init__(self, name, version, description):
        self.name = name
        self.version = version
        self.description = description

    def __str__(self):
        return f"{self.name}=={self.version}"

    def __repr__(self):
        return f"{self.name}=={self.version}"