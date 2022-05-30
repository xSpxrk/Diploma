<template>
    <div class="main">
        <provider-nav-bar></provider-nav-bar>
        <div class="background">
            <div class="offers">
                <h1 class="title">Мои предложения</h1>
                <div class="items">
                    <offer-main v-for="offer in this.offers.reverse()" :offer="offer" :key="offer.offer_id"></offer-main>
            </div>
            </div>
        </div>
        <div ref="observer" class="observer"></div>
    </div>
</template>

<script>
import ProviderNavBar from '@/components/ProviderNavBar.vue'
import CustomerNavBar from '@/components/CustomerNavBar.vue'
import OfferMain from '@/components/OfferMain.vue'
import axios from 'axios'
    export default {
        components: {
            CustomerNavBar,
            ProviderNavBar,
            OfferMain
        },
        data() {
            return {
                type: localStorage.type,
                provider: Object,
                offers: []
            }
        },
        methods: {
            async getProvider() {
                const response = await axios.get('http://127.0.0.1:8000/users',
                {
                    params: {
                        token: localStorage.token,
                    }
                })
                this.provider = response.data
                this.offers = this.provider.offers;
            }
        },
        mounted() {
            this.getProvider();
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
    background: #DF7373;
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