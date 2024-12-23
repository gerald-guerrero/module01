cheetos = [1, 2, 3, 4, 5]

squares = [x*x for x in cheetos]

evens = list(filter(lambda x: x % 2 == 0, cheetos))

print(squares, evens)