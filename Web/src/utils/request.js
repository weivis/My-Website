import axios from 'axios'
import {Message} from 'element-ui'
// import store from '../store'
// import { getToken } from '@/utils/auth'

// // 判断运行环境，如果是生产环境就获取服务器地址，如果是开发环境获取配置dev.env.js
// let HttpRoot = (process.env.NODE_ENV === 'production')
//   ? (location.protocol + '//' + location.host)
//   : process.env.BASE_API

let HttpRoot = 'http://127.0.0.1:8080'

// 创建axios实例
const service = axios.create({
  baseURL: HttpRoot, // api 的 base_url
  timeout: 15000, // 请求超时时间
  // withCredentials: false
})

// request拦截器
service.interceptors.request.use(
  config => {

    // console.log('methods',config.method)
    // if (store.getters.token) {
      // config.headers['Admin-Token'] = getToken() // 让每个请求携带自定义token 请根据实际情况自行修改
    // }
    return config
  },
  error => {
    // Do something with request error
    console.log(error) // for debug
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
    // console.log('res',res)

    if (res && res.code !== 200) {
      Message({
        message: res.msg,
        type: 'error',
        duration: 5 * 1000
      })
    } else {
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


