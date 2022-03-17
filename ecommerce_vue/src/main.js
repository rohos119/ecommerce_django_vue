import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import HeaderNavbar from './components/header-navbar'
import BannerSlide from './components/banner-slide'
import CardProduct from './components/card-product.vue'

import VueCarousel from 'vue-carousel'

Vue.config.productionTip = false

Vue.use(VueCarousel)
Vue.component(HeaderNavbar.name, HeaderNavbar)
Vue.component(BannerSlide.name, BannerSlide)
Vue.component(CardProduct.name, CardProduct)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
