"""
Notes:
    - lots of ways to test
    - used dependency injection since it is the easiest to do
    - the file is still in the bucket, automating cleanup is an exercise left up to the reader
"""

from main import upload_file_to_s3


def test_upload_file_to_s3(tmp_path):
    # Arrange -- create a random file to upload
    d = tmp_path
    path = d / "my_uploaded_file.txt"
    CONTENT = "Hello World!"
    path.write_text(CONTENT)

    # Act -- upload file to localstack
    success = upload_file_to_s3("workflow1-interacting-with-s3/file_to_upload.txt", "example-bucket", use_localstack=True)

    # Assert -- file is there
    assert success
