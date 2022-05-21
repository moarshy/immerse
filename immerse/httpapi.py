# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_httpapi.ipynb (unless otherwise specified).

__all__ = ['IPFS']

# Cell
import requests
import json
from fastcore.all import *

# Cell
class IPFS:
    def __init__(self,
        coreadd:str="http://127.0.0.1:5001", # HTTP address of the local IPFS daemon
        coreapi:str="/api/v0", # Core API address
        local:bool=True, # If local uses local node, else uses Infura.io gateway
    ):
        if local:
            self.coreurl = f"{coreadd}{coreapi}"
        else:
            self.coreurl = f"{'https://ipfs.infura.io:5001/api/v0'}"

    def add(self,
        filepath:str, # Path to the file/directory to be added to IPFS
        wrap_with_directory:str='false', # True if path is a directory
        recursive:str='false', # Add directory paths recursively
        chunker:str='size-262144', # Chunking algorithm, size-[bytes], rabin-[min]-[avg]-[max] or buzhash
        pin:str='true', # Pin this object when adding
        hash_:str='sha2-256', # Hash function to use. Implies CIDv1 if not sha2-256
        progress:str='true', # Stream progress data
        silent:str='false', # Write no output
        cid_version:int=0, # CID version
        **kwargs,
    ):
        "add file/directory to ipfs"

        params = {}
        params['wrap-with-directory'] = wrap_with_directory
        params['chunker'] = chunker
        params['pin'] = pin
        params['hash'] = hash_
        params['progress'] = progress
        params['silent'] = silent
        params['cid-version'] = cid_version
        params.update(kwargs)

        files = {
            'file': open(filepath, 'rb'),
        }

        response = requests.post(f'{self.coreurl}/add',
                                 params=params,
                                 files=files)

        try:
            print("Added", filepath, "to IPFS - ","Response", response.status_code)
            return response, json.loads(response.text.strip().split('\n')[-1])

        except:
            print(response.status_code)
            return response, ""