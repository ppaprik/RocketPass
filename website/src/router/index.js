import { createRouter, createWebHistory } from 'vue-router';
import CartView from '../views/CartView.vue';
import PageView from '../views/PageView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: PageView,
    },
    {
      path: '/cart',
      name: 'cart',
      component: CartView,
    },
    {
      path: '/:page',
      name: 'page',
      component: PageView,
      props: true,
    },
  ],
});

export default router;
