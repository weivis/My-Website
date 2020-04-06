<template>
    <vue2-editor v-model="strHtml" @imageAdded="handleImageAdded" :disabled='!!disabled'></vue2-editor>
</template>
<script>
  import { VueEditor } from 'vue2-editor'
  import axios from "axios";
  import Common from "../Common"
  export default {
    name: 'Editor',
    props: ['content','disabled'],
    data() {
      return {
        strHtml: '',
      }
    },
    components: {
      'vue2-editor': VueEditor
    },
    watch: {
      strHtml (newval) {
        //实时监控编辑器内容变化，使父组件能够实时获取输入内容
        this.$emit('input', newval);
      },
      // content(newval) {
      //   //父组件实时更新数据流向子组件
      //   this.strHtml = newval
      // }
    },
    methods:{
      handleImageAdded(file, Editor, cursorLocation, resetUploader) {
      var formData = new FormData();
      formData.append("image", file);

      axios({
        url: Common.httpUrl + "/upload/file",
        method: "POST",
        data: [formData]
      })
        .then(result => {
          let url = result.data.url; // Get url from response
          Editor.insertEmbed(cursorLocation, "image", url);
          resetUploader();
        })
        .catch(err => {
          console.log(err);
        });
      }
    },
  }
</script>
