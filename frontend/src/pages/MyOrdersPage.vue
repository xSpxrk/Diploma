<template>
    <div class="main">
        <customer-nav-bar></customer-nav-bar>
        <div class="background">
            <div class="offers">
                <h1 class="title">Мои заказы</h1>
                <div class="items">
                    <order-main v-for="order in this.orders.reverse()" :order="order" :key="order.order_id"></order-main>
            </div>
            </div>
        </div>
        <div ref="observer" class="observer"></div>
    </div>
</template>

<script>
import ProviderNavBar from '@/components/ProviderNavBar.vue'
import CustomerNavBar from '@/components/CustomerNavBar.vue'
import OrderMain from '@/components/OrderMain.vue'
import axios from 'axios'
    export default {
        components: {
            CustomerNavBar,
            ProviderNavBar,
            OrderMain
        },
        data() {
            return {
                type: localStorage.type,
                customer: Object,
                orders: []
            }
        },
        methods: {
            async getCustomer() {
                const response = await axios.get('https://bsm-backend.herokuapp.com/users',
                {
                    params: {
                        token: localStorage.token,
                    }
                })
                this.customer = response.data;
                this.orders = this.customer.orders;
            }
        },
        mounted() {
            this.getCustomer();
        },
        
    }
</script>

<style scoped>
.main {
    width: 100%;
    height: 100%;
}
.offers {
    padding: 20px 0;
    margin: 0 auto;
    width: 1440px;
    height: 100%;
}
.items {
    width: 100%;
    height: 100%;
}
.background {
    background: #458686;
    height: 100%;
}
.title {
    width: 100%;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 50px;
    line-height: 61px;
    text-align: center;
    color: #FFFFFF;
}
</style>