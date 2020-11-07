movies = {60: "Breakfast at Tiffany's",
          40: "Pulp Fiction",
          25: "Matrix",
          16: "Trainspotting",
          0: "Lion King"}


def recommend(age):
    for key in movies:
        if age > key:
            return movies[key]
    return ""


print(recommend(int(input())))
