stars = [
  0, 0, 0, 5, 0, 0, 0,
  0, 4, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 3, 0,
  0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 5, 0,
  0, 0, 5, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 4, 0,
  0, 3, 0, 3, 0, 0, 0,
]

total = sum(stars)
N = len([i for i in stars if i > 0])
rating = total / N

print(total, N, rating)



response = []
for i in stars:
  
  if i > 0:
    response.append(i)
  
  N = len(response)
  if N > 0:
    rating = sum(response) / N
  else:
    rating = 0
  
  print(i, f"{rating:0.1f}")

print(response)