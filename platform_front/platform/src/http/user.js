import axios from "./http"

const user = {
    login(loginData) {
        // 使用axios的get方法发送get请求，auth代表校验，和requests的auth相同
        return axios.get("/login", {auth: loginData});
    },
};

export default user