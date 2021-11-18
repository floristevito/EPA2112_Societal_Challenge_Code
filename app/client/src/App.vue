<template>
  <div id="app">
    <Menu></Menu>
    <!-- <div class="row no-gutters mb-5"></div> -->
    <div class="row no-gutters mb-3"></div>
    <Router></Router>
    <Footer></Footer>
  </div>
</template>

<script>
import Router from './components/Router.vue'
import Menu from './components/Menu.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    Router,
    Menu, 
    Footer
  },
}
</script>

<style>
@import url(
"https://fonts.googleapis.com/css?family=Lato:100,100italic,300,300italic,regular,italic,700,700italic,900,900italic&subset=latin,latin-ext&display=swap"
);

#app {
  font-family: 'Lato', sans-serif !important;

}
</style>
