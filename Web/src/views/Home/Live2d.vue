<template>
    <vue-live2d :modelPath="modelPath" :width="width" :height="height" :isScale="isScale" :isMove="isMove"></vue-live2d>
</template>
<script>
export default {
  name: 'app',
  data() {
    return {
      isScale:false,
      isMove:false,
      width:500,
      height:800,
      modelPath: [
        {
          order: 1,
          path: "/live2d/2.json",
        }
      ]
    }
  }
}
</script>
<style lang="scss" scoped>
  .live2d-wrap{
    z-index: 10;
    position: absolute;
    right: 15vh;
    left: inherit;
    top: -30px;
  }
</style>