<template>
    <div class="offer">
        <div class="title">
            <div class="name_price">
                <div class="name">{{ this.order.name }}</div>
                <div class="price">
                    <div class="number">{{ offer.price }}</div>
                    <div class="rubles">руб.</div>
                </div>
            </div>

            <div class="arrow">
                <div class="arrow_img" @click="$router.push(`/order/${offer.order_id}`)"></div>
            </div>

        </div>
            <div class="material">Материал: {{ this.order.materials }}</div>
        <div class="info">
            <div class="customer">Заказчик: {{ this.customer }}</div>
            <div class="count">
                <div class="text">Количество:</div>
                <div class="counter">{{ offer.quantity }}</div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
    export default {
        props: {
            offer: {
                type: Object
            }
        },
        data() {
            return {
                order: Object,
                customer: String
            }
        },
        methods: {
            async getOrder() {
                const response = await axios.get('https://bsm-backend.herokuapp.com/orders/' + this.offer.order_id);
                this.order = response.data;
                return response.data
            },
            async getCustomer() {
                const customer = await this.getOrder();
                const response = await axios.get('https://bsm-backend.herokuapp.com/customers/' + customer.customer_id);
                this.customer = response.data.name;
            }

        },
        mounted() {
            this.getCustomer();
        },
    }
</script>

<style scoped>
.offer {
    padding: 32px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    margin: 16px 0;
    width: calc(100% - 30px);
    background: #FAF6ED;
    height: 240px;
    border-radius: 30px;
    transition-duration: 0.5s;
}
.offer:hover{
    transform: translate(10px, 0);
}
.title {
    display: flex;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 30px;
    line-height: 36px;

    color: #3F4155;
}
.name_price {
    display: flex;
}
.price {
    margin: 0 0 0 32px;
    display: flex;
    color: #6E7080;
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

    color: #6E7080;
}
.material {
    display: flex;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 30px;
    line-height: 36px;

    color: #3F4155;
}
.customer {
    flex: 1;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 30px;
    line-height: 36px;
    color: #3F4155;
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

    color: #3F4155;
}
.counter {
    margin: 0 0 0 15px;
}
.arrow_img {
    background: url('@/resources/images/arrow.svg') no-repeat;
    width: 55px;
}
.rubles {
    margin: 0 0 0 8px;
}

@keyframes donut-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.donut {
  display: inline-block;
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-left-color: #7983ff;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: donut-spin 1.2s linear infinite;
}
</style>