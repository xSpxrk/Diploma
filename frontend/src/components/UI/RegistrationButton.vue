<template>
    <button class="btn">
        <slot></slot>
    </button>
</template>

<script>
    export default {
        name: 'registration-button'
    }
</script>

<style scoped>
.btn {
    padding: 10px 15px;
    border: 1px solid #5cb25d;
    border-radius: 12px;
    background-color: #faf6ed;
    transition-duration: 0.5s;

}
.btn:hover {
    background-color: #5cb25d;
    color: #faf6ed;
}
</style>