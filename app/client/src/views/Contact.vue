<template>
  <div id="contact_info">
    <Infostatic title="Contact" content="Voor vragen over ons project kunt u ons via de mail bereiken:
     youth.social.challenge@hotmail.com"></Infostatic>

     <Infostatic title="Wie zijn wij?" content="Challeges.Social is een initiatief dat tot stand is gekomen
     door een samenwerking tussen de TU Delft en gemeente Den Haag. Het platform is opgezet door studenten, 
     en is een pilot om burgerparticipatie te verbeteren." color="secondary"></Infostatic>
  </div>
</template>

<script>
import Infostatic from '../components/Infostatic.vue'

export default {
name: 'Contact',
components: { 
  Infostatic
}
}
</script>

<style>

</style>