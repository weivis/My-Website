<template>

  <div class="main">
      <editor v-model="content" :content='this.oldcontent'/>
      <button @click="print">print</button>
  </div>

</template>

<script>
import editor from '../../components/Editor'
export default {
  name: 'uploadarticle',
  data(){
      return{
        oldcontent: 'asdasdsa',
        content : '1023132132'
      }
  },
  methods:{
      print(){
          console.log(this.content);  
      }
  },
  components: {
    editor
  }
}
</script>