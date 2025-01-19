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
  methods: {
    updateCartHandler(updatedCart) {
      this.cartItems = updatedCart;
    },
  },
};
</script>