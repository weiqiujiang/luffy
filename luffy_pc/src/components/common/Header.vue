<template>
    <div class="header-box">
      <div class="header">
        <div class="content">
          <div class="logo full-left">
            <router-link to="/"><img src="/static/image/logo.svg" alt=""></router-link>
          </div>
          <ul class="nav full-left">
              <li v-for="nav in nav_list">
                <span v-if="nav.is_site"><a :href="nav.link">{{nav.title}}</a></span>
                <span v-else><router-link :to="nav.link">{{nav.title}}</router-link></span>
              </li>
          </ul>

          <div v-if="token" class="login-bar full-right">
            <div class="shop-cart full-left flex-item">
              <span class="shop-cart-total">0</span>
              <img src="/static/image/cart.svg" alt="">
              <span><router-link to="/cart">购物车</router-link></span>
            </div>
<!--            <div class="login-box full-left">-->
              <router-link to="">学习中心</router-link>
            <el-avatar style="margin: 0 10px" src="/static/image/member.png"></el-avatar>
              <el-menu width="200" class="member el-menu-demo" mode="horizontal">
                  <el-submenu index="2">
                    <el-menu-item index="2-1">我的账户</el-menu-item>
                    <el-menu-item index="2-2">我的订单</el-menu-item>
                    <el-menu-item index="2-3">我的优惠卷</el-menu-item>
                    <el-menu-item index="2-3"><span @click="logoutHander">退出登录</span></el-menu-item>
                  </el-submenu>
                </el-menu>
<!--            </div>-->
          </div>

          <div v-else class="login-bar full-right">
            <div class="shop-cart full-left flex-item">
              <img src="/static/image/cart.svg" alt="">
              <span><router-link to="/cart">购物车</router-link></span>
            </div>
            <div class="login-box full-left flex-item">
              <router-link to="/user/login">登录</router-link>
              &nbsp;|&nbsp;
              <span>注册</span>
            </div>
          </div>

        </div>
      </div>
    </div>
</template>

<script>
    export default {
      name: "Header",
      data(){
        return{
            token:"",
            nav_list: [],
        }
      },
      created() {
          this.check_user_login();
          this.get_nav();
      },
      methods:{
          check_user_login(){
            // 获取用户的登录状态
            this.token = sessionStorage.user_token || localStorage.user_token;
            return this.token;
          },
          get_nav(){
              this.$axios.get(`${this.$settings.Host}/nav/header/`,{}).then(response=>{
                  this.nav_list = response.data;
              }).catch(error=>{
                  console.log(error.response);
              })
          },
          logoutHander(){
              // 退出登录
              localStorage.removeItem("user_token");
              localStorage.removeItem("user_id");
              localStorage.removeItem("user_name");
              sessionStorage.removeItem("user_token");
              sessionStorage.removeItem("user_id");
              sessionStorage.removeItem("user_name");
              this.check_user_login();
          }
      }
    }
</script>

<style scoped>
.header-box{
  height: 80px;
}
.header{
  width: 100%;
  height: 80px;
  box-shadow: 0 0.5px 0.5px 0 #c9c9c9;
  position: fixed;
  top:0;
  left: 0;
  right:0;
  margin: auto;
  z-index: 99;
  background: #fff;
}
.header .content{
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
}
.header .content .logo{
  height: 80px;
  line-height: 80px;
  margin-right: 50px;
  cursor: pointer; /* 设置光标的形状为爪子 */
}
.header .content .logo img{
  vertical-align: middle;
}
.header .nav li{
  float: left;
  height: 80px;
  line-height: 80px;
  margin-right: 30px;
  font-size: 16px;
  color: #4a4a4a;
  cursor: pointer;
}
.header .nav li span{
  padding-bottom: 16px;
  padding-left: 5px;
  padding-right: 5px;
}
.header .nav li span a{
  display: inline-block;
}
.header .nav li .this{
  color: #4a4a4a;
  border-bottom: 4px solid #ffc210;
}
.header .nav li:hover span{
  color: #000;
}
.header .login-bar{
  height: 80px;
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center;     /* 垂直居中 */
}
.flex-item{
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center;     /* 垂直居中 */
}
.header .login-bar .shop-cart .flex-item{
  margin-right: 20px;
  border-radius: 17px;
  background: #f7f7f7;
  cursor: pointer;
  font-size: 14px;
  height: 28px;
  width: 100px;
  margin-top: 27px;
  line-height: 32px;
  text-align: center;
}
.header .login-bar .shop-cart:hover{
  background: #f0f0f0;
}
.header .login-bar .shop-cart img{
  width: 15px;
  margin-right: 4px;
  margin-left: 6px;
}
.header .login-bar .shop-cart span{
  margin-right: 6px;
}

.header .login-bar .login-box .flex-item span{
  color: #4a4a4a;
  cursor: pointer;
}
.header .login-bar .login-box span:hover{
  color: #000000;
}
.member{
    /*display: inline-block;*/
    /*height: 34px;*/
    /*margin-left: 20px;*/
}
.member img{
  width: 26px;
  height: 26px;
  border-radius: 50%;
  display: inline-block;
}
.member img:hover{
  border: 1px solid yellow;
}
/*.header .login-bar .login-box{*/
/*  margin-top: 27px;*/
/*}*/

/*.header .login-bar .login-box1{*/
/*  margin-top: 16px;*/
/*}*/
 .el-menu-demo {
  border-bottom:none !important;
}
  .el-menu-demo >>> .el-submenu__title{
   padding: 0;
   padding-right: 10px;
 }
</style>
