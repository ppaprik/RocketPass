<template>
  <div class="cart-container">
    <h1>Shopping Cart &nbsp; <i class="fa fa-credit-card" aria-hidden="true"></i></h1>
    <ul v-if="cartItems.length > 0">
      <li v-for="item in cartItems" :key="item.id" class="cart-item">
        <span>{{ item.name }} - ${{ item.price.toFixed(2) }}</span>
        <div class="quantity-controls">
          <button @click="incrementItem(item)">+</button>
          <button @click="decrementItem(item)" class="remove-button">-</button>
          <span>Quantity: {{ item.quantity }}</span>
        </div>
      </li>
    </ul>
    <p v-else>Your cart is empty.</p>
    <p>Total: &nbsp; {{ totalPrice.toFixed(2) }} €</p>
  </div>
</template>

<script>
export default {
  props: {
    cartItems: {
      type: Array,
      required: true,
    },
  },
  computed: {
    totalPrice() {
      return this.cartItems.reduce((total, item) => total + item.price * item.quantity, 0)
    },
  },
  methods: {
    incrementItem(item) {
      item.quantity++
      this.updateCart()
    },
    decrementItem(item) {
      item.quantity--
      if (item.quantity === 0) {
        this.removeFromCart(item)
      } else {
        this.updateCart()
      }
    },
    removeFromCart(item) {
      const index = this.cartItems.findIndex((cartItem) => cartItem.id === item.id)
      if (index !== -1) {
        this.cartItems.splice(index, 1)
        this.updateCart()
      }
    },
    updateCart() {
      this.$emit('update-cart', [...this.cartItems])
    },
  },
}
</script>

<style scoped>
h1 {
  font-size: 2rem;
  margin-bottom: 2rem;
  color: white;
  text-align: center;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li.cart-item {
  display: grid;
  grid-template-columns: 1fr 1fr; /* Two columns: 1/2 for item name and price, 1/2 for buttons */
  margin-bottom: 0.5rem;
  background-color: #222;
  border-radius: 0.5rem;
  padding: 0.5rem;
  align-items: center;
}

span {
  display: flex;
  align-items: center;
  width: fit-content;
}

.quantity-controls {
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

button {
  margin-left: 1rem;
  border-radius: 50px;
  padding: 0.5rem 0.7rem;
  background-color: white;
  color: #333;
  border: none;
  cursor: pointer;
}

.remove-button {
  /* margin-left: 1rem; */
  margin-right: 1.5rem;
  border-radius: 1rem;
  padding: 0.5rem 0.85rem;
  color: #333;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #777;
}

p {
  font-size: 1.2rem;
  margin-top: 2rem;
  text-align: center;
}

.cart-container {
  margin-top: 2rem;
  margin-bottom: 6rem;
  color: white;
  height: fit-content;
  background-color: #1a1a1a;
  padding: 2em;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  box-sizing: border-box;
}
</style>
