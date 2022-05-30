<template>
  <div class="app">
    <router-view></router-view>
    </div>
</template>

<script>

  export default {
    data() {
      return {
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
  scroll-behavior: smooth;

}
.app {
  background-color: #faf6ed;
}
body {
    background-color: #faf6ed;
}


</style>