#  You can experiment here, it won’t be checked
dimensions = [int(input()) for _ in range(5)]
box, door = map(sorted, (dimensions[:3], dimensions[3:]))
print('The box can be carried'
      if all(b <= d for b, d in zip(box, door))
      else 'The box cannot be carried')
