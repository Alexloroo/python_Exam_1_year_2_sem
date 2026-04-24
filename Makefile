c ="Add new changes"

sent:
	git add .
	git commit -m "${c}"
	git push


get-data:

	curl -L -o "datas/housing-prices-dataset.zip" "https://www.kaggle.com/api/v1/datasets/download/yasserh/housing-prices-dataset"
	cd datas && python get_data.py && rm housing-prices-dataset.zip