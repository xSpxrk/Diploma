<template>
    <div class="navbar">
        <dialog-window v-model:show="visible">
            <create-order-dialog @order="create"></create-order-dialog>
        </dialog-window>
        <div class="items">
            <router-link class="icon" to="/main">БСМ</router-link>
            <div class="navbar__btns">
            <router-link class="nav__link" to="/my_orders">Мои заказы</router-link>
            <router-link class="nav__link" to="/profile">Профиль</router-link>
            <a class="nav__link" @click="exit">Выход</a>
            <registration-button @click="openWindow">Создать заказ</registration-button>
            </div>
        </div>
        <div class="divider"></div>
    </div>

</template>

<script>
import CreateOrderDialog from '@/components/CreateOrderDialog.vue'
import axios from 'axios'
    export default {
        components: {
            CreateOrderDialog
        },
        data() {
            return {
                visible: false,
                order: Object
            }
        },
        methods: {
            exit() {
                localStorage.token = ''
                localStorage.type = ''
                this.$router.push('/')
            },
            openWindow(){
                this.visible = true;
            },
             async create(order) {
                const response = await axios.post('http://127.0.0.1:8000/orders/', {
                    name: order.name,
                    description: order.description,
                    materials: order.materials,
                    quantity: parseInt(order.quantity)
                },
                {
                    params: {
                        token: localStorage.token
                    }
                });
                this.order = response.data;
                this.visible = false;
            },
            

        },
    }
  
</script>

<style scoped>
.navbar {
    margin: 0 auto;
    padding-top: 28px;
    width: 1440px;
    background-color: #faf6ed;
    align-items: center;
    height: 86px;
}
.icon {
    color: #5cb25d;
    font-size: 40px;
    font-family: 'Roboto Slab', serif;
    font-weight: 400;
    text-decoration: none;
    cursor: default;

}
.divider {
    margin-top: 2px;
    height: 1px;
    background: gray;
}
.navbar__btns {
    margin-left: auto;
    font-size: 15px;
    font-family: 'Roboto Slab', serif;
    font-weight: 400;
    color: black;
}
.nav__link {
    text-decoration: none;
    margin-right: 15px;
    cursor: default;
    transition-duration: 0.2s;
}
.nav__link:visited {
    color: black;
}

.nav__link:hover {
    color: #5cb25d;
}
.items {
    background-color: #faf6ed;
    display: flex;
    align-items: center;
}

</style>