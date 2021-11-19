<template>
<div id="your_opinion">
  <Infostatic title="Laat ons weten wat je van deze plek vindt!" content="
    Welkom! We willen je graag een aantal vragen stellen over de plek waar je jouw QR code hebt gescanned. 
    Met jouw bijdrage helpt u de gemeente Den Haag om deze plek te verbeteren."
    color="primary"></Infostatic>


    <div class="row no-gutters">
        <div id="empty1" class="col-2 col-xxl-1"></div>
        <div id="content" class="col-8 col-xxl-10">
            <Datacollector></Datacollector>
            <div class="row mt-5"></div>
        </div>
        <div id="empty2" class="col-2 col-xxl-1"></div>
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