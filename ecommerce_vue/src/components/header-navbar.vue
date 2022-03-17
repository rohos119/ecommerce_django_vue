<template>
    <div id="header">
     <nav class="navbar">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item is-size-3" id="navbarlogo"><strong>SPACOM</strong></router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" @click="showMobileMenu = !showMobileMenu" >
          <span id="burgerline" aria-hidden="true"></span>
          <span id="burgerline" aria-hidden="true"></span>
          <span id="burgerline" aria-hidden="true"></span>
        </a>
      </div>
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active':showMobileMenu}">
        <div class="navbar-start" id="navbar-start">
          <div class="navbar-item has-dropdown is-hoverable">
            <router-link to="/man" class="navbar-item">MAN</router-link>
            <div class="navbar-dropdown">
              <router-link to="/mantop" class="dropdown-item">Top</router-link>
              <router-link to="/manbottom" class="dropdown-item">Bottom</router-link>
              <router-link to="/manouter" class="dropdown-item">Outer</router-link>
              <router-link to="/manshoes" class="dropdown-item">Shoes</router-link>
              <router-link to="/manbag" class="dropdown-item">Bag</router-link>
              <router-link to="/manmyfit" class="dropdown-item">My fit</router-link>
            </div>
          </div>
          <div class="navbar-item has-dropdown is-hoverable">
            <router-link to="/women" class="navbar-item">WOMEN</router-link>
            <div class="navbar-dropdown">
              <router-link to="/womentop" class="dropdown-item">Top</router-link>
              <router-link to="/womenbottom" class="dropdown-item">Bottom</router-link>
              <router-link to="/womenouter" class="dropdown-item">Outer</router-link>
              <router-link to="/womenshoes" class="dropdown-item">Shoes</router-link>
              <router-link to="/womenbag" class="dropdown-item">Bag</router-link>
              <router-link to="/womenmyfit" class="dropdown-item">My fit</router-link>
            </div>
          </div>
        </div>
        <div class="navbar-end">
          <router-link to="/login" class="navbar-item" >LOGIN</router-link>
            <!-- mdoal로 로그인페이지 구성  -->
          <router-link to="/join" class="navbar-item" >JOIN</router-link> 
          <div class="navbar-item has-dropdown is-hoverable">
            <router-link to="/mypage" class="navbar-item" >MYPAGE</router-link>
            <div class="navbar-dropdown">
              <router-link to="/mypage/order" class="dropdown-item">주문내역조회</router-link>
              <router-link to="/mypage/whishlist" class="dropdown-item">관심상품</router-link>
              <router-link to="/mypage/point" class="dropdown-item">적립금내역</router-link>
              <router-link to="/mypage/coupon" class="dropdown-item">쿠폰내역조회</router-link>
              <router-link to="/mypage/address" class="dropdown-item">배송지주소관리</router-link>
              <router-link to="/mypage/latest" class="dropdown-item">최근본상품</router-link>
            </div> 
          </div>
          <div class="navbar-item has-dropdown is-hoverable">
            <router-link to="/board" class="navbar-item" >BOARD</router-link>
            <div class="navbar-dropdown">
              <router-link to="/board/notice" class="dropdown-item">Notice</router-link>
              <router-link to="/board/faq" class="dropdown-item">FAQ</router-link>
              <router-link to="/board/prdinqury" class="dropdown-item">상품문의</router-link>
              <router-link to="/board/delivery" class="dropdown-item">배송문의</router-link>
              <router-link to="/board/exchange" class="dropdown-item">교환/반품</router-link>
              <router-link to="/board/event" class="dropdown-item">Event</router-link>
            </div> 
          </div>
          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons" id="search-bar">
                <div class="control" id="search-input">
                  <input type="text" class="input is-small" placeholder="keyword" name="query">
                  <!-- <i class="fa fa-search" id="search-icon" @click="searchproduct()"></i> -->
                  <button id="search-icon" class="button is-small" @click="searchProduct()">
                    <span class="icon"><i class="fa fa-search" ></i></span>
                  </button>
                </div>
              </div>
            </form>
          </div>
          <p class="buttons">
            <button class="button"><span class="icon is-big"><i class="fa fa-shopping-cart"></i></span></button>
             <button class="button"><span class="icon is-big"><i class="fa fa-heart"></i></span></button>
          </p>
        </div>
      </div>  
      </nav>
    </div>      
</template>
<script>
  export default{
    name : 'haeder-navbar',
    data(){
      return{
        //hambuger menu display trigger 
        showMobileMenu: false,
      }
    },
    methods :{
      searchProduct(){

      },
    }
  }
</script>

<style lang="sass">
@import '../../node_modules/bulma/bulma.sass'
@import url('https://fonts.googleapis.com/css2?family=Shadows+Into+Light&display=swap')
@import url('https://fonts.googleapis.com/css2?family=Advent+Pro:wght@300&display=swap')
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100&display=swap')

.navbar
  background-color : #437299
  
.navbar-item
  color : #fff
  
.navbar-brand  
  font-size : 1.3em,
  &:hover
    background-color: #437299

.navbar-start  
  font-size : 0.9em
  font-family: 'Advent Pro', 'Noto Sans KR', sans-serif

.navbar-end
  font-size : 0.7em
  padding-right : 2px
  padding-left : 2px
  font-family: 'Advent Pro', 'Noto Sans KR', sans-serif

.icon
  color : white

p
  .button 
    background-color : #437299
    border-color : #437299 

#burgerline
  color : white

#search-bar
  position: relateive
  height : inherit
  width: 150px
  -webkit-transform: skewX(-15deg)
  transform: skewX(-15deg)

#search-input
  position: absoulte
  padding-right: 30px
  height: inherit

#search-icon
  color : gray
  position: absolute
  top: 0
  right: 0
  width: 30px
  height: inherit
  cursor: pointer
  border-color : white
  border-radius : 0px

#search-icon span
  color : gray  

#navbarlogo
  font-family: 'Shadows Into Light', cursive
  

</style>
