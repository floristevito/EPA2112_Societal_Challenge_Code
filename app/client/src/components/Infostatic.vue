<template>
<div id="base">
  <div id="info" class="jumbotron text-center">
  <h1 class="display-4">{{ title }}</h1>
  <div class="row no-gutters">
  <div class="col-1 col-sm-2"></div>
  <div class="col-10 col-sm-8">
      <p class="lead">{{ content }}</p>
  </div>
  <div class="col-1 col-sm-2"></div>
  </div>
</div>


</div>
</template>

<script>
export default {
name: 'Infostatic',
components: {},
props: {
  title: {
    type: String
  },
  content: {
    type: String
  }
}
}
</script>

<style>

</style>