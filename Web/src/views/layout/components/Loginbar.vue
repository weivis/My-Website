<template>
  <div class="HeaderLoginbar">
    <div class="userbar" v-if="AuthUser">
      <el-dropdown>
        <span class="el-dropdown-link">
          欢迎你: {{UserData.UserName}}
          <i class="el-icon-arrow-down el-icon--right"></i>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item @click.native="Logout_users">退出登录</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <!-- <div class="username">
            <span>欢迎你: {{UserData.UserName}}</span>
      </div>-->
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
      AuthUser: "",
      loginurl: "",
      UserData: ""
    };
  },
  created() {
    this.AuthUser = this.LoginStatus();
    this.loginurl = this.Common.LoginUrl;
    this.UserData = this.UserInfo();
  },
  methods: {
    Logout_users() {
      const AuthUserData = this.AuthUserData();
      this.$http
        .Logout(AuthUserData.userid, AuthUserData.token)
        .then(response => {
          if (response.code === 200) {
            console.log('>用户退出登录')
            this.Logout_user();
            this.LogoutUserInfo();
            this.$router.go(0)
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    }
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