import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

/* Layout */
import Layout from '../views/layout/Layout'

const routes = [
  {
    path: '/',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'index',
        component: () => import('@/views/Home/index'),
        meta: { pagename: 'My Website', title:'WeiVi的个人主页'}
      }
    ]
  },
  {
    path: '/works',
    component: Layout,
    children: [
      {
        path: '/works',
        name: 'works',
        component: () => import('@/views/Works/index'),
        meta: { pagename: 'Works', title:'作品' }
      },
      {
        path: 'design',
        name: 'design',
        component: () => import('@/views/Works/WorksDesign/index'),
        meta: { pagename: 'Design', title:'设计作品' }
      }
    ]
  },
  {
    path: '/login',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'login',
        component: () => import('@/views/Auth/Login/index'),
        meta: { pagename: 'Sign-in', title:'登录'}
      },
      {
        path: 'register',
        name: 'register',
        component: () => import('@/views/Works/WorksDesign/index'),
        meta: { pagename: 'Register', title:'注册' }
      }
    ]
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
