<template>
    <HeaderComponent :cartItems="cartItems" />
    <main>
      <RouterView
        @update-cart="updateCart"
        :cartItems="cartItems"
        @increment-item="incrementItem"
        @decrement-item="decrementItem"
        @remove-from-cart="removeFromCart"
      />
    </main>
    <FooterComponent />
  </template>
  
  <script setup>
  import HeaderComponent from './components/HeaderComponent.vue';
  import FooterComponent from './components/FooterComponent.vue';
  import { reactive, onMounted } from 'vue';
  
  const cartItems = reactive([]);
  
  function updateCart(newCartItems) {
    cartItems.length = 0;
    newCartItems.forEach(item => cartItems.push(item));
    localStorage.setItem('cart', JSON.stringify(cartItems));
  }
  
  function addToCart(product) {
    const cartItem = cartItems.find(item => item.id === product.id);
    if (cartItem) {
      cartItem.quantity++;
    } else {
      cartItems.push({ ...product, quantity: 1 });
    }
    updateCart(cartItems);
  }
  
  function incrementItem(item) {
    const cartItem = cartItems.find(cartItem => cartItem.id === item.id);
    if (cartItem) {
      cartItem.quantity++;
    }
    updateCart(cartItems);
  }
  
  function decrementItem(item) {
    const cartItem = cartItems.find(cartItem => cartItem.id === item.id);
    if (cartItem && cartItem.quantity > 1) {
      cartItem.quantity--;
    } else {
      removeFromCart(item);
    }
    updateCart(cartItems);
  }
  
  function removeFromCart(item) {
    const index = cartItems.findIndex(cartItem => cartItem.id === item.id);
    if (index !== -1) {
      cartItems.splice(index, 1);
    }
    updateCart(cartItems);
  }
  
  onMounted(() => {
    const savedCart = JSON.parse(localStorage.getItem('cart'));
    if (savedCart) {
      cartItems.push(...savedCart);
    }
  });
  </script>
  
  <style>
  main {
    display: flex;
    justify-content: center;
    padding-top: 6rem;
    width: 100%;
    min-height: calc(100vh - 6rem); /* Ensure it takes full height minus header */
    box-sizing: border-box;
    text-align: center; /* Center text alignment */
  }
  </style>
  