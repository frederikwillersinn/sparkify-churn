import os
from google.cloud import storage


def transfer_files_with_cloud_storage(
    bucket_name, local_file_name, remote_blob_name, transfer_option
):
    """
    Uploads a file to or downloads a file from Google Cloud Storage bucket.

    :param bucket_name: name of the Google Cloud Storage bucket (str)
    :param local_file_name: name of local file e.g.: *.csv, *.xlsx (str)
    :param remote_blob_name: name of blob name (str)
    :param transfer_option: options: "fetch", "export" (str)
    :return: file saved to local file path or Google Cloud Storage (None)
    """
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(remote_blob_name)

    if transfer_option == "export":
        print(f"Uploading '{local_file_name}' to GCP bucket '{bucket_name}' as '{remote_blob_name}'...")
        blob.upload_from_filename(local_file_name)
    elif transfer_option == "fetch":
        print(f"Downloading '{remote_blob_name}' from GCP bucket '{bucket_name}' as '{local_file_name}'...")
        blob.download_to_filename(local_file_name)
    print("Done.\n")
