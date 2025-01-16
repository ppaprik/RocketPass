<template>
    <header>
        <nav>
            <RouterLink to="/">Home</RouterLink>
            <RouterLink to="/shop">Shop</RouterLink>
            <RouterLink to="/about">About Us</RouterLink>
            <RouterLink to="/contact">Contact</RouterLink>
            <RouterLink to="/blog">Blog</RouterLink>
            <RouterLink to="/faq">FAQ</RouterLink>
            <RouterLink to="/cart">Cart ({{ totalItemsInCart }})</RouterLink>
        </nav>
    </header>
    <main>
        <RouterView
            @update-cart="updateCart"
            :cartItems="cartItems"
            @increment-item="incrementItem"
            @decrement-item="decrementItem"
            @remove-from-cart="removeFromCart"
        />
    </main>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { reactive, computed, onMounted } from 'vue'

const cartItems = reactive([])

const totalItemsInCart = computed(() => {
    return cartItems.reduce((total, item) => total + item.quantity, 0)
})

function updateCart(newCartItems) {
    cartItems.length = 0
    newCartItems.forEach((item) => cartItems.push(item))
    localStorage.setItem('cart', JSON.stringify(cartItems))
}

function addToCart(product) {
    const cartItem = cartItems.find((item) => item.id === product.id)
    if (cartItem) {
        cartItem.quantity++
    } else {
        cartItems.push({ ...product, quantity: 1 })
    }
    updateCart(cartItems)
}

function incrementItem(item) {
    const cartItem = cartItems.find((cartItem) => cartItem.id === item.id)
    if (cartItem) {
        cartItem.quantity++
    }
    updateCart(cartItems)
}

function decrementItem(item) {
    const cartItem = cartItems.find((cartItem) => cartItem.id === item.id)
    if (cartItem && cartItem.quantity > 1) {
        cartItem.quantity--
    } else {
        removeFromCart(item)
    }
    updateCart(cartItems)
}

function removeFromCart(item) {
    const index = cartItems.findIndex((cartItem) => cartItem.id === item.id)
    if (index !== -1) {
        cartItems.splice(index, 1)
    }
    updateCart(cartItems)
}

onMounted(() => {
    const savedCart = JSON.parse(localStorage.getItem('cart'))
    if (savedCart) {
        cartItems.push(...savedCart)
    }
})
</script>

<style>
header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #333;
    padding: 1rem;
    width: 100%;
    position: fixed;
    top: 0;
    left: 0;
}

nav {
    display: flex;
    gap: 1rem;
}

nav a {
    color: white;
    text-decoration: none;
    font-size: 1.2rem;
    padding: 1rem;
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
