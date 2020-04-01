import axios from 'axios'
import { Message } from 'element-ui'
import Auth from '../Auth'
import router from '../router'

let HttpRoot = 'http://127.0.0.1:8080'

// 创建axios实例
const service = axios.create({
  baseURL: HttpRoot, // api 的 base_url
  timeout: 15000, // 请求超时时间
  withCredentials: false
})

// request拦截器
service.interceptors.request.use(
  config => {
    if (Auth.AuthUser()) {
      console.log('>request拦截器被执行')
      const AuthUserData = Auth.AuthUserData()
      config.data['token'] = AuthUserData.token
      config.data['userID'] = AuthUserData.userid
    }
    return config
  },
  error => {
    console.log(error)
    Promise.reject(error)
  }
)

// response 拦截器
service.interceptors.response.use(
  response => {
    /**
     * code为非20000是抛错 可结合自己业务进行修改
     */

    const res = JSON.parse(JSON.stringify(response.data))
    console.log('接口Return: ', res)

    if (res && res.code !== 200) {

      if (res && res.code == 10000 || res.code == 10086) {
        // 如果code == 10000 or 10086 代表该用户的登录状态已经失效 清除登录状态并返回登录页面
        console.log('10000 or 10086')
        Auth.Logout_user()
        localStorage.removeItem('UserName');
        localStorage.removeItem('UserId');
        localStorage.removeItem('UserHead');
        localStorage.clear();
        Message({
          message: res.msg,
          type: 'error',
          duration: 5 * 1000
        })
        router.push({ name: "login", params: { msg: res.msg } })

      } else {
        Message({
          message: res.msg,
          type: 'error',
          duration: 5 * 1000
        })
      }
    } else {
      console.log('response 拦截器:', res.msg)
      Message({
        message: res.msg,
        type: 'success',
        duration: 5 * 1000
      })
    }
    return res
  },
  error => {
    console.log('err' + error) // for debug
    Message({
      message: error.message,
      type: 'error',
      duration: 5 * 1000
    })
    return Promise.reject(error)
  }
)

service.httpRoot = HttpRoot

export default service


