<template>
  <div class="HeaderLoginbar">

    <div class="login">
        <a href="/">
        <div class="visitor_login">游客登录</div>
        </a>
    </div>

    <div class="userbar">
        <a href="/">
        <div class="username">
            <span>欢迎你: 唯酱</span>
        </div>
        </a>
    </div>

  </div>
</template>
<script>
export default {
  name: "HeaderLoginbar",
  methods: {
    //事件处理器
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