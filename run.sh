python mapper.py < input.txt && echo && python mapper.py < input.txt | sort -k1,1 | python reducer.py
