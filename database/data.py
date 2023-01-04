class DTO:
    def __init__(self):
        pass
    
    def get_columns():
        return ''

class ContentFile(DTO):
    def __init__(self, filepath: str, filename: str, filetype: str, contents: bytearray):
        self.filepath = filepath
        self.filename = filename
        self.filetype = filetype
        self.contents = contents
    
    def __value__(self):
        return f"'{self.filepath}', '{self.filename}', '{self.filetype}', {self.contents}"
    
    def get_columns():
        return 'filepath VARCHAR(255), filename VARCHAR(255), filetype VARCHAR(255), content BLOB'

class ContentVersion(DTO):
    def __init__(self, name: str, version: str, content_file: ContentFile):
        self.name = name
        self.version = version
        self.content_file = content_file

    def get_columns():
        # return 'name VARCHAR(255), version VARCHAR(25), content_file FOREIGNKEY(ContentFile)'
        return 'name VARCHAR(255), version VARCHAR(25)'