<template>
  <el-carousel height="720px" :interval="3000" arrow="always">
    <el-carousel-item :key='index' v-for="(banner, index) in banner_list">
      <a :href="banner.link"><img :src='banner.image_url' alt=""></a>
    </el-carousel-item>
  </el-carousel>
</template>

<script>
    export default {
        name: "Banner",
        data(){
          return{
            banner_list:[]
          }
        },
        created() {
          this.get_banner_list();
        },
        methods:{
          //获取轮播图列表
          get_banner_list(){
            this.$axios.get(this.$settings.Host+'/banner/', {}).then(response=>{
            console.log(response.data);
            this.banner_list = response.data;
          }).catch(error=>{
            console.log(error.response)
          })
          }

        }
    }
</script>

<style scoped>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>

