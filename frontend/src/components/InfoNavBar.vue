<template>
    <div class="navbar">
        <div class="items">
            <h1 class="icon">БСМ</h1>
            <div class="navbar__btns">
                <a class="nav__link" href="#about">О нас</a>
                <a class="nav__link" href="#service">Для кого</a>
                <a class="nav__link" href="#customers">Заказчикам</a>
                <a class="nav__link" href="#providers">Поставщикам</a>
                <a class="nav__link" @click="openEntry">Вход</a>
                <registration-button @click="openRegistration">Регистрация</registration-button>
            </div>
        </div>
        <div class="divider"></div>
    </div>

</template>

<script>
    export default {
        methods: {
            openRegistration() {
                this.$emit('registration', true)
            },
            openEntry() {
                this.$emit('entry', true)
            }
        },
    }
  
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@100;400;700&display=swap');
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