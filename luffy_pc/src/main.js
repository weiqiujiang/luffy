// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import settings from './settings'

Vue.config.productionTip = false
Vue.prototype.$settings = settings
/* element-ui 配置 */
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);
/* 导入css初始化配置 */
import '../static/css/reset.css';
/* 导入极验sdk */
import '../static/js/gt';
import axios from 'axios';
axios.defaults.withCredentials = false;// 组织ajax携带cookie
Vue.prototype.$axios = axios; //把对象挂载到vue中
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
