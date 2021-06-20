import axios from "axios"
import router from "../router";

//创建axios的实例
const instance = axios.create({
    baseURL: 'http://127.0.0.1:5000',
    timeout: 10000,
    headers: {'content-type': 'application/json'}
  });

  // axios的hook函数 在发送请求前会主动调用此函数
instance.interceptors.request.use(function(config) {
    // 如果token存在 并且发送的不是登录接口的话，就把token加入到认证中
    if (localStorage.getItem("token")&& config.url != '/login') {
        config.auth = {username: localStorage.getItem("token"), password:""}
    }
    return config;
});
// 如果发送的请求，响应信息内有错误，会回调error的内容
instance.interceptors.response.use((response) => {
    return response;
  },  (error)=> {
    // 如果请求结果状态码是401的话，代表校验失败，就跳转回login
    // 同时清理token
    if (error.response) {
        if(error.response.status == 401) {
            // 清除token
            localStorage.removeItem("token");
            router.replace({"name": "Login"});
            console.log("123")
            return Promise.reject(error);
        }
    }
  });

// 导入实例  
export default instance;