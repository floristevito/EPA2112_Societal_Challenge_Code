<template>
<div id="your_opinion">
  <Infostatic title="Your opinion!" content="Heeft u vragen over ons concept, of iets anders? 
    U kunt ons altijd bereiken via email. 
    Bereik ons via: b.hermans@student.tudelft.nl"></Infostatic>


    <div class="row no-gutters">
        <div id="empty1" class="col-1 col-xxl-1"></div>
        <div id="content" class="col-10 col-xxl-10">
            <Datacollector></Datacollector>
        </div>
        <div id="empty2" class="col-1 col-xxl-1"></div>
    </div>
</div>
</template>

<script>
import Infostatic from '../components/Infostatic'
import Datacollector from '../components/Datacollector'

export default {
    name: 'Form',
    components: {
        Infostatic,
        Datacollector
    }
}
</script>

<style>

</style>