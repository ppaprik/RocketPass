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

<script>
import HeaderComponent from './components/HeaderComponent.vue';
import FooterComponent from './components/FooterComponent.vue';

export default {
  components: {
    HeaderComponent,
    FooterComponent
  },
  data() {
    return {
      cartItems: []
    };
  },
  methods: {
    updateCart(newCartItems) {
      this.cartItems = [...newCartItems];
      localStorage.setItem('cart', JSON.stringify(this.cartItems));
    },
    addToCart(product) {
      const cartItem = this.cartItems.find(item => item.id === product.id);
      if (cartItem) {
        cartItem.quantity++;
      } else {
        this.cartItems.push({ ...product, quantity: 1 });
      }
      this.updateCart(this.cartItems);
    },
    incrementItem(item) {
      const cartItem = this.cartItems.find(cartItem => cartItem.id === item.id);
      if (cartItem) {
        cartItem.quantity++;
      }
      this.updateCart(this.cartItems);
    },
    decrementItem(item) {
      const cartItem = this.cartItems.find(cartItem => cartItem.id === item.id);
      if (cartItem && cartItem.quantity > 1) {
        cartItem.quantity--;
      } else {
        this.removeFromCart(item);
      }
      this.updateCart(this.cartItems);
    },
    removeFromCart(item) {
      const index = this.cartItems.findIndex(cartItem => cartItem.id === item.id);
      if (index !== -1) {
        this.cartItems.splice(index, 1);
      }
      this.updateCart(this.cartItems);
    }
  },
  mounted() {
    const savedCart = JSON.parse(localStorage.getItem('cart'));
    if (savedCart) {
      this.cartItems = savedCart;
    }
  }
};
</script>

<style>
main {
  display: flex;
  justify-content: center;
  padding-top: 3rem;
  width: 100%;
  min-height: calc(100vh - 6rem); /* Ensure it takes full height minus header */
  box-sizing: border-box;
  text-align: center; /* Center text alignment */
}
</style>
