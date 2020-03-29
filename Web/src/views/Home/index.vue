<template>

  <div class="home">
    <firstscreen/>
    <gutterlicard/>
    <myintroduce/>
    <dynamics/>
  </div>

</template>

<script>
import firstscreen from './FirstScreen.vue'
import gutterlicard from '../../components/GutterLiCard.vue'
import myintroduce from './MyIntroduce.vue'
import dynamics from './Dynamics.vue'

export default {
  name: 'Home',
  components: {
    firstscreen,
    gutterlicard,
    myintroduce,
    dynamics
  }
}
</script>

<style scoped>

</style>