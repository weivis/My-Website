import request from '@/utils/request'

// 获取全部类型的文章内容
export function article_query(id) {
  return request({
    url: '/article/query-article?id=' + id,
    method: 'get',
    data: {}
  })
}

// 获取作品列表
export function article_opuslist(content_type) {
  return request({
    url: '/article/query-list?article_type=1&content_type=' + content_type,
    method: 'get',
    data: {}
  })
}

// 获取文章列表
export function article_articlelist() {
  return request({
    url: '/article/query-list?article_type=2',
    method: 'get',
    data: {}
  })
}

// 获取项目列表
export function article_projlist() {
  return request({
    url: '/article/query-list?article_type=3',
    method: 'get',
    data: {}
  })
}

// 登录
export function login(email, password) {
  return request({
    url: '/auth/login',
    method: 'post',
    data: {
      email,
      password
    }
  })
}

// 登出
export function Logout(userid, token) {
  return request({
    url: '/auth/Logout',
    method: 'post',
    data: {
      userid,token
    }
  })
}