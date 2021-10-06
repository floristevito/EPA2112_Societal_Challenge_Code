<template>
  <div id="home">
    <Info></Info>
    <conceptinfo></conceptinfo>
  </div>
</template>

<script>
import Info from '../components/Info.vue'
import Conceptinfo from '../components/Conceptinfo.vue'

export default {
  name: 'Home',
  components: {
    Info,
    Conceptinfo
  },
}
</script>

<style>

</style>