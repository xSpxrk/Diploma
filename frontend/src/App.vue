<template>
  <div class="app">
    <router-view></router-view>
    </div>
</template>

<script>

  export default {

    data() {
      return {
        dialogVisible: false
      }
    },
  }
</script>

<style>
@import "@/assets/css/reset.css";


* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;


}
.app {
  background-color: #faf6ed;
  margin: 0;
  padding: 0;

}



</style>