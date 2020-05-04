<template>
  <div class="bodyssss">
    <div class="main main-content width-normal">
      <el-drawer :visible.sync="drawer" :with-header="false">
        <div style="padding: 35px">
          <span>图片</span>
          <el-upload drag action :http-request="upLoad" :show-file-list="false" multiple>
            <img v-if="loadcover" :src="loadcover" style="width:100%" />
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">
              将文件拖到此处，或
              <em>点击上传</em>
            </div>
          </el-upload>
          <span>作品名</span>
          <el-input v-model="newphoto_title" placeholder="作品名"></el-input>
          <el-button type="primary" round @click="addlink()" style="margin-top:35px">提交</el-button>
        </div>
      </el-drawer>

      <el-dialog :visible.sync="DialogVisible" center>
        <div v-if="this.isAdmin()" style="margin-bottom:20px">
          <el-button @click="delphoto()" type="primary">删除该图片</el-button>
          <el-button @click="changesort()" type="primary">更改权重</el-button>
          当前权重: {{nowopensort}}
        </div>
        <div class="line">
          <img :src="bigImg" style="width: 100%" />
        </div>
      </el-dialog>

      <div v-if="this.isAdmin()" style="margin-bottom:20px">
        <el-button @click="drawer = true" type="primary">新增</el-button>
      </div>

      <el-row :gutter="20">
        <el-col
          :xs="24"
          :sm="12"
          :md="8"
          :lg="8"
          :xl="6"
          style="float:left"
          v-for="(item, index) in list"
          :key="index"
          class="forbox"
        >
          <el-image
            :src="item.link"
            fit="fill"
            style="width: 100%;"
            class="img"
            @click="showImg(item.link, item.id, item.sort)"
          ></el-image>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
export default {
  name: "photo",
  components: {},
  data() {
    return {
      list: [],
      bigImg: "",
      newuplaodphoto: "",
      loadcover: "",
      DialogVisible: false,
      drawer: false,
      newphoto_title: "",
      nowopenid: "",
      nowopensort: ""
    };
  },
  created() {
    this.query_list();
  },
  methods: {
    delphoto(){
      this.change(this.nowopenid,1,null)
    },
    changesort() {
      this.$prompt("权重", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        inputPattern: /[0-9]/,
        inputErrorMessage: "输入有误"
      })
        .then(({ value }) => {
          console.log(value)
          this.change(this.nowopenid, 2, value);
          this.$message({
            type: "success",
            message: "权重: " + value
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "取消输入"
          });
        });
    },
    change(id, types, sort) {
      this.$http
        .photo_change(id, types, sort)
        .then(response => {
          if (response.code == 200) {
            this.query_list();
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    query_list(article_type) {
      this.$http
        .photo_list()
        .then(response => {
          if (response.code == 200) {
            this.list = response.data;
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    addlink() {
      this.$http
        .photo_add(this.newuplaodphoto, this.newphoto_title)
        .then(response => {
          if (response.code == 200) {
            this.drawer = false;
            this.query_list();
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    showImg(img, id, sort) {
      this.DialogVisible = true;
      this.bigImg = img;
      this.nowopenid = id;
      this.nowopensort = sort;
    },
    upLoad(file) {
      const formData = new FormData();
      formData.append("file", file.file);
      formData.append("uploadKey", "photo");

      console.log(file);
      this.$http.upload(formData).then(res => {
        console.log(res);
        console.log("上传成功");
        if (res.code === 200) {
          // console.log('res.data:',res.data)
          this.newuplaodphoto = res.data.ospath;
          this.loadcover = res.data.lodpath;
        }
      });
    }
  }
};
</script>

<style lang="scss" scoped>
.bodyssss {
  min-height: calc(100vh - 50px);
  height: 100%;
  overflow: hidden;
  background-color: #232323 !important;
}
.main {
  margin-top: 20px;
}
.forbox {
  margin-bottom: 20px;
  height: 250px;
  overflow: hidden;
}
.img {
  width: 100%;
}
</style>