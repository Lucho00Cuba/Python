# Herencia a la POO

#class Producto:
#    def __init__(self,referencia,tipo,nombre,pvp,descripcion,productor=None,distribuidor=None,isbn=None,autor=None):
#        self.referencia = referencia
#        self.tipo = tipo
#        self.nombre = nombre
#        self.pvp = pvp
#        self.descripcion = descripcion
#        self.productor = productor
#        self.distribuidor = distribuidor
#        self.isbn = isbn
#        self.autor = autor
#
#adorno = Producto('000A','ADORNO','Vaso Adornado',15,'Vaso de porcelana con dibujos')
#print(adorno)
#print(adorno.tipo)

#class Producto:
#    def __init__(self,referencia,nombre,pvp,descripcion):
#        self.referencia = referencia
#        self.nombre = nombre
#        self.pvp = pvp
#        self.descripcion = descripcion
#    
#    def __str__(self):
#        return """\
#        REFERECENCIA    {r}
#        NOMBRE          {n}
#        PVP             {p}
#        DESCRIPCION     {d}.""".format(r=self.referencia,n=self.nombre,p=self.pvp,d=self.descripcion)
#
#class Adorno(Producto):
#    pass
#
#class Alimento(Producto):
#    productor = ""
#    distribuidor = ""
#
#    def __str__(self):
#        return """\
#        REFERECENCIA    {r}
#        NOMBRE          {n}
#        PVP             {p}
#        DESCRIPCION     {d}.
#        PRODUCTOR       {po}
#        DISTRIBUIDOR    {di}""".format(r=self.referencia,n=self.nombre,p=self.pvp,d=self.descripcion,po=self.productor,di=self.distribuidor)
#
#class Libro(Producto):
#    isbn = ""
#    autor = ""
#
#    def __str__(self):
#        return """\
#        REFERECENCIA    {r}
#        NOMBRE          {n}
#        PVP             {p}
#        DESCRIPCION     {d}
#        ISBN            {i}
#        AUTOR           {a}""".format(r=self.referencia,n=self.nombre,p=self.pvp,d=self.descripcion,i=self.isbn,a=self.autor)
#
#
#a = Adorno(2034,"Vaso Adornado",15,"Vaso de Porcelana")
#al = Alimento(2035,"Botella de Aceite",5,"250 ML")
#al.productor = "La Aceitera"
#al.distribuidor = "Dist SA"
#li = Libro(2036,"Cocina",9,"Recetas")
#li.isbn = "0-123456-78-9"
#li.autor = "Chef"
#
#productos = [a,al]
#productos.append(li)
##print(productos)
#
##for i in productos:
#    #print(i.referencia,i.nombre)
#
#for p in productos:
#    if ( isinstance(p, Adorno) ):
#        print(p.referencia,p.nombre)
#    elif ( isinstance(p, Alimento)):
#        print(p.referencia,p.nombre,p.productor)
#    elif ( isinstance(p, Libro)):
#        print(p.referencia,p.nombre,p.isbn)
#
#def oferta(p,oferta):
#    # Oferta de producto
#    p.pvp = p.pvp - (p.pvp/100*oferta)
#    return p
#
#al_oferta = oferta(al,10)
#print(al_oferta)

#print("Adorno\n",a)
#print("Alimento\n",al)
#print("Libro\n",li)

####################################################

# Herencia Multiple

class A:
    def __init__(self):
        print("Soy de clase A")

    def a(self):
        print("Este metodo lo heredo de A")

class B:
    def __init__(self):
        print("Soy de clase B")
    def b(self):
        print("Este metodo lo heredo de B")

class C(A,B):
    def c(self):
        print("Este metodo es de C")

c = C()
print(c.a())