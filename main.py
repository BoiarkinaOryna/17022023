import turtle
import modules.click_cells as m_click
import modules.createng_cells as m_cells
import modules.create_screen as m_screen

m_cells.draw_cells()

m_screen.screen.onclick(m_click.by_click)
turtle.done()