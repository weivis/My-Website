<template>

  <div class="home">
    <firstscreen/>
    <gutterlicard/>
    <myintroduce/>
  </div>

</template>

<script>
import firstscreen from './FirstScreen.vue'
import gutterlicard from '../../components/GutterLiCard.vue'
import myintroduce from './MyIntroduce.vue'

export default {
  name: 'Home',
  components: {
    firstscreen,
    gutterlicard,
    myintroduce
  }
}
</script>

<style scoped>

</style>