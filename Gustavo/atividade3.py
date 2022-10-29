ax, ay = float(15000), float(15000)
bx = float(45000)
cy = float(65000)
x, y = 0, 0

while True:
    ax += ax*0.1
    bx += bx*0.05
    x += 1
    if (ax>=bx):
        break

while True:
    ay += ay*0.1
    cy += cy*0.025
    y += 1
    if (ay-(ay*0.23) >= cy):
        break

print(f'A população A irá se igualar ou ultrapassar a B em {x} anos')
print(f'A população A ultrapassar a C em 23% em {y} anos')
