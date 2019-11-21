import shapes # dołączenie modułu do programu


for i in range(4):
    for j in range(4):
        shapes.draw_square(i * 100, j * 100, 100)
