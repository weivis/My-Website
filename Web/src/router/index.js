import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

/* Layout */
import Layout from '../views/layout/Layout'

const routes = [
  {
    // 根
    path: '/',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'Home',
        component: () => import('@/views/Home/index'),
        meta: { pagename: 'My Website', title:'WeiVi的个人主页'}
      }
    ]
  },
  {
    // 作品
    path: '/opus',
    component: Layout,
    children: [
      {
        path: '/opus',
        name: 'opus',
        component: () => import('@/views/Opus/index'),
        meta: { pagename: 'Opus', title:'作品' }
      },
      {
        path: 'design',
        name: 'design',
        component: () => import('@/views/Opus/Design/index'),
        meta: { pagename: 'Design', title:'设计作品' }
      }
    ]
  },
  {
    // 认证
    path: '/auth',
    component: Layout,
    children: [
      {
        path: 'sign-in',
        name: 'login',
        component: () => import('@/views/Auth/Login/index'),
        meta: { pagename: 'Sign-in', title:'登录'}
      },
      {
        path: 'register',
        name: 'register',
        component: () => import('@/views/Auth/Register/index'),
        meta: { pagename: 'Register', title:'注册' }
      }
    ]
  },
  {
    // 文章
    path: '/article',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'article',
        component: () => import('@/views/Article'),
        meta: { pagename: 'Article', title:'文章'}
      }
    ]
  },
  {
    // 项目
    path: '/proj',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'proj',
        component: () => import('@/views/Proj'),
        meta: { pagename: 'Projects', title:'项目'}
      }
    ]
  },
  {
    // 摄影
    path: '/photo',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'photo',
        component: () => import('@/views/Photo'),
        meta: { pagename: 'Photo', title:'摄影'}
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
