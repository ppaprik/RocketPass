<template>
  <div>
    <div class="product-container-wrapper">
      <div class="product-container">
        <div class="product" v-for="product in products" :key="product.id">
          <img :src="product.image" :alt="product.name" />
          <h3>{{ product.name }}</h3>
          <p>{{ product.description }}</p>
          <p>Price: ${{ product.price.toFixed(2) }}</p>
        </div>
      </div>
    </div>
  </div>
</template>



<script>
import productsData from '../products.json';

export default {
  data() {
    return {
      products: productsData
    };
  }
};
</script>


<style scoped>
.product-container-wrapper {
  display: flex;
  justify-content: center;
  padding: 1rem;
}

.product-container {
  display: grid;
  grid-template-columns: repeat(3, minmax(400px, 1fr));
  gap: 1rem;
}

.product {
  border: 0.2rem solid #ddd;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-sizing: border-box;
  color: black;
  background-color: white;
}

.product img {
  max-width: 100px;
  margin-bottom: 1rem;
}

.product h3 {
  font-size: 1.5rem;
  margin: 0.5rem 0;
}

.product p {
  font-size: 1rem;
  color: #666;
}

.product p:last-child {
  font-weight: bold;
  color: #333;
}
</style>

