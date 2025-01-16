import { createRouter, createWebHistory } from 'vue-router'
import PageView from '../views/PageView.vue'
import CartView from '../views/CartView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: PageView,
        },
        {
            path: '/shop',
            name: 'shop',
            component: PageView,
        },
        {
            path: '/about',
            name: 'about',
            // route level code-splitting
            // this generates a separate chunk (About.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import('../views/PageView.vue'),
        },
        {
            path: '/contact',
            name: 'contact',
            component: PageView,
        },
        {
            path: '/blog',
            name: 'blog',
            component: PageView,
        },
        {
            path: '/faq',
            name: 'faq',
            component: PageView,
        },
        {
            path: '/cart',
            name: 'cart',
            component: CartView,
        },
    ],
})

export default router
