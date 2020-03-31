<template>

  <div class="Dynamics">
  <div class="headerbox" :style="path">
      <div class="contentbox main-content width-normal">
        <div class="header">
          <div class="headertitlech">我的动态</div>
          <div class="headertitleen">Dynamics</div>
        </div>
        <div class="content">
          <div class="contentl">
            <div class="content-title">研发项目</div>
            <div class="content-list">

              <div class="content-porj-item" v-for="(item,index) in projects" :key="index">
                <el-row :gutter="20">
                  <el-col :span="11">
                    <a :href="item.link">
                      <el-image class="content-porj-item-cover" :src="item.cover"></el-image>
                    </a>
                  </el-col>
                  <el-col :span="13">
                    <a :href="item.link">
                      <div class="content-porj-item-text-title">{{item.title}}</div>
                      <div class="content-porj-item-text-introduce">{{item.introduce}}</div>
                    </a>
                  </el-col>
                </el-row>
                
              </div>

            </div>
          </div>
          <div class="contentr">
            <div class="content-title">公开文章</div>
            <div class="content-list">

              <div class="content-avet-item" v-for="(item,index) in article" :key="index">
                <el-row :gutter="20">
                  <el-col :span="8">
                    <a :href="item.link">
                      <el-image class="content-avet-item-cover" :src="item.cover"></el-image>
                    </a>
                  </el-col>
                  <el-col :span="13">
                    <a :href="item.link">
                      <div class="content-avet-item-title">{{item.title}}</div>
                    </a>
                  </el-col>
                </el-row>
                
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>
<script>

// console.log(this.Common.httpUrl)
// :style="`background-image: url(${this.path})`"

// console.log(Common.httpUrl)

import Common from '@/Common.vue'
export default {
  name: 'dynamics',
  data() {
    return {
      path:{
        backgroundImage:"url(" + Common.httpUrl + '/static/dynamics-background.png' + ")",
      },
      projects:[
        {
          cover:'http://127.0.0.1:8080/static/proj1.png',
          title:'iliya Ai',
          introduce:'iliyaA 伊莉雅人工智能助手',
          link:'1'
        }
      ],
      article:[
        {
          cover:'http://127.0.0.1:8080/static/proj1.png',
          title:'Niputv视频网站 视频上传技术解析 Python  Flask 处理转码分发上传解决方案',
          link:'1'
        },
        {
          cover:'http://127.0.0.1:8080/static/proj1.png',
          title:'Python + AE云视频渲染解决方案',
          link:'1'
        }
      ]
    }
  },
}
</script>

<style lang="scss" scoped>
.Dynamics{
  height: 800px;
  .headerbox{
    width: 100%;
    overflow: hidden;
    background-repeat: no-repeat;
    background-position-x: 130px;
  }
  .header{
    height: 235px;
    overflow: hidden;
    width: 100%;
  }
  .headertitlech{margin-top: 115px;font-size: 18px;height: 18px;width: 100%;}
  .headertitleen{margin-top: 5px;font-size: 30px;font-weight: bold; width: 100%;}
  .content{
    width: 100%;
    height: 500px;
  }
  .contentl{
    width: 48%;
    height: 100%;
    float: left;
  }
  .contentr{
    width: 48%;
    height: 100%;
    border-left: 1px solid #e9e9e9;
    float: right;
    padding-left: 20px;
  }
  .content-title{
    font-size: 16px;font-weight: bold;color: #000;
  }
  // .content-list{}
  .content-porj-item{width: 100%;margin-top: 20px;}
  .content-porj-item-cover{border-radius: 4px;overflow: hidden;}
  .content-porj-item-text-title{font-size: 24px;margin-top: 30px;width: 100%;color: #000;}
  .content-porj-item-text-introduce{margin-top: 10px;font-size: 14px;width: 100%;color: #000;}
  .content-avet-item{width: 100%;margin-top: 20px;}
  .content-avet-item-cover{border-radius: 4px;overflow: hidden;}
  .content-avet-item-title{font-size: 14px;color: #000;}
}

</style>