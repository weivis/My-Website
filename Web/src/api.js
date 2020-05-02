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

// 管理文章获取列表
export function query_article(article_type, content_type, queryPage) {
  return request({
    url: '/article/query-list',
    method: 'post',
    data: {
      admin:'admin',
      article_type:article_type,
      content_type:content_type,
      queryPage:queryPage
    }
  })
}

// 获取作品列表
export function article_opuslist(content_type, queryPage) {
  return request({
    url: '/article/query-list',
    method: 'post',
    data: {
      article_type:1,
      content_type:content_type,
      queryPage:queryPage
    }
  })
}

// 获取文章列表
export function article_articlelist(queryPage) {
  return request({
    url: '/article/query-list',
    method: 'post',
    data: {
      article_type:2,
      queryPage:queryPage
    }
  })
}

// 获取项目列表
export function article_projlist(queryPage) {
  return request({
    url: '/article/query-list',
    method: 'post',
    data: {
      article_type:3,
      queryPage:queryPage
    }
  })
}

// 管理员修改文章状态
export function admin_change_articlestatus(id,type) {
  return request({
    url: '/article/change',
    method: 'post',
    data: {
      id:id,
      to:type
    }
  })
}

// 首页更多文章-获取
export function index_morelink_list(data) {
  return request({
    url: '/index/more_article/list',
    method: 'post',
    data: data
  })
}

// 首页更多文章-添加
export function index_morelink_add(articleid, title, cover, introduce, link) {
  return request({
    url: '/index/more_article/add',
    method: 'post',
    data: {
      articleid:articleid,
      title:title,
      cover:cover,
      introduce:introduce,
      link:link
    }
  })
}

// 首页更多文章-变更
export function index_morelink_change(id, change_type, sort) {
  const data = {
    id:id,
    change_type:change_type,
    sort:sort
  }
  console.log(data)
  return request({
    url: '/index/more_article/change',
    method: 'post',
    data: data
  })
}

// 首页更多文章-变更
export function index_dynamics_data() {
  return request({
    url: '/index/index-dynamics/data',
    method: 'post',
    data: {}
  })
}

// 相册列表
export function photo_list() {
  return request({
    url: '/photo/list',
    method: 'post',
    data: {}
  })
}

// 相册添加图片
export function photo_add(link, title) {
  return request({
    url: '/photo/add',
    method: 'post',
    data: {link:link, title:title}
  })
}

// 相册更改图片
export function photo_change(id, change_type, sort) {
  return request({
    url: '/photo/change',
    method: 'post',
    data: {id:id, change_type:change_type, sort:sort}
  })
}

// 相册更改图片
export function article_edit(data) {
  return request({
    url: '/article/edit',
    method: 'post',
    data: data
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

// 登录
export function regaccount(data) {
  return request({
    url: '/auth/register',
    method: 'post',
    data: data
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