<template>
    <div class="registration">
        <h1 class="header">Начните работать с нами</h1>
        <select v-model="user.type" class="type">
            <option disabled value="" class="option">Выберите</option>
            <option class="option">Заказчик</option>
            <option class="option">Поставщик</option>
        </select>
        <input-item placeholder="Наименование" v-model="user.name"/>
        <input-item placeholder="Почта" type="email" v-model="user.email"/>
        <input-item placeholder="Номер телефона" inputmode="tel" v-model="user.phone"/>
        <input-item placeholder="Пароль" type="password" v-model="user.password"/>
        <input-item placeholder="Повтор пароля" type="password" v-model="user.repeated_password"/>
        <div class="button">
            <button-dialog class="btn" @click="register">Начать работу</button-dialog>
        </div>


    </div>
</template>

<script>
import InputItem from '@/components/UI/InputItem.vue'
    export default {
        components: { InputItem },
        data() {
            return {
                user: {
                    type: '',
                    name: '',
                    email: '',
                    phone: '',
                    password: '',
                    repeated_password: ''
                }
            }
        },
        methods: {
            register() {
                if (this.user.type != '' && this.user.name != '' && this.user.email != '' && this.user.phone != '' && this.user.password != '' && this.user.repeated_password != '') {
                    if (this.user.repeated_password == this.user.password) {
                        this.$emit('register', this.user),
                        this.user = {
                            type: '',
                            name: '',
                            email: '',
                            phone: '',
                            password: '',
                            repeated_password: ''
                        }
                    } else {
                        alert("Пароли не совпадают")
                    }
                } else {
                    alert("Заполните все поля")
                }
                
            }
        },
        
    }
</script>

<style scoped>
.registration {
    padding: 32px 230px;
}
.header {
    text-align: center;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 40px;
    line-height: 48px;
    margin: 0 0 18px 0;
    color: #3F4155;
}
.button {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: end;
}
.btn {
    padding: 8px 40px;
}
.type {
    padding: 8px 16px;
    height: 46px;
    width: 100%;
    background: #D9D9D9;
    border-radius: 10px;
    
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 24px;
    line-height: 29px;
    color: #3F4155;
}
</style>