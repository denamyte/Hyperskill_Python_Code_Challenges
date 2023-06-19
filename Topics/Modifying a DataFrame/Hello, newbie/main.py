row = {'species': 'Adelie', 'bill_length_mm': 45.7, 'bill_depth_mm': 15.5}
penguins_example = pd.concat([penguins_example, pd.DataFrame.from_records([row])], ignore_index=True)

print(penguins_example)