import graphene
from graphene import ObjectType, Int, Float, String, Boolean, List, Field
from models import productos_db

class ProductoType(ObjectType):
    id = Int()
    nombre = String()
    precio = Float()
    stock = Int()
    disponible = Boolean()

class Consulta(ObjectType):
    productos = List(ProductoType)

    def resolve_productos(self, info):
        return productos_db

class ModificarStock(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        stock = Int(required=True)

    producto = Field(lambda: ProductoType)

    def mutate(self, info, id, stock):
        for producto in productos_db:
            if producto["id"] == id:
                producto["stock"] += stock

                if producto["stock"] <= 0:
                    producto["stock"] = 0
                    producto["disponible"] = False
                else:
                    producto["disponible"] = True

                return ModificarStock(producto=producto)

        raise Exception("Producto no encontrado")

class Mutacion(ObjectType):
    modificar_stock = ModificarStock.Field()

schema = graphene.Schema(query=Consulta, mutation=Mutacion)
