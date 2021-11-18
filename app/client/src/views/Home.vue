<template>
  <div id="home">
    <Info></Info>
    <Infostatic title="Welkom op de home pagina van het Challanges.Social project"
    content="Middels de inzet van QR codes hopen wij jongeren te bereiken in Den Haag."
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