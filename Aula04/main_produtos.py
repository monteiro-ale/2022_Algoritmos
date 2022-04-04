from Categoria import Categoria
from Produto import Produto

c1 = Categoria(1,"Bebidas")
p1 = Produto(1,"Guaraná", 7.99, 50, c1)
p1.cadastrar()
p2 = Produto()
p2.setCategoria()
p2.cadastrar()