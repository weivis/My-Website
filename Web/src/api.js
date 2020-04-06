import request from '@/utils/request'

export function article_query(id) {
  return request({
    url: '/article/query?id=' + id,
    method: 'get',
    data: {
    }
  })
}

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

export function Logout(userid, token) {
  return request({
    url: '/auth/Logout',
    method: 'post',
    data: {
      userid,token
    }
  })
}