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

### ¿Por qué es importante que el backend también actualice disponible y no depender solo del frontend?

Es importante que la lógica de disponibilidad esté controlada desde el backend, ya que esto asegura que los datos se mantengan consistentes en todo el sistema. Si esta lógica dependiera solo del frontend, se corre el riesgo de mostrar información desactualizada o incorrecta a otros usuarios o servicios. Al gestionarla desde el servidor, cualquier cambio en el stock se refleja de forma inmediata y coherente, sin importar si la acción se realizó desde una app móvil, una web, o una API externa.

### ¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?

Para asegurar la coherencia del sistema, la lógica que actualiza el stock debe encargarse también de ajustar el estado de disponibilidad en una sola operación transaccional. De esta forma se evitan inconsistencias que podrían aparecer si estas acciones se hicieran por separado. Al centralizar todo en el backend como única fuente de verdad, se reduce el riesgo de errores y se garantiza que todas las aplicaciones cliente consulten el mismo estado del inventario. Además, este enfoque simplifica el mantenimiento y permite escalar el sistema con mayor facilidad en el futuro.
  
