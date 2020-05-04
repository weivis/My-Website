<template>
  <div class="main">
    <div class="nowmain main-content width-normal">
      <el-button @click="drawer = true" type="primary">新增</el-button>
      <el-drawer :visible.sync="drawer" :before-close="handleClose" :with-header="false">
        <div style="padding: 35px">
          <el-radio-group v-model="addnewlinktype" style="margin-bottom:35px">
            <el-radio-button label="1">站内文章</el-radio-button>
            <el-radio-button label="2">站外地址</el-radio-button>
          </el-radio-group>
          <div v-if="addnewlinktype == 2">
            <span>封面</span>
            <el-upload drag action :http-request="upLoad" :show-file-list="false" multiple>
              <img v-if="loadcover" :src="loadcover" style="width:100%" />
              <i class="el-icon-upload"></i>
              <div class="el-upload__text">
                将文件拖到此处，或
                <em>点击上传</em>
              </div>
            </el-upload>
            <span>标题</span>
            <el-input v-model="newadd_title" placeholder="标题"></el-input>
            <span>介绍</span>
            <el-input v-model="newadd_introduce" placeholder="介绍"></el-input>
            <span>链接地址</span>
            <el-input v-model="newadd_link" placeholder="链接地址"></el-input>
          </div>

          <div v-if="addnewlinktype == 1">
            <span>文章id</span>
            <el-input v-model="newadd_article" placeholder="文章id"></el-input>
          </div>

          <el-button type="primary" round @click="addlink()" style="margin-top:35px">提交</el-button>
        </div>
      </el-drawer>
      <transition name="fade-transform" mode="out-in">
        <el-table :data="tableData" style="width: 100%;margin-top:30px">
          <el-table-column label="标题" width="250">
            <template slot-scope="scope">
              <span>{{ scope.row.title }}</span>
            </template>
          </el-table-column>
          <el-table-column label="介绍" width="450">
            <template slot-scope="scope">
              <span>{{ scope.row.introduce }}</span>
            </template>
          </el-table-column>
          <el-table-column label="地址" width="450">
            <template slot-scope="scope">
              <span>{{ scope.row.link }}</span>
            </template>
          </el-table-column>
          <el-table-column label="链接类型" width="100" align="right">
            <template slot-scope="scope">
              <span v-if="scope.row.line_type == 0">站内文章</span>
              <span v-if="scope.row.line_type == 1">站外链接</span>
            </template>
          </el-table-column>
          <el-table-column label="权重" width="100" align="right">
            <template slot-scope="scope">
              <span>{{ scope.row.sort }}</span>
            </template>
          </el-table-column>
          <el-table-column label="操作" align="right">
            <template slot-scope="scope">
              <el-button size="mini" @click="change(scope.row.id, 1, null)" v-if="scope.row.status == 0">显示</el-button>
              <el-button size="mini" @click="change(scope.row.id, 2, null)" v-if="scope.row.status == 1">隐藏</el-button>
              <el-button size="mini" @click="changesort(scope.row.id)">权重</el-button>
              <el-button size="mini" @click="change(scope.row.id, 3, null)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  name: "recommendlist",
  data() {
    return {
      tableData: [],
      drawer: false,
      addnewlinktype: 1,
      loadcover: "",
      newadd_cover: "",
      newadd_title: "",
      newadd_introduce: "",
      newadd_link: "",
      newadd_article: ""
    };
  },
  created() {
    this.query_list();
  },
  methods: {
    changesort(id) {
      this.$prompt("权重", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        inputPattern: /[0-9]/,
        inputErrorMessage: "输入有误"
      })
        .then(({ value }) => {

          this.change(
            id,4,value
          )
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
    handleClose(done) {
      this.$confirm("确认关闭？")
        .then(_ => {
          done();
        })
        .catch(_ => {});
    },
    change(id, types, sort) {
      this.$http
        .index_morelink_change(id, types, sort)
        .then(response => {
          if (response.code == 200) {
            this.query_list();
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    addlink() {
      console.log(
        this.newadd_cover,
        this.newadd_title,
        this.newadd_introduce,
        this.newadd_link
      );
      console.log(this.newadd_article);
      this.$http
        .index_morelink_add(
          this.newadd_article,
          this.newadd_title,
          this.newadd_cover,
          this.newadd_introduce,
          this.newadd_link
        )
        .then(response => {
          if (response.code == 200) {
            this.drawer = false
            this.query_list();
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    query_list(article_type) {
      this.$http
        .index_morelink_list({
          admin:'admin'
        })
        .then(response => {
          if (response.code == 200) {
            this.tableData = response.data;
          }
        })
        .catch(error => {
          console.log("error", error);
        });
    },
    upLoad(file) {
      const formData = new FormData();
      formData.append("file", file.file);
      formData.append("uploadKey", "link");

      console.log(file);
      this.$http.upload(formData).then(res => {
        console.log(res);
        console.log("上传成功");
        if (res.code === 200) {
          // console.log('res.data:',res.data)
          this.newadd_cover = res.data.ospath;
          this.loadcover = res.data.lodpath;
        }
      });
    }
  }
};
</script>

<style lang="scss" scoped>
.main-content {
  margin-top: 30px;
}
</style>