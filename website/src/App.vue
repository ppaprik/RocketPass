<template>
  <header>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/shop">Shop</RouterLink>
      <RouterLink to="/about">About Us</RouterLink>
      <RouterLink to="/contact">Contact</RouterLink>
      <RouterLink to="/blog">Blog</RouterLink>
      <RouterLink to="/faq">FAQ</RouterLink>
    </nav>
  </header>
  <main>
    <RouterView/>
  </main>
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>


<style>
  header {
    background-color: #333;
    /* padding: 1rem; */
    width: 100%;
    position: fixed;
    top: 0;
    left: 0;
  }

  nav {
    display: flex;
    justify-content: center;
    gap: 1rem;
  }

  nav a {
    color: white;
    align-items: center;

    text-decoration: none;
    font-size: 1.2rem;
    padding: 1rem 2rem 1rem 2rem;
  }

  nav a:hover {
    background-color: #444;
  }

  main {
    padding-top: 6rem;
    display: flex;
    justify-content: center;
  }
  </style>