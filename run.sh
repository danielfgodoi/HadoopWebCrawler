python mapper.py < links && echo && python mapper.py < links | sort -k1,1 | python reducer.py
