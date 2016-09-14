python mapper.py < input && echo && python mapper.py < input | sort -k1,1 | python reducer.py
