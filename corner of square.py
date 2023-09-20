def is_corner_occupied(x, y, squares):
  def generate_square(N):
squares = set()
  for i in range(N - 1):
        if not is_corner_occupied(0, 0, squares):
            squares.add((0, 0))
        if not is_corner_occupied(i, 0, squares):
            squares.add((i, 0))
        if not is_corner_occupied(0, i, squares):
            squares.add((0, i))
        if not is_corner_occupied(i, i, squares):
            squares.add((i, i))
square_N = []
    for y in range(N):
        row = []
        for x in range(N):
            if (x, y) in squares:
                row.append('#') 
            else:
                row.append('.') 
        square_N.append(''.join(row))
    return square_N
N = 5  
result = generate_square(N)
for row in result:
    print(row)
