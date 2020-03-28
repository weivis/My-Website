<template>

  <div class="FirstScreen">
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
    <div class="contentpage main-content width-normal">
      <div class="left-sidebar">
        <div class="content-introduce">{{introduce}}</div>
        <div class="content-longintroduction">{{longintroduction}}</div>
        <div class="sidebar-box">
          <div v-for="(item,index) in button" :key="index">
            <div v-if="item.type == 1">
              <div class="sidebar-button">{{item.title}}</div>
            </div>
            <div v-else>
              <div class="sidebar-button s2">{{item.title}}</div>
            </div>
          </div>
        </div>
      </div>

      <div class='right-imgbox'>
        <img :src="this.COMMON.httpUrl + '/static/1.png'" />
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: 'firstscreen',
  data(){
    return{
      introduce:'欢迎来到WeiVi的 个人主页',
      longintroduction:'我的主页上有我的设计作品 动画作品 软件 程序 游戏 获奖作品等众多内容 欢迎阅读  如果想快速了解我可以点击下方的按钮 前往',
      button:[
        {link:'/', title:'WeiVi个人介绍 >', type:1},
        {link:'/', title:'个人项目和作品 >', type:2},
      ]
    }
  },
  components: {
  }
}
</script>

<style lang="scss" scoped>
  #particles-js{
    width: 100%;
    position:absolute;z-index:0
  }

  .FirstScreen{
    overflow: hidden;
    position: relative;
    .contentpage{
      position: relative;
    }
    .left-sidebar{
      width: 400px;
      position: absolute;
      left: 50px;
      top: 215px;
    }
    .content-introduce{
      width: 100%;
      font-size: 36px;
      font-weight: lighter;
    }
    .content-longintroduction{
      margin-top: 35px;
      width: 100%;
      font-size: 16px;
    }
    .sidebar-box{
      margin-top: 15px;
      height: 53px;
      width: 100%;
    }
    .sidebar-button{
      float: left;
      width: 156px;
      height: 53px;
      line-height: 53px;
      text-align: center;
      margin-right: 15px;
      color: #ffffff;
      background-color: #cc0152;
      font-weight: bold;
      font-size: 14px;
    }
    .s2{
      background-color: initial !important ;color: #cc0152 !important;
    }
    .right-imgbox{height:100%;float:right;margin-right:50px}
  }
</style>