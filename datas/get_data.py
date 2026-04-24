import zipfile
zip = "housing-prices-dataset.zip"
with zipfile.ZipFile(zip, 'r') as zip_ref:
    zip_ref.extractall()