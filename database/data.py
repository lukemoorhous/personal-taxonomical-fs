from dataclasses import dataclass


@dataclass
class DTO:
    id: int = None


@dataclass
class ContentFile(DTO):
    filename: str = None
    filetype: str = None
    fileextension: str = None


@dataclass
class ContentVersion(DTO):
    name: str = None
    version: str = None
    content_file: ContentFile = None
    contents: bytes = None
