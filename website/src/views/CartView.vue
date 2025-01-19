<template>
  <ShoppingCart
    :cartItems="cartItems"
    @update-cart="updateCartHandler"
  />
</template>

<script>
import ShoppingCart from "@/components/ShoppingCart.vue";

export default {
  name: "CartView",
  components: {
    ShoppingCart,
  },
  data() {
    return {
      cartItems: [], // Example cartItems array with one item { id: 1, name: "Mars Expedition", price: 499999.99, quantity: 1 }
    };
  },
  methods: {
    updateCartHandler(updatedCart) {
      this.cartItems = updatedCart;
    },
  },
};
</script>
