<template>
    <div class="main" v-show="this.type == 'customer'">
        <customer-nav-bar></customer-nav-bar>
        <div class="background__customer">
            <div class="orders">
                <h1 class="title__customer">Последние заказы</h1>
                <div class="items">
                    <order-main v-for="order in this.sortOrders().slice(0, 3)" :order="order" :key="order.order_id"></order-main>
            </div>
            </div>
           
        </div>
    </div>
    <div class="main" v-show="this.type == 'provider'">
        <provider-nav-bar></provider-nav-bar>
        <div class="background__provider">
            <div class="offers">
                <h1 class="title__provider">Последние предложения</h1>
                <div class="items">
                    <offer-main v-for="offer in this.sortOffers().slice(0, 3)" :offer="offer" :key="offer.offer_id"></offer-main>
            </div>
            </div>
        </div>
    </div>
</template>

<script>
import ProviderNavBar from '@/components/ProviderNavBar.vue'
import OrderMain from '@/components/OrderMain.vue'
import CustomerNavBar from '@/components/CustomerNavBar.vue'
import OfferMain from '@/components/OfferMain.vue'
import axios from 'axios'
    export default {
        components: {
            CustomerNavBar,
            OrderMain,
            OfferMain,
            ProviderNavBar
        },
        data() {
            return {
                orders: [],
                type: localStorage.type,
                offers: []
            }
        },
        methods: {
            async getOrders() {
                const response = await axios.get('http://127.0.0.1:8000/customers/one', {
                    headers: {
                        'Authorization': localStorage.token
                    }
                });
                this.orders = response.data.orders;
                console.log(response);
            },
            async getOffers() {
                const response = await axios.get('http://127.0.0.1:8000/providers/one', {
                    headers: {
                        'Authorization': localStorage.token
                    }
                }
                );
                this.offers = response.data.offers;
                console.log(response)
            },
            sortOffers() {
                return this.offers.sort((a, b) => a.offer_id > b.offer_id ? 1 : -1).reverse();
            },
            sortOrders() {
                return this.orders.sort((a, b) => a.offer_id > b.offer_id ? 1 : -1);

            }
        },
        mounted() {
            if (this.type == 'customer') {
                this.getOrders();
            } else {
                this.getOffers();
            }

            
        },
    }
</script>

<style scoped>
.main {
    width: 100%;
    height: 100%;
}
.background__customer {
    background: url("@/resources/images/orders_rectangle.svg") no-repeat;
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
.background__provider {
    background: url("@/resources/images/offers_rectangle.svg") no-repeat;
    height: 100%;
}
.offers {
    padding: 20px 0;
    margin: 0 auto;
    width: 1440px;
    height: 100%;
}
.title__provider {
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