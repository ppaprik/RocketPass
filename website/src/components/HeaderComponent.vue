<template>
    <header>
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/shop">Services</RouterLink>
        <RouterLink to="/about">About Us</RouterLink>
        <RouterLink to="/contact">Contact</RouterLink>
        <RouterLink to="/blog">Blog</RouterLink>
        <RouterLink to="/faq">FAQ</RouterLink>
        <RouterLink to="/cart" class="cart">Cart ({{ totalItemsInCart }})</RouterLink>
      </nav>
    </header>
  </template>
  
  <script setup>
  import { RouterLink } from 'vue-router';
  import { computed, toRefs } from 'vue';
  
  const props = defineProps({
    cartItems: {
      type: Array,
      required: true
    }
  });
  
  const { cartItems } = toRefs(props);
  
  const totalItemsInCart = computed(() => {
    return cartItems.value.reduce((total, item) => total + item.quantity, 0);
  });
  </script>
  
  <style scoped>
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #1a1a1a;
    /* padding: 1rem; */
    padding-left: 4rem;
    padding-right: 2rem;
    width: 100%;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 10; /* Ensure header stays on top */
  }
  
  nav {
    display: flex;
    flex-grow: 1;
  }
  
  nav .cart {
    margin-left: auto;
  }
  
  nav a {
    color: white;
    text-decoration: none;
    font-size: 1.1rem;
    padding: 1rem 1.5rem 1rem 1.5rem;
  }
  
  nav a:hover {
    background-color: #444;
  }
  </style>
  