<template>
    <div>
        <h1>Shopping Cart</h1>
        <ul v-if="cartItems.length > 0">
            <li v-for="item in cartItems" :key="item.id">
                {{ item.name }} - ${{ item.price.toFixed(2) }} - Quantity: {{ item.quantity }}
                <button @click="incrementItem(item)">+</button>
                <button @click="decrementItem(item)">-</button>
            </li>
        </ul>
        <p v-else>Your cart is empty.</p>
        <p>Total: ${{ totalPrice.toFixed(2) }}</p>
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
            item.quantity++;
            this.updateCart();
        },
        decrementItem(item) {
            if (item.quantity > 1) {
                item.quantity--;
                this.updateCart();
            } else {
                this.removeFromCart(item);
            }
        },
        removeFromCart(item) {
            const index = this.cartItems.findIndex(cartItem => cartItem.id === item.id);
            if (index !== -1) {
                this.cartItems.splice(index, 1);
                this.updateCart();
            }
        },
        updateCart() {
            this.$emit('update-cart', [...this.cartItems]);
        }
    }
}
</script>

<style scoped>
h1 {
    font-size: 2rem;
    margin-bottom: 1rem;
}

ul {
    list-style: none;
    padding: 0;
}

li {
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
}

button {
    margin-left: 1rem;
    padding: 0.5rem;
    background-color: #333;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #555;
}

p {
    font-size: 1.5rem;
    margin-top: 1rem;
}
</style>