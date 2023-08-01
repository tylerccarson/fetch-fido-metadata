# fetch-fido-metadata
Python utility to fetch FIDO Metadata Service (MDS) data

To download the metadata:
1) `mkdir .venv`
2) `python3 -m venv .venv`
3) `source .venv/bin/activate`
4) `pip install -r requirements.txt`
5) `python get_fido_metadata.py`

A JSON file `fido_metadata.json` will be created. To cleanup your environement, run `deactivate`.
