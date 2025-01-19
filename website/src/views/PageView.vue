<template>
  <div class="page-container" :class="{ centerContent: isHomePage }">
    <!-- Dynamic content based on the route -->
    
    <!-- Services (Shop Page) -->
    <ServiceList v-if="isShopPage" @add-to-cart="addToCart" />
    
    <!-- About RocketPass (About Page) -->
    <AboutRocketPass v-if="isAboutPage" :aboutData="pageData.aboutRocketPass" />

    <Home v-if="isHomePage" :aboutData="pageData.aboutRocketPass" />
  </div>
</template>

<script>
import pagesData from '../pages.json'; // Assuming this is a JSON file for page data
import ServiceList from '../components/ServiceList.vue';
import AboutRocketPass from '../components/AboutRocketPass.vue';
import Home from '../components/Home.vue';

export default {
  name: 'PageView',
  components: {
    ServiceList,
    AboutRocketPass,
    Home
  },
  props: {
    cartItems: Array, // Receiving cartItems from parent (App.vue)
  },
  data() {
    return {
      pageData: {},
      isShopPage: false,
      isHomePage: false,
      isAboutPage: false,
    };
  },
  created() {
    this.loadPageData(); // Load data on component creation
  },
  watch: {
    $route() {
      this.loadPageData(); // Load page data when the route changes
    }
  },
  methods: {
    loadPageData() {
      const page = this.$route.params.page || 'home'; // Use params.page or default to 'home'

      this.pageData = pagesData[page] || this.$router.push('/');

      // Check the route and set the flags accordingly
      this.isShopPage = page === 'shop';
      this.isHomePage = page === 'home';
      this.isAboutPage = page === 'about';
    },
    // Add item to the cart and emit update-cart event
    addToCart(service) {
      const cartItem = this.cartItems.find((item) => item.id === service.id);
      if (cartItem) {
        cartItem.quantity++;
      } else {
        this.cartItems.push({ ...service, quantity: 1 });
      }
      this.$emit('update-cart', this.cartItems);
    }
  }
};
</script>

<style scoped>
.page-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  height: 100%;
  padding-top: 1rem;
}

.centerContent {
  min-height: calc(100vh - 6rem);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>