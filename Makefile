c =Add new changes

sent:
	git add .
	git commit -m "${c}"
	git push


get-data:

	curl -L -o "ML/datas/housing-prices-dataset.zip" "https://www.kaggle.com/api/v1/datasets/download/yasserh/housing-prices-dataset"
	cd ML/datas && python get_data.py && rm housing-prices-dataset.zip

prod:
	pip install -r requirements.txt
note:
	pip install -r note_requirements.txt

viz:
	sudo apt update
	sudo apt install graphviz