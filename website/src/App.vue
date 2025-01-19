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
    FooterComponent,
  },
  data() {
    return {
      cartItems: [],
    };
  },
  methods: {
    // Updates the cart, saving it in localStorage
    updateCart(newCartItems) {
      this.cartItems = [...newCartItems];
      localStorage.setItem('cart', JSON.stringify(this.cartItems));
    },
    // Add item to cart (or increment quantity if it exists)
    addToCart(product) {
      const cartItem = this.cartItems.find(item => item.id === product.id);
      if (cartItem) {
        cartItem.quantity++;
      } else {
        this.cartItems.push({ ...product, quantity: 1 });
      }
      this.updateCart(this.cartItems);
    },
    // Increment item quantity
    incrementItem(item) {
      const cartItem = this.cartItems.find(cartItem => cartItem.id === item.id);
      if (cartItem) {
        cartItem.quantity++;
      }
      this.updateCart(this.cartItems);
    },
    // Decrement item quantity
    decrementItem(item) {
      const cartItem = this.cartItems.find(cartItem => cartItem.id === item.id);
      if (cartItem && cartItem.quantity > 1) {
        cartItem.quantity--;
      } else {
        this.removeFromCart(item);
      }
      this.updateCart(this.cartItems);
    },
    // Remove item from cart
    removeFromCart(item) {
      const index = this.cartItems.findIndex(cartItem => cartItem.id === item.id);
      if (index !== -1) {
        this.cartItems.splice(index, 1);
      }
      this.updateCart(this.cartItems);
    },
  },
  mounted() {
    const savedCart = JSON.parse(localStorage.getItem('cart'));
    if (savedCart) {
      this.cartItems = savedCart;
    }
  },
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
