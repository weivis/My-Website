import Cookies from 'js-cookie'

const LoginTokenID = 'LoginToken'

export function AuthUser() {
    // 如果 AuthUser为空 表示用户未登录
  return Cookies.get(LoginTokenID)
}

export function Login_user(token) {
    // 用户登录 Login_user(usertoken)
  return Cookies.set(LoginTokenID, token)
}

export function Logout_user() {
    // 取消登录 Logout_user
  return Cookies.remove(LoginTokenID)
}