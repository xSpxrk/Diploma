<template>
    <div class="main">
        <customer-nav-bar v-show="this.type == 'customer'"></customer-nav-bar>
                <provider-nav-bar v-show="this.type == 'provider'"></provider-nav-bar>
        <div class="background">
            <h1 class="title">Профиль</h1>
            <div class="inner">
                <div class="items">
                    <h1 class="text">Наименование</h1>
                    <input-item class="input" v-model="user.name"></input-item>
                    <h1 class="text" >Почта</h1>
                    <input-item class="input" v-model="user.email" readonly></input-item>
                    <h1 class="text">Телефон</h1>
                    <input-item class="input" v-model="user.phone_number"></input-item>
                    <h1 class="text">Новый пароль</h1>
                    <input-item class="input" v-model="this.password" type="password"></input-item>
                    <div class="button">
                        <div class="btn" @click="updateUser">Сохранить</div>
                    </div>
                </div>
                
            </div>
        </div>
    </div>
</template>

<script>
import ProviderNavBar from '@/components/ProviderNavBar.vue'
import CustomerNavBar from '@/components/CustomerNavBar.vue'
import axios from 'axios'
    export default {
        components: {
            CustomerNavBar,
            ProviderNavBar
        },
        data() {
            return {
                type: localStorage.type,
                user: Object,
                password: ''
            }


        },
        methods: {
            async getUser() {
                const response = await axios.get('https://bsm-backend.herokuapp.com/users/', {
                    params: {
                        token: localStorage.token,
                    }
                });
                this.user = response.data;
            },
            async updateUser(){
                const response = await axios.put('https://bsm-backend.herokuapp.com/users/', {
                    name:  this.user.name,
                    email:  this.user.email,
                    phone_number:  this.user.phone_number,
                    password: this.password

                }, {
                    params: {
                        token: localStorage.token,
                    }

                });
                alert('Данные успешно изменены');
                this.getUser();
            }
        },
        mounted() {
            this.getUser();
        },
        
    }
</script>

<style scoped>
.main {
    width: 100%;
    height: 100%;
}
.background {
    background: url("@/resources/images/profile_rectangle.svg") no-repeat;
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
.inner{
    padding: 20px 0;
    margin: 0 auto;
    width: 1440px;
    height: 100%;
    align-items: center;
    display: flex;
    flex-direction: column;
}
.items {
    width: calc(100% - 50%);
}
.input {
    background: #FFFFFF;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 25px;
    line-height: 48px;

    color: #3F4155;
}
.text {
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 25px;
    color: #FFFFFF;
    }
.button {
    width: 100%;
    display: flex;
    justify-content: flex-end;
}
.btn {
    padding: 15px 60px;
    background: #458686;
    border-radius: 10px;

    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 24px;
    line-height: 29px;
    border: none;
    text-align: center;
    transition-duration: 0.2s;
    color: #FFFFFF;
    border-radius: 20px;
}
.btn:active {
    background: #3F4155;
}
</style>