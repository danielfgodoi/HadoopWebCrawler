python mapper.py < data/urls.txt && echo && python mapper.py < data/urls.txt | sort -k1,1 | python reducer.py
