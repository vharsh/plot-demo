#!/usr/bash/python3
"""
module to download data
"""
import io
from requests import get



def download(url, file_name):
    """
    function to download file over http
    url : URL of file to be downloaded
    file_name : File name
    """
    with io.FileIO(file_name, "w") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)
