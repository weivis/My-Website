<script type="text/javascript">
    // 定义一些公共的属性和方法
    const httpUrl = 'http://127.0.0.1:8080'

    const L_Nav = [
                    {link:'/works',title:'作品'},
                    {link:'/',title:'文章'},
                    {link:'/',title:'项目'}
                ]

    const R_Nav = [
                    {link:'/',title:'Movie'},
                    {link:'/',title:'摄影作品'},
                    {link:'/',title:'Github'}
                ]

    function commonFun() {
        console.log("公共方法")
    }
    // 暴露出这些属性和方法
    export default {
        httpUrl,
        L_Nav,
        R_Nav,
        commonFun
    }
</script>