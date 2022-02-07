<template>
  <div id="wrapper">
    <nav class="navbar">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Fashion Mall</strong></router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu" >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active':showMobileMenu}">
        <div class="navbar-start">
          <router-link to="/Man" class="navbar-item">Man</router-link>
          <router-link to="/Women" class="navbar-item">Women</router-link> 
        </div>
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light">Login</router-link>
              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span><span>Cart</span>
              </router-link>
            </div>
          </div>
        </div>     
      </div>
      
    </nav>
    <section class="section">
      <router-view/>
    </section>
    <footer class="footer">
      <p>Copyright (c) 2022</p>
    </footer>
  </div>
</template>
<script>
  export default{
    data(){
      return{
        //hambuger menu display trigger 
        showMobileMenu: false,
        }
    }
  }
</script>
<style lang="scss">
@import '../node_modules/bulma';


</style>
