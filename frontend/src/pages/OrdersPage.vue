<template>
    <div class="main">
        <provider-nav-bar></provider-nav-bar>
        <div class="background">
            <div class="orders">
                <h1 class="title__customer">Заказы</h1>
                <div class="items">
                    <order-main v-for="order in this.orders.reverse()" :order="order" :key="order.order_id"></order-main>
                </div>
            </div>
        <div ref="observer" class="observer"></div>
        </div>
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
                orders: [],
                skip: 0,
                limit: 3,
                maxOrders: 0
            }
        },
        methods: {
            async getOrders() {
                const response = await axios.get('http://127.0.0.1:8000/orders/', {
                    params: {
                    skip: this.skip,
                    limit: this.limit,
                    }

                });
                this.orders = [...this.orders, ...response.data].sort((a, b) => a.offer_id > b.offer_id ? 1 : -1).reverse();
                
                this.skip = this.limit;
                this.limit += 1;
            },
            async getMax() {
                const max = await axios.get('http://127.0.0.1:8000/orders/max/');
                this.maxOrders = max.data;
            }
            
        },
        mounted() {
            this.getOrders();
            this.getMax();
            const options = {
            rootMargin: '0px',
            threshold: 1.0
            }
            const callback = (entries, observer) => {
                if (entries[0].isIntersecting && this.orders.length < this.maxOrders) {
                    this.getOrders()
                }
            };
            const observer = new IntersectionObserver(callback, options);
            observer.observe(this.$refs.observer);
        },
        
    }
</script>

<style scoped>
.main {
    width: 100%;
    height: 100%;
}
.background {
    background: #458686 no-repeat;
    height: 100%;
}
.title__customer {
    width: 100%;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 50px;
    line-height: 61px;
    text-align: center;
    color: #FFFFFF;
}
.orders {
    padding: 20px 0;
    margin: 0 auto;
    width: 1440px;
    height: 100%;
}
.items {
    width: 100%;
    height: 100%;
}
.observer {
    height: 10px;
}
</style>