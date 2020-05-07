<template>
  <div class="main">
    <div class="nowmain main-content width-normal">
      <el-row>
        <el-button @click="query_list(1)">作品</el-button>
        <el-button @click="query_list(2)">文章</el-button>
        <el-button @click="query_list(3)">项目</el-button>
        <el-button @click="query_list(4)">回收站</el-button>
      </el-row>
          <transition
      name="fade-transform"
      mode="out-in"
    >
      <el-table :data="tableData" style="width: 100%">
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
        <el-table-column label="作品类型" width="100" v-if="opus == 1">
          <template slot-scope="scope">
            <span v-if="scope.row.content_type == 1">设计</span>
            <span v-if="scope.row.content_type == 2">视频</span>
          </template>
        </el-table-column>
        <el-table-column label="首页展示" align="right" v-if="opus != 4">
          <template slot-scope="scope">
            <el-button size="danger" @click="change(scope.$index, scope.row, 6)" v-if="scope.row.index == true">取消</el-button>
            <el-button @click="change(scope.$index, scope.row, 5)" v-if="scope.row.index == false">展示</el-button>
          </template>
        </el-table-column>
        <el-table-column label="操作" align="right">
          <template slot-scope="scope">
            <el-button size="mini"><a :href="'/article-edit?id=' + scope.row.id">编辑</a></el-button>
            <el-button size="mini" @click="change(scope.$index, scope.row, 2)" v-if="scope.row.status == 0 && scope.row.is_delete == 0" type="success">下架</el-button>
            <el-button size="mini" @click="change(scope.$index, scope.row, 1)" v-if="scope.row.status == 1 && scope.row.is_delete == 0" type="info">上架</el-button>
            <el-button size="mini" type="danger" @click="change(scope.$index, scope.row, 3)" v-if="scope.row.is_delete == 0">删除</el-button>
            <el-button size="mini" type="danger" @click="change(scope.$index, scope.row, 4)" v-if="scope.row.is_delete == 1">恢复</el-button>
          </template>
        </el-table-column>
      </el-table>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  name: "articlelist",
  data() {
    return {
      tableData: [
      ],
      opus:1
    };
  },
  created(){
    this.query_list(1,1)
  },
  methods: {
    change(index, row, changetype) {
      console.log(index, row, changetype);
      this.$http.admin_change_articlestatus(row.id, changetype)
      .then(response => {
        if (response.code == 200){
          this.query_list(this.opus)
        }
      })
      .catch(error => {
        console.log("error", error);
      });
    },
    query_list(article_type){
      this.opus = article_type
      this.$http.query_article(article_type, null, 1)
      .then(response => {
        if (response.code == 200){
          this.tableData = response.data.list
        }
      })
      .catch(error => {
        console.log("error", error);
      });
    }
  }
};
</script>

<style lang="scss" scoped>
.main-content{margin-top: 30px;}
</style>