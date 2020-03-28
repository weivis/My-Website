<template>

  <div class="GutterLiCard main-content width-normal">

      <div class="module-title">
          {{ title }}
      </div>

    <el-row :gutter="30">
        <div class="block" v-for="fit in data" :key="fit">
            <el-col :span="6">
                <a :href="fit.link">
                    <div class="item-imgbox">
                        <el-image class="item-img" :src="fit.img"></el-image>
                    </div>
                    <div class="item-title">{{ fit.title }}</div>
                    <div class="item-introduce">{{ fit.introduce }}</div>
                    <div class="item-linkbutt">了解更多 ></div>
                </a>
            </el-col>
        </div>
    </el-row>
  </div>

</template>

<script>

export default {
  name: 'GutterLiCard',
  data(){
      return{
          title:'更多',
          data:[
              {
                  img:'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
                  title:'标题1标题1标题1标题1标题1标题1标题1标题1',
                  introduce:'标题标题标题标题标题标题标题标题标题标题标题标题标题标题标题标题标题标题标题标题标题标题标题标题',
                  link:''
              },
              {
                  img:'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
                  title:'标题2',
                  introduce:'标题标题标题',
                  link:''
              },
              {
                  img:'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
                  title:'标题3',
                  introduce:'标题标题标题',
                  link:''
              },
              {
                  img:'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
                  title:'标题4',
                  introduce:'标题标题标题',
                  link:''
              }
          ]
      }
  },
  components: {
  }
}
</script>

<style lang="scss" scoped>
.GutterLiCard{
    .module-title{
        width: 100%;line-height: 70px;font-size: 24px;font-weight: bold;color: #000;
    }
    .item-box{
        max-width:381px;min-width:100%;  
    }
    .item-imgbox{
        max-height: 213px;overflow: hidden;
    }
    .item-img{
        width:100%
    }
    .item-title{
        margin-top: 40px;width: 100%;font-weight: bold;font-size: 18px;color: #000;white-space: nowrap;text-overflow:ellipsis;overflow: hidden;
        }
    .item-introduce{
        margin-top: 8px;width: 100%; font-weight: lighter; font-size: 14px;color: #000;height: 35px;overflow: hidden;text-overflow:ellipsis;
    }
    .item-linkbutt{
        margin-top: 20px; font-weight: lighter; font-size: 14px; color: #f8005d;
    }
}
</style>