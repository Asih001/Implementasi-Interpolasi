# Data dari gambar
x = [5, 10, 15, 20, 25, 30, 35, 40]
y = [40, 30, 25, 40, 18, 20, 22, 15]

# Interpolasi Polinom Lagrange
def lagrange_interpolation(x, y, x_interp):
  n = len(x)
  y_interp = 0
  for i in range(n):
    l = 1
    for j in range(n):
      if i != j:
        l *= (x_interp - x[j]) / (x[i] - x[j])
    y_interp += y[i] * l
  return y_interp

# Interpolasi Polinom Newton
def newton_interpolation(x, y, x_interp):
  n = len(x)
  # Hitung tabel selisih terbagi
  divided_differences = [[0 for _ in range(n)] for _ in range(n)]
  for j in range(n):
    divided_differences[j][0] = y[j]
  for j in range(1, n):
    for i in range(j, n):
      divided_differences[i][j] = (divided_differences[i][j-1] - divided_differences[i-1][j-1]) / (x[i] - x[i-j])
  # Hitung nilai interpolasi
  y_interp = divided_differences[0][0]
  for j in range(1, n):
    term = 1
    for i in range(j):
      term *= (x_interp - x[i])
    y_interp += term * divided_differences[j][j]
  return y_interp

# Titik interpolasi
x_interp = list(range(5, 41))

# Hitung nilai interpolasi dengan kedua metode
y_lagrange = [lagrange_interpolation(x, y, i) for i in x_interp]
y_newton = [newton_interpolation(x, y, i) for i in x_interp]

# Print hasil interpolasi
print("Interpolasi Lagrange:")
for i in range(len(x_interp)):
  print(f"x = {x_interp[i]}, y = {y_lagrange[i]}")

print("\nInterpolasi Newton:")
for i in range(len(x_interp)):
  print(f"x = {x_interp[i]}, y = {y_newton[i]}")
