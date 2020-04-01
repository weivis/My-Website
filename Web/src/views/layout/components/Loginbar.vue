<template>
  <div class="HeaderLoginbar">
    <div class="userbar" v-if="AuthUser">
        <el-dropdown>
          <span class="el-dropdown-link">
            欢迎你: {{UserData.UserName}}<i class="el-icon-arrow-down el-icon--right"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
              <el-dropdown-item @click.native="Logout_user">退出登录</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
        <!-- <div class="username">
            <span>欢迎你: {{UserData.UserName}}</span>
        </div> -->
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
  created() {
    this.Redata()
  },
  mounted(){
    // console.log(123)
  },
  methods: {
    Logout_user(){
      // console.log('执行')
      this.Auth.Logout_user()
      this.LogoutUserInfo()
      console.log(this.LoginStatus())
      // this.$router.push('/')
      if (this.LoginStatus() == null){
        // console.log('退出登录')
        this.$router.go(0)
      }
    },
    Redata(){
      // console.log('头部重新获取')
      this.AuthUser = this.Auth.AuthUser()
      //  console.log('头部重新获取1')
      this.loginurl = this.Common.LoginUrl
      //  console.log('头部重新获取2')
      this.UserData = this.UserInfo()
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