<template>
  <div class="app-container">
    <h1 class="title">Inventario de Productos</h1>

    <!-- Formulario para añadir productos -->
    <div class="form-container">
      <div class="form-field">
        <input v-model="nuevoProducto.nombre" placeholder="Nombre del Producto" class="input" />
      </div>
      <div class="form-field">
        <input v-model.number="nuevoProducto.stock" placeholder="Stock" type="number" class="input" />
      </div>
      <div class="form-field">
        <input v-model.number="nuevoProducto.precio" placeholder="Precio" type="number" class="input" />
      </div>
      <button @click="agregarProducto" class="button">Añadir Producto</button>
    </div>

    <!-- Mostrar el inventario -->
    <ul class="product-list">
      <li v-for="(producto, index) in inventory" :key="index" class="product-item">
        <div class="product-info">
          <div class="product-name">{{ producto.nombre }}</div>
          <div class="product-price">€{{ producto.precio }}</div>
        </div>
        <div class="stock-info">
          <div>Stock: {{ producto.stock }}</div>
          <div :style="{ color: producto.disponible ? 'green' : 'red' }">
            {{ producto.disponible ? 'Disponible' : 'No Disponible' }}
          </div>
        </div>
        <div class="buttons">
          <button @click="reducirStock(index)" class="button reduce">Reducir stock</button>
          <button @click="aumentarStock(index)" class="button increase">Aumentar stock</button>
          <!-- Botón para eliminar producto -->
          <button @click="eliminarProducto(index)" class="button remove">Eliminar</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import { defineComponent, reactive, watch } from 'vue';

// Importamos el archivo CSS
import './assets/main.css';

export default defineComponent({
  name: 'App',
  setup() {
    const inventory = reactive([
      { nombre: 'Producto A', precio: 100, stock: 5, disponible: true },
      { nombre: 'Producto B', precio: 200, stock: 0, disponible: false },
      { nombre: 'Producto C', precio: 150, stock: 2, disponible: true }
    ]);

    const nuevoProducto = reactive({
      nombre: '',
      stock: 0,
      precio: 0
    });

    watch(
      () => inventory.map(producto => producto.stock),
      (newStocks) => {
        newStocks.forEach((stock, index) => {
          inventory[index].disponible = stock > 0;
        });
      }
    );

    const reducirStock = (index) => {
      if (inventory[index].stock > 0) {
        inventory[index].stock--;
      }
    };

    const aumentarStock = (index) => {
      inventory[index].stock++;
    };

    const agregarProducto = () => {
      if (nuevoProducto.nombre && nuevoProducto.stock >= 0 && nuevoProducto.precio >= 0) {
        inventory.push({
          nombre: nuevoProducto.nombre,
          precio: nuevoProducto.precio,
          stock: nuevoProducto.stock,
          disponible: nuevoProducto.stock > 0
        });
        nuevoProducto.nombre = '';  // Limpiar el campo nombre
        nuevoProducto.stock = 0;  // Limpiar el campo stock
        nuevoProducto.precio = 0; // Limpiar el campo precio
      } else {
        alert("Por favor, ingrese un nombre, un stock y un precio válidos.");
      }
    };

    // Función para eliminar producto
    const eliminarProducto = (index) => {
      inventory.splice(index, 1);  // Elimina el producto en el índice dado
    };

    return { inventory, reducirStock, aumentarStock, nuevoProducto, agregarProducto, eliminarProducto };
  }
});
</script>
