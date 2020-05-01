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
    // 上传文章
    path: '/article-upload',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'upload',
        component: () => import('@/views/Article/upload'),
        meta: { pagename: 'UploadArticle', title:'上传文章'}
      }
    ]
  },
  {
    // 管理
    path: '/article-manager',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'articlelist',
        component: () => import('@/views/Manager/ArticleList'),
        meta: { pagename: 'Article-Manager', title:'文章管理'}
      },
      {
        path: '/edit',
        name: 'articleedit',
        component: () => import('@/views/Manager/ArticleEdit'),
        meta: { pagename: 'Article-Edit', title:'文章编辑'}
      }
    ]
  },
  {
    // 推荐管理
    path: '/recommend-manager',
    component: Layout,
    children: [
      {
        path: '/',
        name: 'recommendlist',
        component: () => import('@/views/Manager/RecommendList'),
        meta: { pagename: 'Recommend-Manager', title:'推荐管理'}
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
        component: () => import('@/views/Article/opus'),
        meta: { pagename: 'Opus', title:'作品' }
      },
      {
        path: 'design',
        name: 'opusitem',
        component: () => import('@/views/Article/item/opusitem'),
        meta: { pagename: 'Design', title:'设计作品' }
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
        component: () => import('@/views/Article/article'),
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
        component: () => import('@/views/Article/proj'),
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
