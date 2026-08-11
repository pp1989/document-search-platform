from docling.document_converter import DocumentConverter

from app.domain.ports.document_parser import (
    DocumentParser,
)


class DoclingParser(DocumentParser):

    def __init__(self):

        self.converter = DocumentConverter()

    async def parse(

        self,

        file_path: str,

    ):

        result = self.converter.convert(file_path)

        return result.document