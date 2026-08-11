class UploadService:

    def __init__(

        self,

        repository,

        parser,

    ):

        self.repository = repository

        self.parser = parser

    async def upload(

        self,

        file,

    ):
        return {file.filename: "Uploaded Successfully!"}
        

        #

        # Save PDF

        #

        #

        # SHA256

        #

        #

        # Duplicate Check

        #

        #

        # Save Metadata

        #

        #

        # Queue Background Job