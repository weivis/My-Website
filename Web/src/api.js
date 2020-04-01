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