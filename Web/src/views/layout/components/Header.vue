<template>
    <div class="layout-header">
        <div class="main-content width-normal header-content">
            <div class="content-libox">
                <a href="/">
                    <img class="logo" :src="this.COMMON.httpUrl + '/static/logo.png'">
                    <div class="comname">WeiVi dr</div>
                </a>
                <layout-lnav/>
                <layout-rnav/>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.layout-header{
    overflow: hidden;
    width: 100%;
    height: 60px;
}

.header-content{
    width: 100%;
    margin: 0 auto;
    height: 60px;
    margin-top: 17.5px;
    .content-libox{
        width: 100%;height: 25px;
    }
    .logo{
        float: left;
        height: 25px;
    }
    .comname{
        font-size: 16px;
        float: left;
        line-height: 25px;
        margin-left: 11px;
        font-weight:300;
    }
}
</style>

<script>
import Lnav from './Lnav.vue'
import Rnav from './Rnav.vue'
    export default {
        name:'Home',
        methods: { //事件处理器
        },
        components: { //定义组件
            'layout-lnav':Lnav,
            'layout-rnav':Rnav
        },
        created() { //生命周期函数

        }
    }
</script>