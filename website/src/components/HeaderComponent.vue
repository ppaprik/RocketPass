<template>
  <header>
    <nav>
      <!-- <a href="/"> <img src="../../favicon.png" alt="logo" class="logo"> </a> -->
      <RouterLink
        v-for="(page, key) in navigationLinks"
        :key="key"
        :to="`/${key}` === '/home' ? '/' : `/${key}`"
      >
        {{ page.title }}
      </RouterLink>
      <RouterLink to="/cart" class="cart">Cart ({{ totalItemsInCart }})</RouterLink>
    </nav>
  </header>
</template>

<script>
import { RouterLink } from 'vue-router';
import pagesData from '../pages.json'; // Adjust the path to your JSON file if needed

export default {
  name: 'HeaderComponent',
  props: {
    cartItems: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      navigationLinks: {},
    };
  },
  computed: {
    totalItemsInCart() {
      return this.cartItems.reduce((total, item) => total + item.quantity, 0);
    },
  },
  created() {
    this.navigationLinks = pagesData;
  },
};
</script>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #1a1a1a;
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

/* .logo {
  padding: 0rem;
  margin: 0;
  height: 2rem;
} */
</style>
