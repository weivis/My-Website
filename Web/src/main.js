import Vue from 'vue'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import '@/styles/common.scss' // global css
import global from './Common.vue'
import VueParticles from 'vue-particles'

import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

Vue.prototype.COMMON = global

Vue.use(ElementUI);
Vue.use(VueParticles)

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
}).$mount('#app')
