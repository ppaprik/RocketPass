<template>
  <div class="page-container" :class="{ centerContent: isHomePage }">
    <p v-if="!isShopPage && !isAboutPage">{{ pageData.content }}</p>
    <ServiceList v-if="isShopPage" @add-to-cart="addToCart" />
    <AboutRocketPass v-if="isAboutPage" :aboutData="pageData.aboutRocketPass" />
  </div>
</template>

<script>
import pagesData from '../pages.json'
import ServiceList from '../components/ServiceList.vue'
import AboutRocketPass from '../components/AboutRocketPass.vue'

export default {
  components: {
    ServiceList,
    AboutRocketPass,
  },
  data() {
    return {
      pageData: {},
      isShopPage: false,
      isHomePage: false,
      isAboutPage: false,
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
      this.isHomePage = page === 'home'
      this.isAboutPage = page === 'about'
    },
    addToCart(service) {
      const cartItem = this.cartItems.find((item) => item.id === service.id)
      if (cartItem) {
        cartItem.quantity++
      } else {
        this.cartItems.push({ ...service, quantity: 1 })
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
.page-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  height: 100%; /* Ensure it takes the full height of the main container */
}

.centerContent {
  min-height: calc(100vh - 6rem); /* Adjust for header height */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
