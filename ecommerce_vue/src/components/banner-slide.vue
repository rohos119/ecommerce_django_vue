<template>
  <div id="banners">
    <carousel :perPage="1" 
              :autoplay="true" 
              :navigationEnabled="true" 
              :paginationPadding="3">
      <slide v-for="bannerItem of bannerItems" :key="bannerItem.imgUrl" class="slide item" id="slides" >
        <a :href="bannerItem.linkUrl" target="_blank"><img :src="bannerItem.imgUrl" class="landscape"></a>
      </slide>  
    </carousel>
    </div>
</template>

<script>
  export default{
    name : 'banner-slide',
    data(){
      return{
        bannerItems:[
          { 'brand' : 'FashionFull',
            'date' : 20220317,
            'imgUrl':'https://fashion-full.com/web/upload/category/editor/2022/03/14/08eb342735b8442bafe35e62d6a5ac57.jpg',
            'linkUrl' : 'https://fashion-full.com/product/detail.html?product_no=27709&cate_no=147&display_group=1'
          },
          { 
            'brand' : 'SPAO',
            'date' : 20220317,
            'imgUrl':'https://spao.com/web/upload/NNEditor/20220224/a445837eb19bfcd614000d1e6ecdb170.jpg',
            'linkUrl' : 'https://spao.com/product/project.html?cate_no=2214'
          },
          {
            'brand' : 'SPAO',
            'date' : 20220317,
            'imgUrl' : 'https://spao.com/web/upload/NNEditor/20220315/c53a0310a2599ec64b69e8d3bbe56bb3.jpg',
            'linkUrl' :  'https://spao.com/product/project.html?cate_no=1869'
          },
          {
            'brand' : 'forever21',
            'date' : 20220317,
            'imgUrl' : 'https://www.forever21.com/dw/image/v2/BFKH_PRD/on/demandware.static/-/Library-Sites-RefArchSharedLibrary/default/dw9fc7c203/Homepage/2022/BMSM_D_M.jpg',
            'linkUrl' : 'https://www.forever21.com/us/shop/catalog/category/f21/women-new-arrivals-clothing'
          } 
        ],
      }
    },
  } 
</script>
<style lang="sass">

#banners
  padding : 0 30px
  margin-bottom : 10%

.VueCarousel
  height : inherit

.VueCarousel-wrapper
  height : inherit

.VueCarousel-inner
  height : inherit

img.landscape
    height: 100%

</style>