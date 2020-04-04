<template>

  <div class="main">
    <div class="main-content width-normal">

      <div class="App-content">
        <div class="List">
          <div class="title">设计作品</div>
          <div class="content" >
            <el-row :gutter="25">

              <el-col :span="6" v-for="(item, index) in desgin" :key="index">
                <div class="for-item">
                  <el-link :href="item.url" target="_blank" :underline="false">
                    <div class="item-cover">
                      <el-image class="list-imgitem-img" :src="item.img" fit='scale-down'/>
                    </div>
                    <div class="item-title">
                      <span>{{item.title}}</span>
                      <el-divider direction="vertical"></el-divider>
                      <span>{{item.introduce}}</span>
                    </div>
                  </el-link>
                </div>
              </el-col>

            </el-row>
          </div>
        </div>
      </div>

    </div>
  </div>

</template>

<script>
export default {
  name: 'Opus',
  data(){
    return{
      desgin:[
        {img:'http://127.0.0.1:8080/static/project/cover.png', title:'尼噗云', introduce:'基于模板的视频生成平台', link:''},
        {img:'http://127.0.0.1:8080/static/project/cover.png', title:'尼噗云', introduce:'基于模板的视频生成平台', link:''},
        {img:'http://127.0.0.1:8080/static/project/cover.png', title:'尼噗云', introduce:'基于模板的视频生成平台', link:''},
        {img:'http://127.0.0.1:8080/static/project/cover.png', title:'尼噗云', introduce:'基于模板的视频生成平台', link:''},
        {img:'http://127.0.0.1:8080/static/project/cover.png', title:'尼噗云', introduce:'基于模板的视频生成平台', link:''}
      ]
    }
  }
}
</script>
<style lang="scss" scoped>

  .App-content{
    // margin-top: 30px;
  }

  .List{
    width: 100%;
    .title{
      line-height: 60px;
      height: 60px;
      font-size: 16px;
      font-weight: bold;
    }
    .content{
      width: 100%;
    }
    .for-item{
      margin-bottom: 40px;
      width:100%;
      overflow: hidden;
    }
    .item-cover{
      width: 100%;
    }
    .item-title{font-size: 14px;line-height: 30px;}
  }

</style>