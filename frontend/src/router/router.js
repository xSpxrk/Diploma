import InfoPage from "@/pages/InfoPage.vue";
import MainPage from '@/pages/MainPage.vue';
import ProfilePage from '@/pages/ProfilePage.vue';
import OffersPage from '@/pages/MyOffersPage.vue';
import OrdersPage from '@/pages/OrdersPage.vue';
import OrderPage from '@/pages/OrderPage.vue';
import MyOrdersPage from '@/pages/MyOrdersPage.vue';
import {createRouter, createWebHistory} from "vue-router";

const routes = [
    {
        path: '/',
        component: InfoPage,
    },
    {
        path: '/main',
        component: MainPage
    },
    {
        path: '/profile',
        component: ProfilePage
    },
    {
        path: '/offers',
        component: OffersPage
    },
    {
        path: '/orders',
        component: OrdersPage
    },
    {
        path: '/order/:id',
        component: OrderPage
    },
    {
        path: '/my_orders',
        component: MyOrdersPage
    }
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router;