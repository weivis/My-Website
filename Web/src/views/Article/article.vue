<template>

  <div class="main">
    <div class="main-content width-normal">
    <el-row :gutter="24">
      <el-col :span="12" v-for="(index, item) in list" :key="index">
        <div class="item">
          <div class="cover">
            <img :src="item.cover">
          </div>
          <div class="r">
            <div class="title">
              {{item.title}}
            </div>
            <div class="introduce">
              {{item.introduce}}
            </div>
          </div>
        </div>
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
      list:[]
    }
  },
  components: {
  }
}
</script>

<style lang="scss" scoped>
  .item{
    width: 100%;
    .cover{
      width: 230px;
      height: 120px;
      float: left;
    }
    .img{
      width: 100%;
    }
    .r{
      float: right;
      width: calc(100% - 230px);
    }
    .title{
      width: 100%;
    }
    .introduce{
      width: 100%;
    }
  }
</style>