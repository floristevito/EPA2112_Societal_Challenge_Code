<template>
  <div id="home">
    <Info></Info>
    <Infostatic title="Wat wij doen"
    content="Met behulp van QR-codes proberen wij jongeren te betrekken bij het verbeteren van hun leefomgeving."
    color="secondary"
    ></Infostatic>
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

<style>

</style>