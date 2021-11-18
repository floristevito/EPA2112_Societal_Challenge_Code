<template>
<div class="base">
    <div  id ="footer" class="row no-gutters pt-5 pb-5">
                    <div class="col-0 col-lg-2"></div>
                    <div class="row no-gutters col-12 col-lg-8">
                            
                            <div class="col-12 col-md-4">
                                <div class="row no-gutters">
                                    <div class="col-1 col-md-0"></div>
                                    <div class= "col-10 col-md-12 text-center" id="subfooter1">
                                        <div class="row no-gutters">
                                            <div class="col-2"></div>
                                            <div class="onsLogo col-8">
                                                <img class="qr" src="../assets/qr.png" width="40em" ><img>
                                                <h1 class="logoText">Challenges.Social</h1>
                                            </div>
                                            <div class="col-2"></div>
                                        </div>
                                        <div class="row mt-5"></div>
                                       
                                        
                                    </div>
                                    <div class="col-1 col-md-0"></div>
                                </div>
                            </div>

                            <div class="col-12 col-md-4">
                                <div class="row no-gutters">
                                    <div class="col-1 col-md-0"></div>
                                    <div class= "col-10 col-md-12 text-center" id = "subfooter2">
                                    <h1>Partners</h1>
                                     <div class="row no-gutters">
                                            <div class="collab col-12">
                                                <a href="https://www.denhaag.nl"><img class="denhaag" src="../assets/logo.svg" width="200em" ><img></a>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-1 col-md-0"></div>
                                </div>
                            </div>

                            <div class="col-12 col-md-4">
                                <div class="row no-gutters">
                                    <div class="col-1 col-md-0"></div>
                                    <div class= "col-10 col-md-12 text-center" id = "subfooter3">
                                    <h1>Vragen?</h1>
                                    <li class = "footer_li"><a href="/#/contact/">Contact</a></li>
                                    <li class = "footer_li"><a href="/#/concept/">Wat we doen</a></li>
                                    </div>
                                    <div class="col-1 col-md-0"></div>
                                </div>
                            </div>
                        </div>
                        <div class="col-0 col-lg-2"></div>
                    </div>
                    
</div>

</template>

<script>
export default {

}
</script>

<style scoped>
#footer{
    background-color: white;
    
}

h1 {
    color: black;
    font-size: 1.5em;
}

a {
    color: black;
}

.footer_li {
    list-style-type: none;
    margin: 0.5em;
}

.qr {
    float: left;
}


.logoText {
    float: left;
    margin-left: 0.4em;
    margin-top: 0.1em;
    font-size: 1.4em;
}
</style>