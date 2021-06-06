import axios from "axios"

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

// 导入实例  
export default instance;