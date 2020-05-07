<script type="text/javascript">
    // 定义一些公共的属性和方法
    const httpUrl = 'http://www.weivird.com/'
    const LoginUrl = '/auth/sign-in'
    const RegisterUrl = '/auth/register'
    const commonlink = {
        bilibili:'https://space.bilibili.com/4028423',
        github:'https://github.com/weivis'
    }
    const L_Nav = [
                    {link:'/opus',title:'作品'},
                    {link:'/article',title:'文章'},
                    {link:'/proj',title:'项目'},
                    {link:'/photo',title:'摄影作品'}
                ]

    const R_Nav = [
                    {link:commonlink.bilibili,title:'Movie'},
                    {link:commonlink.github,title:'Github'}
                ]

    // function commonFun() {
    //     console.log("公共方法")
    // }
    // 暴露出这些属性和方法
    export default {
        LoginUrl,RegisterUrl,
        httpUrl,
        L_Nav,
        R_Nav
        // commonFun
    }
</script>