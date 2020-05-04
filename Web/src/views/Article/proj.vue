<template>

  <div class="main">
    <div class="main-content width-normal">

          <div class="item" :span="12" v-for="(item, index) in list" :key="index">
            <div class="cover">
              <a :href="'/page?id=' + item.id" target="_blank">
                <img class="cover-img" :src="item.cover" >
              </a>
            </div>

            <div class="info">
              <div class="info-h">
                <a :href="'/page?id=' + item.id" target="_blank">
                  <div class="title">{{item.title}}</div>
                  <div class="introduce">{{item.introduce}}</div>
                </a>
              </div>
              <div class="bar">
                <a :href="'/page?id=' + item.id" target="_blank">
                <el-button type="primary">主要按钮</el-button>
                </a>
              </div>
            </div>
          </div>

    </div>
  </div>

</template>

<script>
export default {
  name: 'proj',
  data(){
    return{
      list:[
      ],
      queryPage:1
    }
  },
  created(){
    this.httpUrl = this.Common.httpUrl;
    this.$http.article_projlist(this.queryPage)
    .then(response => {
      if (response.code == 200){
        this.list = response.data.list
      }
    })
    .catch(error => {
      console.log("error", error);
    });
  },
  components: {
  }
}
</script>
<style lang="scss" scoped>
.main-content{
  margin-top: 30px;
  overflow: hidden;
}
.item{
  border-bottom: 1px solid #f4f4f4;
  overflow: hidden;
  .cover{
    width: 350px;height: 200px;overflow: hidden;
    float: left;
  }
  .cover-img{
    width: 100%;
  }
  .info{
    width: calc(100% - 400px);float: left;padding: 25px
  }
  .info-h{
    overflow: hidden;
    min-height: 135px;
  }
  .title{
    margin-top: 30px;
    font-size: 18px;color: #373737;font-weight: bold;width: 100%;
  }
  .introduce{
    font-size: 12px;color: #717171;width: 100%;margin-top: 15px;
  }
  .bar{
    width: 100%;height: 40px;
  }
}
</style>