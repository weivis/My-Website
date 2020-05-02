<template>
  <div id="oldapp">
    <vue-editor v-model="strHtml" :disabled='!!disabled'></vue-editor>
    <!-- <el-button @click="add" useCustomImageHandler @imageAdded="handleImageAdded" /> -->
  </div>
  <!-- @imageAdded="handleImageAdded" -->
</template>
<script>
import { VueEditor } from "vue2-editor";
// import axios from "axios";
// import Common from "../Common"
export default {
  name: "Editor",
  props: ["content", "disabled"],
  data() {
    return {
      strHtml: ""
    };
  },
  components: { VueEditor },
  watch: {
    $attrs(val) {
      this.strHtml = val.value;
    },
    strHtml(newval) {
      //实时监控编辑器内容变化，使父组件能够实时获取输入内容
      this.$emit("input", newval);
    }
    // content(newval) {
    //   //父组件实时更新数据流向子组件
    //   this.strHtml = newval
    // }
  },
  methods: {
  }
};
</script>