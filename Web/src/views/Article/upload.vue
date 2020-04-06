<template>

  <div class="main">
      <editor v-model="content" :content='this.oldcontent'/>
      <button @click="print">print</button>
      <button @click="pass2child">父级传递给子级</button>
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
      pass2child () {
        this.content = '父级传递给子级'
      },
      print(){
          console.log(this.content);  
      }
  },
  components: {
    editor
  }
}
</script>