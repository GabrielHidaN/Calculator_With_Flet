import flet as ft
from flet import colors

def  main (page:ft.Page):
  page.bgcolor = "#000"
  page.window_resizable = False
  page.window_width = 250
  page.window_height = 380
  page.title = 'Calculadora'
  page.window_always_on_top = True

  result = ft.Text(value= '0' , color= colors.WHITE , size= 20)

  display = ft.Row(
    width= 250,
    controls=[result],
    alignment= 'end'

  )
  page.add(display)











ft.app(target = main)
