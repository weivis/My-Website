<template>
  <div class="GutterLiCard main-content width-normal">
    <div class="module-title">{{ title }}</div>

    <el-row :gutter="30">
      <div class="block" v-for="(item, index) in data" :key="index">
        <el-col :span="6">
          <router-link :to="item.link" v-if="item.line_type == 0">
            <div class="item-imgbox">
              <el-image class="item-img" :src="item.cover"></el-image>
            </div>
            <div class="item-title">{{ item.title }}</div>
            <div class="item-introduce">{{ item.introduce }}</div>
            <div class="item-linkbutt">了解更多 ></div>
          </router-link>
          <a :href="item.link" v-if="item.line_type == 1">
            <div class="item-imgbox">
              <el-image class="item-img" :src="item.cover"></el-image>
            </div>
            <div class="item-title">{{ item.title }}</div>
            <div class="item-introduce">{{ item.introduce }}</div>
            <div class="item-linkbutt">了解更多 ></div>
          </a>
        </el-col>
      </div>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "GutterLiCard",
  data() {
    return {
      title: "更多",
      data: []
    };
  },
  components: {},
  created() {
    this.query_list();
  },
  methods: {
    query_list(article_type) {
      this.$http
        .index_morelink_list({})
        .then(response => {
          if (response.code == 200) {
            this.data = response.data;
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
.GutterLiCard {
  .module-title {
    width: 100%;
    line-height: 70px;
    font-size: 24px;
    font-weight: bold;
    color: #000;
  }
  .item-box {
    max-width: 381px;
    min-width: 100%;
  }
  .item-imgbox {
    max-height: 213px;
    overflow: hidden;
    border-radius: 4px;
  }
  .item-img {
    width: 100%;
  }
  .item-title {
    margin-top: 40px;
    width: 100%;
    font-weight: bold;
    font-size: 18px;
    color: #000;
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
  }
  .item-introduce {
    margin-top: 8px;
    width: 100%;
    font-weight: lighter;
    font-size: 14px;
    color: #000;
    height: 35px;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .item-linkbutt {
    margin-top: 20px;
    font-weight: lighter;
    font-size: 14px;
    color: #f8005d;
  }
}
</style>