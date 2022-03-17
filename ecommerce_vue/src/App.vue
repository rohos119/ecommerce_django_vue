<template>
  <div id="main">
    <div id="wrap">
      <header-navbar></header-navbar>
    </div>
    <div id="container">
      <div id="contents">
        <banner-slide></banner-slide>
        <div id="bestPrd"> 
          <div class="block" id="title">
            <h3> BEST ITEM</h3>
            <hr>
          </div>
          <div class="columns is-multiline">
            <card-product></card-product>
            <card-product></card-product>
            <card-product></card-product>
            <card-product></card-product>
            <card-product></card-product>
            <card-product></card-product>
            <card-product></card-product>
            <card-product></card-product>
          </div>
        </div>
      </div>
    </div>
  </div>
    
</template>
<script>
import headerNavbar from './components/header-navbar.vue'
import bannerSlide from './components/banner-slide.vue'
import cardProduct from './components/card-product.vue'

  export default{
  components: { 
    headerNavbar,
    bannerSlide,
    cardProduct
  },
    data(){
      return{
      }
    },
  } 
</script>

<style lang="sass">
#wrap
  display : block
  
#bestprd
  margin-left : 10%
  margin-right : 10%
  
.block
  text-align : center
</style>
