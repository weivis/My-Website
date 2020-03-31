<template>

  <div class="Main">
      <vue-particles
      color="#409EFF"
      :particleOpacity="0.7"
      :particlesNumber="60"
      shapeType="circle"
      :particleSize="4"
      linesColor="#409EFF"
      :linesWidth="1"
      :lineLinked="true"
      :lineOpacity="0.4"
      :linesDistance="150"
      :moveSpeed="2"
      :hoverEffect="true"
      hoverMode="grab"
      :clickEffect="true"
      clickMode="push"
      class="lizi"
    >
    </vue-particles>

  <div class="main-content width-normal">
  </div>
  </div>

</template>

<script>

export default {
  name: 'login',
  components: {
  }
}
</script>

<style>
  .app-main{
    margin-top: 0px !important;
  }
  .layout-header{
    position: initial !important;
    border-bottom: 0 !important;
    box-shadow: initial !important;
  }
</style>

<style scoped>
  .Main{}
</style>