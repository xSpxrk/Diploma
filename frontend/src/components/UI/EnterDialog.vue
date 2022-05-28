<template>
    <div class="entry">
        <h1 class="header">Авторизация</h1>
        <input-item placeholder="Почта"/>
        <input-item placeholder="Пароль" type="password"/>
        <div class="button">
            <button-dialog class="btn">Вход</button-dialog>
        </div>


    </div>
</template>

<script>
import InputItem from './InputItem.vue'
    export default {
  components: { InputItem },
        
    }
</script>

<style scoped>
.entry {
    padding: 32px 100px;
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
   padding: 8px 100px; 
}
</style>