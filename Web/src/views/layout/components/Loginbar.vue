<template>
  <div class="HeaderLoginbar">
    <div class="userbar" v-if="AuthUser">
      <el-dropdown>
        <span class="el-dropdown-link">
          欢迎你: {{UserData.UserName}}
          <i class="el-icon-arrow-down el-icon--right"></i>
        </span>
        <el-dropdown-menu slot="dropdown">

          <div v-if="this.isAdmin()">
            <a href="/upload"><el-dropdown-item>发布文章</el-dropdown-item></a>
          </div>

          <div v-if="this.isAdmin()">
            <a href="/manager"><el-dropdown-item>管理文章</el-dropdown-item></a>
          </div>

          <el-dropdown-item @click.native="Logout_users">退出登录</el-dropdown-item>

        </el-dropdown-menu>
      </el-dropdown>
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
    if(this.AuthUser){
      this.UserData = this.UserInfo();
    }
    this.loginurl = this.Common.LoginUrl;
  },
  methods: {
    Logout_users() {
      const AuthUserData = this.AuthUserData();
      this.$http
        .Logout(AuthUserData.token)
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