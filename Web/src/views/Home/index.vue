<template>
  <transition
    name="fade-transform"
    mode="out-in"
  >
    <div class="home">
      <firstscreen/>
      <gutterlicard/>
      <myintroduce/>
      <dynamics/>
    </div>
  </transition>
</template>

<script>
import firstscreen from './FirstScreen.vue'
import gutterlicard from '../../components/GutterLiCard.vue'
import myintroduce from './MyIntroduce.vue'
import dynamics from './Dynamics.vue'
import {Message} from 'element-ui'
export default {
  name: 'Home',
  components: {
    firstscreen,
    gutterlicard,
    myintroduce,
    dynamics
  },
  created(){
    if (this.$route.params){
      if (this.$route.params.topage == 'login'){
        this.$forceUpdate()
        this.$router.go(0)
      }
      if (this.$route.params.msg){
        Message({
          message: this.$route.params.msg,
          type: 'error',
          duration: 5 * 1000
        })
      }
    }
  }
}
</script>

<style scoped>

</style>