<template>

  <div class="main">
    <div class="main-content width-normal">
      <el-row :gutter="20">
        <el-col :span="12" v-for="(item, index) in list" :key="index">
          <div class="item">

            <div class="cover">
              <a :href="'/page?id=' + item.id" target="_blank">
                <img class="cover-img" :src="item.cover" >
              </a>
            </div>

            <div class="info">
              <a :href="'/page?id=' + item.id" target="_blank">
                <div class="title">{{item.title}}</div>
                <div class="introduce">{{item.introduce}}</div>
              </a>
            </div>

          </div>
          </el-link>
        </el-col>
      </el-row>
    </div>
  </div>

</template>

<script>

export default {
  name: 'Article',
  data(){
    return{
      list:[
      ],
      queryPage:1
    }
  },
  created(){
    this.httpUrl = this.Common.httpUrl;
    this.$http.article_articlelist(this.queryPage)
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
  .main-content{margin-top: 20px;}
  .item{
    width: 100%;
    border: 1px solid #e1e1e1;
    height: 130px;
    .info{
      width: calc(100% - 260px);
      height: 100%;
      float: right;
      padding: 15px;
    }
    .title{
      width: 100%;
      color: #282828;
      font-size: 14px;
    }
    .introduce{
      width: 100%;
      font-size: 12px;
      margin-top: 5px;
      color: #9b9b9b;
    }
    .cover{
      float: left;
      width: 230px;
      height: 130px;
      overflow: hidden;
    }
    .cover-img{
      width: 100%;
    }
  }
</style>