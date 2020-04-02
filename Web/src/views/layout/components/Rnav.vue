<template>
    <div class="R-Nav">
        <ul>
            <li v-for="(item,index) in nav" :key="index">
                <a :href="item.link" target="_blank">{{ item.title }}</a>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        data() {
            return{
                nav:this.Common.R_Nav
            }
        },
        name:'Rnav'
    }
</script>

<style lang="scss" scoped>
.R-Nav{
    height: 25px;
    float: right;
    ul{float: right;height: 25px;margin: 0;padding: 0;}
    li{float: right;list-style-type:none;line-height: 25px;margin-left: 25px;}
    a{text-decoration:none;font-size: 13px;color: #525252;}
}
</style>