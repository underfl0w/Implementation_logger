import base64
import csv
import io
import json
import zipfile

import jsondiff
import requests

API_endpoint = "http://127.0.0.1:8000/device/"

def filechanged(changed_files, all_hashes):
    # Lets save the changed files, zip it and send it.
    print(len(changed_files))
    files = []

    for i in range(len(changed_files)):
        a = list(changed_files.keys())[i]
        files.append(all_hashes[a])
    print(files)

def checkPrevious(device, hashes):

    r = requests.get(device)
    x = json.loads(json.dumps(r.json()))
    x = json.loads((x["hashes"]))
    hashes = json.loads(hashes)
    if(x == hashes):
        result = jsondiff.diff(x, hashes)
        print(result)
        # Looks like the hashes stayed the same.
        return 0
    else:
        result = jsondiff.diff(x, hashes)
        print(result)
        data = {
            'hashes': json.dumps(hashes)
        }
        filechanged(result, hashes)
        r = requests.patch(device,data)



def saveHashes(csvFile, device):

    file_zip = io.BytesIO(base64.b64decode(csvFile))
    zipfile_ob = zipfile.ZipFile(file_zip)
    print(zipfile_ob.namelist())
    with zipfile_ob.open('collection') as myfile:
        items_file = io.TextIOWrapper(io.BytesIO(myfile.read()))
        myfile_csv = csv.DictReader(items_file)
        hashes = json.dumps([row for row in myfile_csv])
    checkPrevious(device, hashes)
    data = {
        'device': device,
        'hashes': hashes
    }

    #r = requests.post(url = API_endpoint, data= data)
