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

Es crucial que el backend maneje la lógica de disponibilidad (disponible) porque garantiza la integridad de los datos en todo el sistema. Si solo el frontend decide cuándo un producto está disponible, se corre el riesgo de que otros clientes o servicios consuman información desactualizada o incorrecta. Al centralizar esta lógica en el servidor, se asegura que cualquier cambio en el stock refleje inmediatamente y de forma coherente si un producto está disponible, sin importar desde dónde se realice la operación (por ejemplo, desde una app móvil, otro frontend, o una API externa).

### ¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?

Para garantizar coherencia, la lógica que actualiza el stock también debe encargarse de revisar y ajustar el estado de disponibilidad en una sola operación transaccional. Esto evita inconsistencias que podrían surgir si estas actualizaciones se realizan por separado. Además, al tener una única fuente de verdad en el backend, se minimiza el riesgo de errores y se asegura que todas las aplicaciones cliente vean el mismo estado del inventario. Esta práctica también facilita el mantenimiento y la escalabilidad del sistema a largo plazo.
  
