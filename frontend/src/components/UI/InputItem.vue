<template>
    <input :value="modelValue" @input="updateInput" class="input" type="text"/>
</template>

<script>
    export default {
        name: 'input-item',
        props: {
            modelValue: [String, Number]
        },
        methods: {
            updateInput(event) {
                this.$emit('update:modelValue', event.target.value)
            }
        },
    }
</script>

<style scoped>
.input {
    height: 46px;
    width: 100%;
    background: #3F4155;
    border-radius: 10px;
    margin: 16px 0;
    padding: 10px 16px;
    color: #FAF6ED;
    font-size: 24px;

}
.input::placeholder {
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 24px;
    line-height: 29px;

    color: #FAF6ED;
}

</style>