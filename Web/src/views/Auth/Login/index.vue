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
        <div class="login-title">游客登陆</div>
        <el-input v-model="email" class="txt-input" placeholder="Email 邮箱" prefix-icon="el-icon-user"></el-input>
        <el-input v-model="password" class="txt-input" placeholder="Password 密码" prefix-icon="el-icon-key" show-password></el-input>
        <div style="text-align:center;margin-top: 20px;">
          <el-button type="primary" round align="center">立即登录</el-button>                  
        </div>
        <el-row type="flex" style="margin-top: 20px;" justify="space-around">
          
          <el-col></el-col>
        </el-row>
        
        <el-divider></el-divider>
      </div>
    </div>
  </div>

</template>

<script>

export default {
  name: 'login',
  data(){
    return{
      email:'',
      password:''
    }
  },
  components: {
  }
}
</script>

<style>
  .app-main{
    margin-top: 0px !important;
  }
  .layout-header{
    position: absolute !important;
    top: 30px !important;
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
    .content-main{
      position: relative;
      margin-top: 50px;
      z-index: 20;
    }
    .loginbox{
      width: 300px;
      height: 300px;
      z-index: 30;
      float: right;
      margin-top: 200px;
      background-color:rgba(0, 0, 0, 0.06);
      margin-right: 50px;
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