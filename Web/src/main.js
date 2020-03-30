import Vue from 'vue'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import '@/styles/common.scss' // global css
import VueParticles from 'vue-particles'
import '@/permission' // permission control

import App from './App.vue'
import router from './router'
// import store from './store' 取消vuex

Vue.config.productionTip = false

import * as StoreUser from './store/user'
import Common from './Common'
import Auth from './Auth'

Vue.prototype.Common = Common
Vue.prototype.Auth = Auth
Vue.prototype.UserInfo = StoreUser.QueryUserInfo

Vue.use(ElementUI);
Vue.use(VueParticles)

new Vue({
  el: '#app',
  router,
  render: h => h(App)
}).$mount('#app')

// console.log(Vue.prototype.COMMON)