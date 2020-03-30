<script type="text/javascript">
    import Cookies from 'js-cookie'

    const LoginTokenID = 'LoginToken'

    function AuthUser() {
        // 如果 AuthUser为空 表示用户未登录
        return Cookies.get(LoginTokenID)
    }

    function Login_user(token) {
        // 用户登录 Login_user(usertoken)
        return Cookies.set(LoginTokenID, token)
    }

    function Logout_user() {
        // 取消登录 Logout_user
        return Cookies.remove(LoginTokenID)
    }

    // 暴露出这些属性和方法
    export default {
        AuthUser,
        Login_user,
        Logout_user,
        LoginTokenID
    }
</script>