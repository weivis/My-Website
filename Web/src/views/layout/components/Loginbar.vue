<template>
  <div class="HeaderLoginbar">
    <div class="userbar" v-if="AuthUser">
        <a href="/">
        <div class="username">
            <span>欢迎你: {{UserData.UserName}}</span>
        </div>
        </a>
    </div>

    <div class="login" v-else>
        <a :href="loginurl">
        <div class="visitor_login">游客登录</div>
        </a>
    </div>

  </div>
</template>
<script>
export default {
  name: "HeaderLoginbar",
  data() {
    return {
      AuthUser:'',
      loginurl:'',
      UserData:''
    }
  },
  methods: {
  },
  created:function(){
    this.AuthUser = this.Auth.AuthUser()
    this.loginurl = this.Common.LoginUrl
    this.UserData = this.UserInfo()
  }
};
</script>
<style lang="scss" scoped>
.HeaderLoginbar {
    margin-left: 25px;
  float: right;
  height: 25px;
  line-height: 25px;
  font-size: 14px;
  a {
    color: #525252;
  }
  .username {
    float: right;
  }
  .visitor_login {
    float: right;
  }
}
</style>