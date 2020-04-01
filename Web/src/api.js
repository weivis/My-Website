import request from '@/utils/request'

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

export function Logout(userID, token) {
  return request({
    url: '/auth/Logout',
    method: 'post',
    data: {
      userID,token
    }
  })
}