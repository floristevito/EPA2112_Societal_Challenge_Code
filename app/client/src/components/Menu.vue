<template>
  <div id="nav" class="pb-5">
    <div id="nav1" class="row no-gutters fixed-top">
        <div id="menu1" class="col-md-1 col-lg-2"></div>
        <div id="menu2" class="col-md-10 col-lg-8">
            <b-navbar toggleable="md" class="ml-auto" type="light" variant="secondary">
                <b-navbar-nav class="mr-auto">
                    <b-navbar-brand to="/" left>
                        <img class="logo" src="../assets/qr.png" width="40em" ><img>
                        <h1 class="logoText">Challenges.Social</h1>
                    </b-navbar-brand>
                     <!--
                    <b-navbar-brand to="/" left>
                        <img src="../assets/tudelft.jpeg" width="50em" ><img>
                    </b-navbar-brand> -->
                </b-navbar-nav>
                
                <b-navbar-nav  class="ml-auto">
                    <b-collapse id="navbar-toggle-collapse" is-nav>
                        <b-nav-item to="/">Home</b-nav-item>
                        <b-nav-item to="/concept">Ons concept</b-nav-item>
                        <b-nav-item to="/form">Jouw mening</b-nav-item>
                        <b-nav-item to="/contact">Contact</b-nav-item>
                    </b-collapse>
                </b-navbar-nav>

                <b-navbar-nav class="ml-auto mb-auto">
                    <b-navbar-toggle class="justify-content-top" target="navbar-toggle-collapse">
                        <template #default="{ expanded }">
                        <b-icon v-if="expanded" icon="list" rotate = "-90"></b-icon>
                        <b-icon v-else icon="list" align = "top"></b-icon>
                        </template>
                    </b-navbar-toggle>
                </b-navbar-nav>
            </b-navbar>
        </div>
        <div id="menu3" class="col-md-1 col-lg-2"></div>
    </div>
  </div>
</template>

<script>
export default {
}

</script>

<style scoped>
#nav1 {
    border-bottom: 0.1vh inset rgb(212, 212, 212); 
}

#menu1, #menu3 {
    background-color: white;
}

.logo {
    float: left;
}

.logoText {
    font-size: 1.5em;
    float: left;
    margin-left: 0.2em;
}
</style>