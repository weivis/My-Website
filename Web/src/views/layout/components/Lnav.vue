<template>
    <div class="Nav">
        <ul>
            <li v-for="(item,index) in nav" :key="index">
                <router-link :to="item.link">{{ item.title }}</router-link>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        data() {
            return{
                nav:this.Common.L_Nav
            }
        },
        name:'Lnav'
    }
</script>

<style lang="scss" scoped>
.Nav{
    height: 25px;
    float: left;
    ul{float: left;height: 25px;margin: 0;padding: 0;}
    li{float: left;list-style-type:none;line-height: 25px;margin-left: 25px;}
    a{text-decoration:none;font-size: 13px;color: #525252;}
}
</style>