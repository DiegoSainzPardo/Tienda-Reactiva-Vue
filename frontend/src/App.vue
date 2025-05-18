<template>
  <div class="app-container">
    <h1 class="title">Inventario de Productos</h1>

    <ul class="product-list">
      <li v-for="(producto, index) in productos" :key="producto.id" class="product-item">
        <div class="product-info">
          <div class="product-name">{{ producto.nombre }}</div>
          <div class="product-price">{{ producto.precio || 'N/A' }}€</div>
        </div>
        <div class="stock-info">
          <div>Stock: {{ producto.stock }}</div>
          <div :style="{ color: producto.disponible ? 'green' : 'red' }">
            {{ producto.disponible ? 'Disponible' : 'No Disponible' }}
          </div>
        </div>
        <div class="buttons">
          <button @click="modificarStock(producto.id, -1)" class="button reduce">Reducir stock</button>
          <button @click="modificarStock(producto.id, 1)" class="button increase">Aumentar stock</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue';

const API_URL = "http://localhost:5000/shopAPI"; // Ajusta si es diferente

export default defineComponent({
  name: 'App',
  setup() {
    const productos = ref([]);

    const fetchProductos = async () => {
      try {
        const response = await fetch(API_URL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            query: `
              query {
                productos {
                  id
                  nombre
                  precio
                  stock
                  disponible
                }
              }
            `
          })
        });

        const result = await response.json();
        if (result.data && result.data.productos) {
          productos.value = result.data.productos;
        } else {
          console.error("Error al obtener productos:", result.errors);
        }
      } catch (error) {
        console.error("Error de red al obtener productos:", error);
      }
    };

    const modificarStock = async (id, cambio) => {
      const producto = productos.value.find(p => p.id === id);
      if (!producto) return;

      try {
        const response = await fetch(API_URL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            query: `
              mutation ModificarStock($id: Int!, $stock: Int!) {
                modificarStock(id: $id, stock: $stock) {
                  producto {
                    id
                    stock
                    disponible
                  }
                }
              }
            `,
            variables: {
              id,
              stock: cambio
            }
          })
        });

        const result = await response.json();
        if (result.data && result.data.modificarStock) {
          const actualizado = result.data.modificarStock.producto;
          const index = productos.value.findIndex(p => p.id === actualizado.id);
          if (index !== -1) {
            productos.value[index].stock = actualizado.stock;
            productos.value[index].disponible = actualizado.disponible;
          }
        } else {
          console.error("Error al modificar stock:", result.errors);
        }
      } catch (error) {
        console.error("Error de red al modificar stock:", error);
      }
    };

    onMounted(fetchProductos);

    return {
      productos,
      modificarStock
    };
  }
});
</script>

<style>

body{
background-color: beige;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
gap: 12px
}

.title{
width: 100%;
text-align: center;
}

.product-list{
 display: grid;
 grid-template-columns: 1fr 1fr 1fr 1fr;
 gap: 8px;
}

.product-item{
column-span: 1;
background-color: white;
border-radius: 8px;
padding: 1rem 2rem;
display: flex;
flex-direction: column;
justify-content: center;
align-items: center;
gap: 4px;
}

.product-name{
font-weight: bold;
width: 100%;
text-align: center;
}

.product-price{
width: 100%;
text-align: center;
}

.stock-info{
width: 100%;
text-align: center;
}

.buttons{
display: flex;
gap: 4px;
}
</style>