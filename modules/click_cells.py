import modules.create_square as m_square
import modules.create_triangle as m_triangle

def by_click(x, y):
    if x > -100 and x < 0:
        m_square.draw_square()
        list_cell[0] = 1
        print(list_cell)
    elif x > 0 and x < 100:
        m_triangle.draw_triangle()
        list_cell[1] = 2
        print(list_cell)
list_cell = [0, 0]