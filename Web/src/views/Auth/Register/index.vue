<template>

  <div class="main">
    <el-row :gutter="20" justify="center" type="flex" >
      <el-col :span="6" class="box">
        <span class="input-title">用户名</span>
        <el-input v-model="username" placeholder="用户名" class="input"></el-input>
        <span class="input-title">邮箱</span>
        <el-input v-model="email" placeholder="邮箱" class="input"></el-input>
        <span class="input-title">密码</span>
        <el-input placeholder="请输入密码" v-model="password" show-password class="input"></el-input>
        <span class="input-title">重复输入一次密码</span>
        <el-input placeholder="请输入密码" v-model="repassword" show-password class="input"></el-input>
      </el-col>
    </el-row>
    <el-row :gutter="20" justify="center" type="flex" >
      <el-button type="primary" align="center" @click="register">立即注册</el-button>
    </el-row>
  </div>

</template>

<script>

export default {
  name: 'register',
  data(){
    return{
      username:'',
      email:'',
      password:'',
      repassword:''
    }
  },
  components: {
  },
  created() {
    this.RegisterUrl = this.Common.RegisterUrl;
    if (this.LoginStatus()) {
      // 如果用户已经登录就跳转回首页
      this.$router.push({ name: "Home", params: { topage: "login" } });
    }
  },
  methods:{
    register(){
      console.log(this.username)
      console.log(this.email)
      console.log(this.password)
      console.log(this.repassword)
      if (this.password != this.repassword){
          this.$message({
            type: "info",
            message: "密码不一致"
          });
      }else{
      this.$http.regaccount({
        username:this.username,
        email:this.email,
        password:this.password,
        repassword:this.repassword,
      })
      .then(response => {
        if (response.code == 200){
          this.$router.push({ name: "login" })
        }
      })
      .catch(error => {
        console.log("error", error);
      });
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.box{margin-top: 50px;}
.input-title{line-height: 30px;font-size: 14px;}
.input{margin-bottom: 15px;}
</style>