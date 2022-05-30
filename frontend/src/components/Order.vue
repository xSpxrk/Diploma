<template>
    <div class="order">
        <div class="title">
            <div class="name">{{ customer }}</div>
            <div class="btn">
                <div @click="letOffer" v-show="this.type == 'provider'">Оставить предложение</div>
                <div @click="deleteOrder" v-show="this.type == 'customer'">Удалить заказ</div>
            </div>

        </div>
        <div class="description">{{ order.description }}</div>
        <div class="info">
            <div class="material">Материал: {{ order.materials }}</div>
            <div class="count">
                <div class="text">Количество:</div>
                <div class="counter">{{ order.quantity }}</div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
    export default {
        props: {
            order: {
                type: Object,
            }
        },
        data() {
            return {
                customer: String,
                type: localStorage.type
            }
        },
        methods: {
            async getCustomer() {
                const response = await axios.get('http://127.0.0.1:8000/customers/' + this.order.customer_id);
                this.customer = response.data.name;
            },
            letOffer() {
                this.$emit('openDialog', true)
            },
            async deleteOrder() {
                const response = await axios.delete('http://127.0.0.1:8000/orders/'+ this.order.order_id);
            this.$router.back();
                
            }
        },
        mounted() {
        },
        watch: {
            order(order) {
                this.getCustomer();
            }
        }
        
    }
</script>

<style scoped>
.order {
    padding: 32px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    margin: 16px auto;
    width: calc(100% - 30px);
    background: #458686;
    height: 240px;
    border-radius: 30px;
    transition-duration: 0.5s;
}
.title {
    display: flex;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 30px;
    line-height: 36px;

    color: #F5F5F5;;
}
.name {
    flex: 1;
}
.arrow {
    display: flex;
    justify-content: end;
    flex: 1;
}
.info {
    display: flex;
    justify-content: flex-start;
}
.description {
    word-wrap: break-word;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 25px;
    line-height: 30px;
    text-align: justify;

    color: #CCCCCC;
}
.material {
    flex: 1;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 30px;
    line-height: 36px;


    color: #F5F5F5;;
}
.count {
    flex: 1;
    justify-content: end;
    display: flex;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 30px;
    line-height: 36px;
    text-align: center;

    color: #F5F5F5;;
}
.counter {
    margin: 0 0 0 15px;
}
.arrow_img {
    background: url('@/resources/images/arrow.svg') no-repeat;
    width: 55px;
}
.btn {
    background:#DF7373;
    padding: 10px;
    border-radius: 12px;
    cursor: default;
    transition-duration: 0.5s;
}
.btn:active {
    background: #F5F5F5;
    color: #DF7373;
}
</style>