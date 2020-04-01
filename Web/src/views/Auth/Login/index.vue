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
    >
    </vue-particles>
    <div class="content-main main-content width-normal">
      <div class="loginbox">
        <div class="login-title">登录你的游客账户</div>
        <el-input v-model="email" class="txt-input" placeholder="Email 邮箱" prefix-icon="el-icon-user"></el-input>
        <el-input v-model="password" class="txt-input" placeholder="Password 密码" prefix-icon="el-icon-key" show-password></el-input>
        <div style="text-align:center;margin-top: 20px;">
          <el-button type="primary" round align="center" @click.native="loginstart">立即登录</el-button>                  
        </div>
        <el-divider content-position="center" style="ackground-color: #f0f0f0;">or</el-divider>
        <div style="text-align:center;margin-top: 20px;">
          <el-button round align="center">注册</el-button>             
        </div>
      </div>
      <div class="image"><el-image :src="image"></el-image></div>
    </div>
  </div>

</template>

<script>

export default {
  name: 'login',
  created(){
    if(this.LoginStatus()){
      this.$router.push({name: "Home", params: {topage:'login'}})
    }
  },
  data(){
    return{
      email:'',
      password:'',
      image:this.Common.httpUrl + '/static/login.png'
    }
  },
  methods: {
    loginstart(){
      console.log(this.email)
      console.log(this.password)
      // this.Auth.Login_user('weivi')
      // this.LoginUserInfo('WeiVi',1,'1.png')
      // if (this.LoginStatus()){
      //   this.$forceUpdate()
      //   // this.$router.push({ name: "Home" });
      //   // this.$router.go(0)
      //   this.$router.push({name: "Home", params: {topage:'login'}})
      // }

      this.$http.login(this.email, this.password).then(response => {
          console.log('cookie',response)
          // const data = JSON.parse(JSON.stringify(response.d))
          // console.log(data)
          // if (response.c === 0) {
            // setToken(data.session_id)
            // console.log(data.session_id)
            // localStorage.setItem('token', data.session_id) // 本地缓存token
            // localStorage.setItem('username', username) // 本地缓存用户名
            // commit('SET_TOKEN', data.session_id)
          // }
        }).catch(error => {
          console.log('error', error);
        })

    }
  },
  components: {
  }
}
</script>
<style type="css">
  .el-divider__text{background-color: #fbfbfb;color: #9e9e9e;}
</style>
<style>
  .app-main{
    margin-top: 0px !important;
    min-height: calc(100vh - 230px) !important;
  }
  .layout-header{
    position: absolute !important;
    /* top: 30px !important; */
    border-bottom: 0 !important;
    box-shadow: initial !important;
    background-color: initial !important;
  }
</style>

<style lang="scss" scoped>
  .lizi{
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 10;
  }
  .Main{
    .image{
    position: absolute;
    width: 40%;
    max-width: 460px;
    min-width: 400px;
    left: 10%;
    z-index: 0;
    top: 100px;
    }
    .content-main{
      position: relative;
      margin-top: 50px;
      z-index: 30;
    }
    .loginbox{
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
    .login-title{
      color: #8a8a8a;
      margin: 0;
      border: 0;
      width: 100%;
      padding: 0;
      font-size: 14px;
    }
    .txt-input{
      position: relative;
      font-size: 14px;
      display: inline-block;
      width: 100%;
      margin-top: 20px;
    }
  }
</style>