<template>
    <div class="layout-footer">
        <div class="main-content width-normal">

        <div class="footer-mainbav">
            <el-row :gutter="20">
                <el-col :span="4">
                    <div class="mainbav-title">WeiVi</div>
                    <div class="mainbav-itemlist">
                        <li v-for="(item,index) in weivi" :key="index"><a class="mainbav-item" :href="item.link"><div class="mainbav-item">{{item.title}}</div></a></li>
                    </div>
                </el-col>
                <el-col :span="4">
                    <div class="mainbav-title">关于</div>
                    <div class="mainbav-itemlist">
                        <li v-for="(item,index) in about" :key="index"><a class="mainbav-item" :href="item.link"><div class="mainbav-item">{{item.title}}</div></a></li>
                    </div>
                </el-col>
                <el-col :span="4">
                    <div class="mainbav-title">文章</div>
                    <div class="mainbav-itemlist">
                        <li v-for="(item,index) in article" :key="index"><a class="mainbav-item" :href="'/page?id=' + item.id"><div class="mainbav-item">{{item.title}}</div></a></li>
                        <li><a class="mainbav-item" href="/opus"><div class="mainbav-item">更多文章 》</div></a></li>
                    </div>
                </el-col>
                <el-col :span="4">
                    <div class="mainbav-title">更多</div>
                    <div class="mainbav-itemlist">
                        <li v-for="(item,index) in more" :key="index"><a class="mainbav-item" :href="item.link"><div class="mainbav-item">{{item.title}}</div></a></li>
                    </div>
                </el-col>
                <el-col :span="4">
                    <div class="mainbav-title">个人项目</div>
                    <div class="mainbav-itemlist">
                        <li v-for="(item,index) in project" :key="index"><a class="mainbav-item" :href="'/page?id=' + item.id"><div class="mainbav-item">{{item.title}}</div></a></li>
                        <li><a class="mainbav-item" href="/opus"><div class="mainbav-item">更多项目 》</div></a></li>
                    </div>
                </el-col>
                <el-col :span="4">
                    <div class="mainbav-title">联系方式</div>
                    <div class="mainbav-itemlist">
                        <li v-for="(item,index) in contact" :key="index"><a class="mainbav-item" :href="item.link"><div class="mainbav-item">{{item.title}}</div></a></li>
                    </div>
                </el-col>
            </el-row>
        </div>

        <div class="footer-introduce">
            <div class="l">该网站是WeiVi的个人主页 感谢你的访问 遇到什么问题可以通过以上方式联系我</div>
            <div class="r">© WeiVi 2014-2020</div>
            <div class="r">粤ICP备20033641号</div>
            <div class="r">网页插图来自网络</div>
        </div>

        </div>
    </div>
</template>

<script>
    export default {
        name:'Footer',
        data(){
            return{
                weivi:[
                    // {title:'个人荣誉', link:''},
                    {title:'自我介绍', link:'myintroduction'},
                    // {title:'招聘', link:''}
                ],
                about:[  
                    {title:'作品', link:'/opus'},
                    {title:'文章', link:'/article'},
                    {title:'项目', link:'/proj'}
                ],
                article:[
                ],
                more:[
                    {title:'BiliBili', link:'https://space.bilibili.com/4028423'},
                    {title:'Github', link:'https://github.com/weivis'},
                    // {title:'WeChat', link:''},
                    {title:'摄影作品', link:'/photo'}
                ],
                project:[
                ],
                contact:[
                    {title:'BiliBili私信', link:'https://space.bilibili.com/4028423'},
                    {title:'发送邮件到442981412@qq.com', link:'442981412@qq.com'}
                ],
            }
        },
        components: { //定义组件
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
            this.project = response.data.project;
            this.article = response.data.article;
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
.layout-footer {
    background-color: #fafafa;
    border-top: 1px solid #f4f4f4;
    height: 350px;
    .footer-mainbav{
        margin-top: 50px;width: 100%;height: 235px;
    }
    .mainbav-title{
        // width: 100%;
        font-size: 14px;
        font-weight: bold;
        color: #000;
    }
    .mainbav-itemlist{}
    .mainbav-item{
        font-size: 12px;font-weight: lighter;margin-top: 15px;color: #525252;
    }
    .footer-introduce{
        width: 100%;font-size: 12px;font-weight: inherit;line-height: 15px;
    }
    .l{float: left;margin-right: 15px;}
    .r{float: right;margin-left: 15px;}
}
</style>