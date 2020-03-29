<template>
  <div class="MyIntroduce">
    <div class="main-content width-normal">
      <div class="modulecontent-width">
        <div class="myinfobox">
          <div class="floadhead">
            <img class="floadhead-img" :src="this.Common.httpUrl + '/static/head.png'" />
          </div>
          <div class="myinforightbox">
            <div class="myinfo-myname">{{myname}}</div>
            <div class="myinfo-myintroduce">{{myintroduce}}</div>
          </div>
        </div>

        <div>
          <el-row :gutter="5">
            <el-col :span="8">
              <div class="list">

                <div class="list-page">
                  <div class="list-pagename">个人介绍</div>
                  <div class="list-pageitembox">
                    本人初一因校园暴力被欺负缀学, 凭自己努力自学各种技能, 很喜欢动漫因此学会了视频制作和平面设计, 也因此就业过, 后来为了开发自己的动漫网站等接触了程序这行, 如今在一家科技公司担任开发
                  </div>
                </div>

                <div class="list-page">
                  <div class="list-pagename">个人成就</div>
                  <div class="list-pageitembox">
                    <div class="list-item">
                      <el-row :gutter="20">

                        <div v-for="(item,index) in honour" :key="index">
                            <el-col :span="12">
                              <div class="list-imgitembox">

                                <div class="list-imgitemimgbox">
                                  <el-image class="list-imgitem-img" :src="item.url" fit='scale-down'/>
                                </div>
                                <div class="list-imgitem-title">{{item.title}}</div>
                                
                              </div>
                          </el-col>
                        </div>

                      </el-row>
                    </div>
                  </div>
                </div>

              </div>
            </el-col>
            <el-col :span="8">
              <div class="list">

                <div class="list-page">
                  <div class="list-pagename">个人荣誉</div>
                  <div class="list-pageitembox">
                    <div class="list-item">2018年全国大学生创新技术应用大赛获奖者</div>
                  </div>
                </div>

                <div class="list-page">
                  <div class="list-pagename">职业经验</div>
                  <div class="list-pageitembox">
                    <div class="list-item">淘宝美工设计</div>
                    <div class="list-item">影视后期制作</div>
                    <div class="list-item">动漫周边店店长</div>
                    <div class="list-item">视频制作团队运营和创始人</div>
                    <div class="list-item">淘宝电商工作室</div>
                    <div class="list-item">自主外包程序开发团队</div>
                    <div class="list-item">原创视频分享网站创始人及CEO</div>
                    <div class="list-item">后端开发工程师</div>
                  </div>
                </div>

              </div>
            </el-col>
            <el-col :span="8">
              <div class="list">

                <div class="list-page">
                  <div class="list-pagename">技能</div>
                  <div class="list-pageitembox">
                    <div class="list-item">UE UI 设计</div>
                    <div class="list-item">电商运营 天猫淘宝店装修</div>
                    <div class="list-item">MG动画设计 3D动画 建模</div>
                    <div class="list-item">WEB前端开发 小程序开发</div>
                    <div class="list-item">服务器后端开发</div>
                  </div>
                </div>

                <div class="list-page">
                  <div class="list-pagename">熟练技术和软件</div>
                  <div class="list-pageitembox">
                    <div class="list-item">PS AE AxureRP Ai </div>
                    <div class="list-item">Maya C4D</div>
                    <div class="list-item">Python Node Javascripts</div>
                    <div class="list-item">HTML5 VUE2-3 CSS3 NW.js Element</div>
                    <div class="list-item">Mysql Elasticsearch MariaDB MongDB</div>
                    <div class="list-item">Scrapy Redis Tornado Django Flask</div>
                  </div>
                </div>

              </div>
            </el-col>
          </el-row>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "myintroduce",
  data() {
    return {
        myname:'WeiVi',
        myintroduce:'男 出生于 1999/04/19 最高学历 初一 - 兴趣 : 羽毛球 公路车骑行 音乐 烹饪 摄影 禅茶',
        honour:[
          {
            title:'尼噗动漫视频网创始人',
            url:"http://127.0.0.1:8080/static/il1.png"
          },
          {
            title:'外管境外旅客护照信息提交系统开发组长',
            url:"http://127.0.0.1:8080/static/il2.png"
          },
          {
            title:'可识别全球护照的OCR核心研发者(投入使用中)',
            url:"http://127.0.0.1:8080/static/il3.png"
          },
          {
            title:'Yami!~动漫周边店创始人',
            url:"http://127.0.0.1:8080/static/il4.png"
          }
        ]
    };
  }
};
</script>

<style lang="scss" scoped>
.MyIntroduce {
  margin-top: 130px;
  width: 100%;
  height: 715px;
  background-color: #fafafa;
  border-top: 1px solid #f4f4f4;
  border-bottom: 1px solid #f4f4f4;
  .modulecontent-width{
    width: calc(100% - 100px);
    margin: 0 auto;
  }
  .myinfobox {
    height: 150px;
    width: 100%;
  }
  .myinforightbox {
    width: 50%;
    float: left;
    margin-left: 30px;
    height: 150px;
  }
  .myinfo-myname {
    font-size: 24px;
    width: 100%;
    margin-top: 50px;
    height: 24px;
  }
  .myinfo-myintroduce {
    font-size: 14px;
    width: 100%;
    margin-top: 10px;
    height: 14px;
  }
  .floadhead {
    height: 150px;
    width: 150px;
    margin-top: -30px;
    float: left;
    border-radius: 4px
  }
  .floadhead-img {
    width: 100%;
  }
  .list{
    width: 100%;
    min-height: 400px;
    border-left: 1px solid #f4f4f4;
    margin-top: 35px;
  }
  .list-page{
    margin-left: 15px;
    width: 95%;
    margin-top: 10px;
    border-bottom: 1px solid #f4f4f4;
  }
  .list-imgitembox{
    border:1px solid #f4f4f4;
    min-height: 120px;
    margin-bottom: 15px;
  }
  .list-imgitemimgbox{
    height: 50px;
    width: 100%;
  }
  .list-imgitem-img{
    width: 100%;
    height: 100%;
    padding-top: 10px;
  }
  .list-imgitem-title{
    padding: 10px;text-align: center;font-size: 12px;
  }
  .list-pagename{
    font-size: 14px;
    height: 50px;
    line-height: 50px;
    color: #848484;
  }
  .list-pageitembox{
    width: 80%;
    margin-left: 15px;
    margin-bottom: 30px;
    font-size: 14px;
  }
  .list-item{
    width: 100%;
    font-size: 14px;
    margin-bottom: 10px;
  }
}
</style>