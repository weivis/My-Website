import request from '@/utils/request'

/* 通用api */
export function upload(data) {
  return request({
    url: '/upload/',
    method: 'post',
    data: data,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
}

// 上传文章
export function upload_article(data) {
  return request({
    url: '/article/upload',
    method: 'post',
    data: data
  })
}

// 根据文章id获取内容
export function article_query(id) {
  return request({
    url: '/article/query-article',
    method: 'POST',
    data: {
      id:id
    }
  })
}

// 获取作品列表
export function article_opuslist(content_type) {
  return request({
    url: '/article/query-list',
    method: 'post',
    data: {
      article_type:1,
      content_type:content_type
    }
  })
}

// 获取文章列表
export function article_articlelist() {
  return request({
    url: '/article/query-list',
    method: 'post',
    data: {
      article_type:2
    }
  })
}

// 获取项目列表
export function article_projlist() {
  return request({
    url: '/article/query-list',
    method: 'post',
    data: {
      article_type:3
    }
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
export function Logout(token) {
  return request({
    url: '/auth/Logout',
    method: 'post',
    data: {
      'Token':token
    }
  })
}