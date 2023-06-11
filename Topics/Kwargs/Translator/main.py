def translate(**kwargs):
    for eng, esp in kwargs.items():
        print(eng, ":", esp)


words = {"mother": "madre", "father": "padre", 
         "grandmother": "abuela", "grandfather": "abuelo"}

translate(**words)
