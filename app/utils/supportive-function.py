import hashlib


def calculate_checksum(
    file_path: str,
):

    sha = hashlib.sha256()

    with open(
        file_path,
        "rb",
    ) as file:

        while chunk := file.read(8192):

            sha.update(chunk)

    return sha.hexdigest()
