<template>
  <div class="Main">
    <vue-particles
      color="#409EFF"
      :particleOpacity="0.7"
      :particlesNumber="60"
      shapeType="circle"
      :particleSize="4"
      linesColor="#409EFF"
      :linesWidth="1"
      :lineLinked="true"
      :lineOpacity="0.4"
      :linesDistance="150"
      :moveSpeed="2"
      :hoverEffect="true"
      hoverMode="grab"
      :clickEffect="true"
      clickMode="push"
      class="lizi"
    ></vue-particles>
    <div class="content-main main-content width-normal">
      <div class="loginbox">
        <div class="login-title">登录你的游客账户</div>
        <el-input
          v-model="email"
          class="txt-input"
          placeholder="Email 邮箱"
          prefix-icon="el-icon-user"
        ></el-input>
        <el-input
          v-model="password"
          class="txt-input"
          placeholder="Password 密码"
          prefix-icon="el-icon-key"
          show-password
        ></el-input>
        <div style="text-align:center;margin-top: 20px;">
          <el-button type="primary" round align="center" @click.native="loginstart">立即登录</el-button>
        </div>
        <el-divider content-position="center" style="ackground-color: #f0f0f0;">or</el-divider>
        <div style="text-align:center;margin-top: 20px;">
          <a :href="RegisterUrl">
            <el-button round align="center">注册</el-button>
          </a>
        </div>
      </div>
      <div class="image">
        <el-image :src="image"></el-image>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "login",
  created() {
    this.RegisterUrl = this.Common.RegisterUrl;
    if (this.LoginStatus()) {
      // 如果用户已经登录就跳转回首页
      this.$router.push({ name: "Home", params: { topage: "login" } });
    }
  },
  data(){
    return {
      email: "",
      password: "",
      image: this.Common.httpUrl + "/static/login.png",
      RegisterUrl: ""
    };
  },
  methods: {
    seedauth(){
      var regEmail = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/
        if (this.email != '' && !regEmail.test(this.email)) {
            this.$message({
                message: '邮箱格式不正确',
                type: 'error'
            })
            return false
            // this.email = ''
        } else {
          if (this.password == ''){
            this.$message({
                message: '密码不能为空',
                type: 'error'
            })
            return false
          } else {
            return true
          }
        }
    },
    loginstart() {
      if (this.seedauth() == false){
        return console.log('终止')
      }
      this.$message({
          message: '正在登录中',
          type: 'success'
      })
      console.log(this.email)
      console.log(this.password)
      this.$http
        .login(this.email, this.password)
        .then(response => {
          if (response.code == 200){
            this.Login_user(
              response.data.Token,
              response.data.userID,
              response.data.group
            );
            this.LoginUserInfo(
              response.data.username,
              response.data.userID,
              response.data.head
            );
            this.$router.push({ name: "Home", params: { topage: "login" } });
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    }
  }
};
</script>
<style type="css">
.el-divider__text {
  background-color: #fbfbfb;
  color: #9e9e9e;
}
</style>
<style>
.app-main {
  margin-top: 0px !important;
  min-height: calc(100vh - 230px) !important;
}
.layout-header {
  position: absolute !important;
  /* top: 30px !important; */
  border-bottom: 0 !important;
  box-shadow: initial !important;
  background-color: initial !important;
}
</style>

<style lang="scss" scoped>
.lizi {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 10;
}
.Main {
  .image {
    position: absolute;
    width: 40%;
    max-width: 460px;
    min-width: 400px;
    left: 10%;
    z-index: 0;
    top: 100px;
  }
  .content-main {
    position: relative;
    margin-top: 50px;
    z-index: 30;
  }
  .loginbox {
    border-radius: 3px;
    width: 300px;
    height: 300px;
    z-index: 999;
    float: right;
    margin-top: 200px;
    background-color: #fbfbfb;
    margin-right: 10%;
    border: 1px solid #f4f4f4;
    padding: 20px;
  }
  .login-title {
    color: #8a8a8a;
    margin: 0;
    border: 0;
    width: 100%;
    padding: 0;
    font-size: 14px;
  }
  .txt-input {
    position: relative;
    font-size: 14px;
    display: inline-block;
    width: 100%;
    margin-top: 20px;
  }
}
</style>