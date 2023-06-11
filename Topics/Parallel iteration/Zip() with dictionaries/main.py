# please do not modify the following code
_d_list = [keyword.split(':') for keyword in input().split(', ')]
domestic_animal = {key: value for key, value in _d_list}
_w_list = [keyword.split(':') for keyword in input().split(', ')]
wild_animal = {key: value for key, value in _w_list}

for (dk, dv), (wk, wv) in zip(domestic_animal.items(), wild_animal.items()):
    print(f"The domestic animal's {dk} is '{dv}'.")
    print(f"The wild animal's {wk} is '{wv}'.")
