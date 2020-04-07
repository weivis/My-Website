<template>

  <div class="main">
    <div class="nowmain main-content width-normal">

      <div class="ibox">
        <div class="lbox">
          <div class="input">
            <div class="inputcontentname">上传封面</div>
            <el-upload
              class="upload-demo"
              drag
              action=""
              :http-request="upLoad"
              :show-file-list="false"
              multiple>
              <img v-if="loadcover" :src="loadcover" style="width:100%">
              <i class="el-icon-upload"></i>
              <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
              <!-- <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div> -->
            </el-upload>
          </div>
        </div>

        <div class="rbox">

          <el-row :gutter="20">
            <el-col :span="4" class="min-w">
              <div class="input">
                <div class="inputcontentname">上传分类</div>
                <el-radio-group v-model="article_type">
                  <el-radio-button label="1">作品</el-radio-button>
                  <el-radio-button label="2">文章</el-radio-button>
                  <el-radio-button label="3">项目</el-radio-button>
                </el-radio-group>
              </div>
            </el-col>
            <el-col :span="4" class="min-w">

            <div class="input" v-if="article_type=='1'">
              <div class="inputcontentname">作品类型</div>
              <el-select v-model="content_type" placeholder="请选择">
                <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </div>
            </el-col>

            <el-col :span="4" class="min-w">
              <div class="input">
                <div class="inputcontentname">状态</div>
                <el-radio-group v-model="status">
                  <el-radio-button label="0">正常</el-radio-button>
                  <el-radio-button label="1">下架</el-radio-button>
                </el-radio-group>
              </div>
            </el-col>

          </el-row>

          <div class="input">
            <div class="inputcontentname">标题</div>
            <el-input v-model="title" placeholder="文章标题" class="inputs"></el-input>
          </div>

          <div class="input">
            <div class="inputcontentname">介绍</div>
            <el-input v-model="introduce" placeholder="文章标题" class="inputs"></el-input>
          </div>

        </div>
      </div>

      <div class="input">
        <div class="inputcontentname">文章内容</div>
        <editor v-model="content" :content='content' class="editor"/>
      </div>
    
    <!-- <button @click="print">print</button>
    <button @click="pass2child">父级传递给子级</button> -->
    <el-row>
      <el-button type="primary" @click="seed()">确认上传</el-button>
    </el-row>
    </div>
  </div>

</template>

<script>
import editor from '../../components/Editor'
export default {
  name: 'uploadarticle',
  data(){
      return{
        title:'',
        introduce:'',
        content : '',
        article_type: '',
        content_type:'',
        options: [{
          value: '1',
          label: '设计'
        }, {
          value: '2',
          label: '视频'
        }],
        value:'',
        cover:'',
        loadcover:'',
        status:''
      }
  },
  methods:{
    pass2child () {
      this.content = '父级传递给子级'
    },
    print(){
        console.log(this.content);  
    },
    upLoad(file) {
      const formData = new FormData();
      formData.append('file', file.file);
      formData.append('uploadKey', 'article_cover');

      console.log(file);
      this.$http.upload(formData).then((res) => {
        console.log(res);
        console.log('上传成功');
        if (res.code === 200) {
          // console.log('res.data:',res.data)
          this.cover = res.data.ospath;
          this.loadcover = res.data.lodpath;
        }
      });
    },
    seed(){
      const seeddata = {
        cover: this.cover,
        title: this.title,
        introduce: this.introduce,
        content: this.content,
        article_type: this.article_type,
        content_type: this.content_type,
        status: this.status
      }
      this.$http.upload_article(seeddata).then((res) => {
        console.log(res);
        console.log('上传成功');
        if (res.code === 200) {
          console.log('res.data:',res.data)
        }
      });
    }
  },
  components: {
    editor
  }
}
</script>

<style lang="scss" scoped>
.ibox{overflow: hidden;}
.lbox{float: left;width: 360px;}
.rbox{float: right;width: calc(100% - 390px);}
.min-w{min-width: 230px;}
.upload-demo{height: 280px;}
.nowmain{
  margin-top: 30px;
}
.input{
  margin-bottom: 20px;
  .inputcontentname{
    line-height: 30px;
    font-size: 14px;
    margin-bottom: 10px;
    color: #afafaf;
  }
  // .inputs{}
}

.editor{
  margin-top: 0px;
}
</style>