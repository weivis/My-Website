import Vue from 'vue'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import { Message } from 'element-ui'
import '@/styles/common.scss' // global css
import VueParticles from 'vue-particles'
import '@/permission' // permission control
import locale from 'element-ui/lib/locale/lang/zh-CN' // lang i18n
import VueLive2d from 'vue-live2d-model' 
import App from './App.vue'
import router from './router'
// import store from './store' 取消vuex

Vue.config.productionTip = false

import * as StoreUser from './store/user'
import Common from './Common'
import Auth from './Auth'
import * as api from './api'

Vue.prototype.$http = api
Vue.prototype.Common = Common
Vue.prototype.$httpUrl = Common.httpUrl
Vue.prototype.Message = Message
Vue.prototype.isAdmin = Auth.isAdmin
Vue.prototype.AuthUserData = Auth.AuthUserData
Vue.prototype.Login_user = Auth.Login_user
Vue.prototype.Logout_user = Auth.Logout_user
Vue.prototype.LoginStatus = Auth.AuthUser
Vue.prototype.UserInfo = StoreUser.QueryUserInfo
Vue.prototype.LoginUserInfo = StoreUser.StoreUserInfo
Vue.prototype.LogoutUserInfo = StoreUser.RemoveUserInfo

// Vue.use(ElementUI);
Vue.use(ElementUI, { locale })
Vue.use(VueParticles)
Vue.use(VueLive2d)
new Vue({
  el: '#app',
  router,
  render: h => h(App)
}).$mount('#app')

// console.log(Vue.prototype.COMMON)