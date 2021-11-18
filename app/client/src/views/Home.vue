<template>
  <div id="home">
    <Info></Info>
    <HomePage></HomePage>
  </div>
</template>

<script>
import Info from '../components/Info.vue'
import HomePage from '../components/HomePage.vue'

export default {
  name: 'Home',
  components: {
    Info,
    HomePage
  },
}
</script>

<style>

</style>