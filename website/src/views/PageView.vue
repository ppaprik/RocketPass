<template>
    <div>
        <p v-if="!isShopPage">{{ pageData.content }}</p>
        <ProductList v-if="isShopPage" @add-to-cart="addToCart" />
    </div>
</template>

<script>
import pagesData from '../pages.json'
import ProductList from '../components/ProductList.vue'

export default {
    components: {
        ProductList,
    },
    data() {
        return {
            pageData: {},
            isShopPage: false,
            cartItems: JSON.parse(localStorage.getItem('cart')) || [],
        }
    },
    created() {
        this.loadPageData()
    },
    watch: {
        $route() {
            this.loadPageData()
        },
    },
    methods: {
        loadPageData() {
            const page = this.$route.name
            this.pageData = pagesData[page] || {
                title: 'Page Not Found',
                content: 'Sorry, this page does not exist.',
            }
            this.isShopPage = page === 'shop'
        },
        addToCart(product) {
            const cartItem = this.cartItems.find((item) => item.id === product.id)
            if (cartItem) {
                cartItem.quantity++
            } else {
                this.cartItems.push({ ...product, quantity: 1 })
            }
            this.updateCart(this.cartItems)
        },
        incrementItem(item) {
            const cartItem = this.cartItems.find((cartItem) => cartItem.id === item.id)
            if (cartItem) {
                cartItem.quantity++
            }
            this.updateCart(this.cartItems)
        },
        decrementItem(item) {
            const cartItem = this.cartItems.find((cartItem) => cartItem.id === item.id)
            if (cartItem && cartItem.quantity > 1) {
                cartItem.quantity--
            } else {
                this.removeFromCart(item)
            }
            this.updateCart(this.cartItems)
        },
        removeFromCart(item) {
            const index = this.cartItems.findIndex((cartItem) => cartItem.id === item.id)
            if (index !== -1) {
                this.cartItems.splice(index, 1)
            }
            this.updateCart(this.cartItems)
        },
        updateCart(newCartItems) {
            localStorage.setItem('cart', JSON.stringify(newCartItems))
            this.$emit('update-cart', newCartItems)
        },
    },
}
</script>

<style scoped>
h1 {
    font-size: 2rem;
    color: #333;
}

p {
    font-size: 1.2rem;
    color: #666;
}
</style>
