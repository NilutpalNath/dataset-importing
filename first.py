!touch ~/.kaggle/kaggle.json
api_token = {"username": "darkaxe", "key": "4061c17c6ceeea23cf38b713156e25c6"}

import json
with open('/root/.kaggle/kaggle.json', 'w') as file:
	json.dump(api_token, file)

!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d tongpython/cat-and-dog # get api command fro kaggle

import zipfile
import os

zip_ref = zipfile.ZipFile('cat-and-dog.zip', 'r')
zip_ref.extractall()
zip_ref.close()