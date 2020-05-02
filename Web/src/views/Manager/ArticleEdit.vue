<template>
  <div class="main">
    <div class="main-content width-normal">
      <div style="margin-top:30px">
        <el-upload
          class="content"
          drag
          action
          :http-request="upLoad"
          :show-file-list="false"
          multiple
        >
          <img v-if="loadcover" :src="loadcover" style="width:100%" />
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">
            将文件拖到此处，或
            <em>点击上传</em>
          </div>
          <!-- <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div> -->
        </el-upload>
        <span>标题</span>
        <el-input v-model="title" placeholder="标题" class="content"></el-input>
        <span>简介</span>
        <el-input v-model="introduce" placeholder="介绍" class="content"></el-input>
        <!-- <el-divider></el-divider> -->
        <span>内容</span>
        <editor v-model="content" :content="content" class="editor content" />
        <!-- <div class="content" v-html="content"></div> -->
        <el-row>
          <el-button type="primary" @click="seed()">确认修改</el-button>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script>
import editor from "../../components/Editor";
export default {
  name: "articleedit",
  components: {
    editor
  },
  data() {
    return {
      title: "",
      introduce: "",
      cover: "",
      content: "",
      loadcover: ""
    };
  },
  created() {
    this.$http
      .article_query(this.$route.query.id)
      .then(response => {
        if (response.code == 200) {
          this.title = response.data.title;
          this.content = response.data.content;
          this.introduce = response.data.introduce;
          this.cover = response.data.cover;
          this.loadcover = response.data.cover;
        }
      })
      .catch(error => {
        console.log("error", error);
      });
  },
  methods: {
    upLoad(file) {
      const formData = new FormData();
      formData.append("file", file.file);
      formData.append("uploadKey", "article_cover");

      console.log(file);
      this.$http.upload(formData).then(res => {
        console.log(res);
        console.log("上传成功");
        if (res.code === 200) {
          // console.log('res.data:',res.data)
          this.cover = res.data.ospath;
          this.loadcover = res.data.lodpath;
        }
      });
    },
    seed() {
      const seeddata = {
        id: this.$route.query.id,
        title: this.title,
        introduce: this.introduce,
        content: this.content,
        cover: this.cover
      };
      console.log(seeddata);
      this.$http.article_edit(seeddata).then(res => {
        console.log(res);
        console.log("上传成功");
        if (res.code === 200) {
          console.log("res.data:", res.data);
        }
      });
    }
  }
};
</script>

<style lang="scss" scoped>
.title {
  width: 100%;
  font-size: 24px;
  line-height: 24px;
  margin-top: 50px;
}
.introduce {
  color: #616161;
  font-size: 14px;
  width: 100%;
  overflow: hidden;
  margin-top: 10px;
}
.content {
  margin-bottom: 30px;
}
</style>