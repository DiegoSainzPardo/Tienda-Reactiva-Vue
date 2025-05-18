# Tienda con Flask + GraphQL + Vue.js

Aplicación para gestionar inventario de productos usando un backend en Flask con GraphQL (`graphene`) y un frontend en Vue.js.

## Instalación y ejecución

### 1. Clonar repositorio

git clone https://github.com/DiegoSainzPardo/Tienda-Reactiva-Vue.git

cd Tienda-Reactiva-Vue

cd backend

pip install flask flask_cors graphene

### 2. Ejecutar Servidor
python.exe app.py

cd ../frontend

npm install

npm run dev

### 3. Disfrutar

### 4. Preguntas

### ¿Qué ventajas ofrece GraphQL sobre REST en este contexto?

- **Obtención precisa de datos**: GraphQL permite al cliente solicitar solo los campos que necesita, evitando transferencias innecesarias.
- **Menos solicitudes al servidor**: Se pueden combinar múltiples operaciones en una sola petición.
- **Mayor flexibilidad**: El frontend puede adaptarse a nuevos requerimientos sin que el backend tenga que cambiar sus endpoints.
- **Esquema auto-documentado**: GraphQL actúa como contrato tipado entre frontend y backend, lo cual facilita el desarrollo.

### ¿Cómo se definen los tipos y resolvers en una API con GraphQL?

- **Tipos (`ObjectType`)**: Representan entidades de datos. Por ejemplo, un `ProductType` incluye campos como `id`, `name`, `stock` y `available`.
  
  ```python
  class ProductType(ObjectType):
      id = Int()
      name = String()
      price = Float()
      stock = Int()
      available = Boolean()

  
