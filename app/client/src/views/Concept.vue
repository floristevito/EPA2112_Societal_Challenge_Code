<template>
  <div id="concept">     
      <Infostatic title="Ons concept" content="         
            Met behulp van QR-posters verzamelen wij data voor de Wijkagenda’s in Den Haag.
            De Wijkagenda is bedoeld voor inwoners om hun eigen wijk te kunnen verbeteren. 
            Het is een goed instrument om input te krijgen, maar schiet tekort in het bereiken van jongeren.
            Door een vragenlijst in de publieke ruimte aan te bieden met behulp van QR-codes, 
            hopen wij meer jongeren te bereiken.
            "
            color="primary">
      </Infostatic>

      <div class="row no-gutters text-center">
      <div class="col-1 col-sm-2"></div>
      <div class="col-10 col-sm-8">
        <h1 class="display-4">Hoe het werkt</h1>
        <img :src="require('../assets/steps.png')" height="250em" fluid alt="Responsive image">
      </div>
      <div class="col-1 col-sm-2"></div>      
    </div>

    <Infostatic title="Verbindend" content="         
            Ons intiatief is een poging om beleidsmakers en burgers elkaar beter te leren begrijpen. 
            "  color="primary">
      </Infostatic>
      
  </div>
</template>

<script>
import Infostatic from '../components/Infostatic.vue'
export default {
  name: 'Concept',
  components: {
  Infostatic
  }
}
</script>

<style>
</style>