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
              <a :href="item.link">
              <el-button type="primary" v-if="item.type == 1" class="elbutton">{{item.title}}</el-button>
              <el-button v-if="item.type == 2" class="elbutton">{{item.title}}</el-button>
              </a>
          </div>
        </div>
      </div>

      <div class='right-imgbox'>
        <live2d/>
        <!-- <img :src="this.Common.httpUrl + '/static/1.png'" /> -->
      </div>
    </div>
  </div>

</template>

<script>
import Live2d from './Live2d.vue'
export default {
  name: 'firstscreen',
  data(){
    return{
      introduce:'欢迎来到WeiVi的 个人主页',
      longintroduction:'我的主页上有我的设计作品 动画作品 软件 程序 游戏 获奖作品等众多内容 欢迎阅读  如果想快速了解我可以点击下方的按钮 前往',
      button:[
        {link:'/opus', title:'我的设计作品 >', type:1},
        {link:'/proj', title:'个人项目作品 >', type:2},
      ]
    }
  },
  components: {
    Live2d
  }
}
</script>

<style lang="scss" scoped>
.elbutton{
  float: left;
  margin-right: 25px;
}
  #particles-js{
    width: 100%;
    position:absolute;z-index:10
  }

  .FirstScreen{
    min-height: 700px;
    .left-sidebar{
      z-index: 20;
    }
    .right-imgbox{
      z-index: 0;
    }

    overflow: hidden;
    position: relative;
    .contentpage{
      position: relative;
    }
    .left-sidebar{
      width: 400px;
      position: absolute;
      left: 20vh;
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
      border-radius: 4px
    }
    .s2{
      background-color: initial !important ;color: #cc0152 !important;
    }
    .right-imgbox{height:100%;float:right;margin-right:-80px}
  }
</style>