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
            <div class="content-title">个人项目</div>
            <div class="content-list">

              <div class="content-porj-item" v-for="(item,index) in projects" :key="index">
                <el-row :gutter="20">
                  <el-col :span="11">
                    <a :href="'/page?id=' + item.id">
                      <el-image class="content-porj-item-cover" :src="item.cover"></el-image>
                    </a>
                  </el-col>
                  <el-col :span="13">
                    <a :href="'/page?id=' + item.id">
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
                    <a :href="'/page?id=' + item.id">
                      <el-image class="content-avet-item-cover" :src="item.cover"></el-image>
                    </a>
                  </el-col>
                  <el-col :span="13">
                    <a :href="'/page?id=' + item.id">
                      <div class="content-avet-item-title">{{item.title}}</div>
                      <div class="content-porj-item-text-introduce">{{item.introduce}}</div>
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
      ],
      article:[
      ]
    }
  },
  created() {
    this.query_list();
  },
  methods: {
    query_list() {
      this.$http
        .index_dynamics_data()
        .then(response => {
          if (response.code == 200) {
            this.projects = response.data.project.slice(0,2);
            this.article = response.data.article.slice(0,3);
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    }
  }
}
</script>

<style lang="scss" scoped>
.Dynamics{
  height: 800px;
  margin-bottom: 100px;
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
    // height: 500px;
    margin-bottom: 30px;
    overflow: hidden;
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