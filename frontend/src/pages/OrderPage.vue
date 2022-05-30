<template>
    <div class="main" v-show="this.type == 'customer'">
        <customer-nav-bar></customer-nav-bar>
             <div class="order_main">
                <h1 class="title">Заказ</h1>
                <div class="items">
                    <order :order="this.order"></order>
                    <offer v-for="offer in offers.reverse()" :offer="offer" :key="offer.offer_id"></offer>
                </div>
        </div>
    </div>
    <div class="main" v-show="this.type == 'provider'">
        <dialog-window v-model:show="offerVisible">
          <offer-dialog @offer="createOffer"></offer-dialog>
        </dialog-window>
        <provider-nav-bar></provider-nav-bar>
        <div class="order_main">
                <h1 class="title">Заказ</h1>
                <div class="items">
                    <order  @openDialog="openDialog" class="main_order" :order="this.order"></order>
                    <offer v-for="offer in offers.reverse()" :offer="offer" :key="offer.offer_id"></offer>
                </div>
        </div>
    </div>
</template>

<script>
import ProviderNavBar from '@/components/ProviderNavBar.vue'
import CustomerNavBar from '@/components/CustomerNavBar.vue'
import OfferDialog from '@/components/OfferDialog.vue'
import Order from '@/components/Order.vue'
import Offer from '@/components/Offer.vue'
import axios from 'axios'
    export default {
        components: {
            CustomerNavBar,
            ProviderNavBar,
            Order,
            Offer,
            OfferDialog
        },
        data() {
            return {
                type: localStorage.type,
                id: 0,
                order: Object,
                offers: [],
                offerVisible: false,
            }
        },
        methods: {
            getId() {
                return parseInt(this.$route.params.id);
            },
            async getOrder(id) {
                const response = await axios.get('http://127.0.0.1:8000/orders/' + id );
                this.order = response.data;
                this.offers = this.order.offers;
            },
            async createOffer(offer) {
                const response = await axios.post('http://127.0.0.1:8000/offers/', {
                    quantity: offer.quantity,
                    price: offer.price,
                    order_id: this.order.order_id,
                    provider_id: null
                },
                {
                    params: {
                        token: localStorage.token
                    },
                });
                this.getOrder(this.$route.params.id);
                this.offerVisible = false;
        
            },
            openDialog(show) {
                this.offerVisible = show;
            }
        },
        mounted() {
            this.getId();
            this.getOrder(this.getId());
        },
        
    }
</script>

<style scoped>
.main {
    width: 100%;
    height: 100%;
}
.background {
    background: url("@/resources/images/orders_rectangle.svg") no-repeat;
    height: 100%;
}
.order_main {
    padding: 20px 0;
    margin: 0 auto;
    width: 1440px;
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

    color: #3F4155;
}
.items {
    width: 100%;
    height: 100%;
}
</style>