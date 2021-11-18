<template>
  <div id="home">
    <Info></Info>
    <Infostatic title="Wat wij doen"
    content="Met behulp van QR-codes proberen wij jongeren te betrekken bij het verbeteren van hun leefomgeving."
    color="secondary"
    ></Infostatic>
    <div class="row no-gutters text-center">
      <div class="col-1 col-sm-2"></div>
      <div class="col-10 col-sm-8">
        <img class="animation" loading="lazy" src="../assets/qr_gif.gif" alt="responsive image" title="uitleg" width="300vw">
      </div>
      <div class="col-1 col-sm-2"></div>      
    </div>
  </div>
</template>

<script>
import Info from '../components/Info.vue'
import Infostatic from '../components/Infostatic.vue'

export default {
  name: 'Home',
  components: {
    Info,
    Infostatic
  },
}
</script>

<style scoped>


</style>