# Tienda Online con Vue - Sistema de Inventario

Este proyecto implementa un sistema de gestión de inventario para una tienda online utilizando Vue.js. El sistema permite manejar productos con nombre, precio, stock y disponibilidad, actualizando la interfaz de usuario automáticamente según el stock de los productos.

## Respuestas a las preguntas planteadas

### Vue no detecta cambios dentro de objetos reactivos de la forma que esperarías. ¿Cómo podrías observar un cambio en una propiedad anidada?

Vue detecta cambios en las propiedades de objetos reactivos, pero puede haber casos en los que no detecta cambios en propiedades anidadas de manera predeterminada. Esto sucede porque Vue no puede "profundizar" automáticamente en objetos dentro de otros objetos para observar los cambios.

Para solucionar esto, usamos `watch()` para observar propiedades anidadas. En este caso, estamos observando la propiedad `stock` dentro de un array de productos. Dado que `stock` puede cambiar sin que Vue lo detecte automáticamente, usamos un `watch` que mapea el array de productos y observa los cambios en la propiedad `stock` de cada uno:


a función watch() en Vue.js permite escuchar y reaccionar ante cambios en propiedades específicas dentro de un objeto reactivo. Cuando se usa reactive(), Vue crea una versión reactiva del objeto, y watch() nos permite monitorear de forma más detallada las propiedades de ese objeto.


watch() permite escuchar cambios en propiedades específicas dentro de reactive(), ¿cómo funciona?

En este caso, estamos utilizando watch() para observar cambios en el array inventory, específicamente en los valores de la propiedad stock de cada producto. Usamos una función que devuelve una lista de los valores de stock:

El primer argumento de watch es una función que devuelve una lista de valores que se desean observar (en este caso, stock de cada producto).

El segundo argumento es el callback que se ejecuta cada vez que alguno de los valores observados cambia. En este caso, el callback actualiza la propiedad disponible de cada producto según el valor de stock.

¿Cómo harías que un watch() detecte cambios en stock dentro de un array de productos?

Para que un watch() detecte cambios en stock dentro de un array de productos, debemos observar específicamente la propiedad stock de cada producto en el array. Como Vue no puede observar directamente los cambios en propiedades anidadas dentro de un array, usamos map() para crear una lista de todos los valores de stock y luego observamos esa lista.
