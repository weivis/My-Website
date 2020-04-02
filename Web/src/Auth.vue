<script type="text/javascript">
    import Cookies from 'js-cookie'

    const LoginTokenID = 'LoginToken'
    const UserID = 'userID'
    const UserType = 'UserType'

    function AuthUser() {
        // 如果 AuthUser为空 表示用户未登录
        console.log('>Auth: 获取用户登录状态')
        return Cookies.get(LoginTokenID)
    }

    function isAdmin() {
        if (Cookies.get(UserType) == 1){
            return true
        }
        return false
    }

    function AuthUserData() {
        // 获取用户的登录数据
        console.log('>Auth: 获取用户登录缓存参数')
        return {
            token:Cookies.get(LoginTokenID),
            userid:Cookies.get(UserID),
            usertype:Cookies.get(UserType),
        }
    }

    function Login_user(token, userid, usertype) {
        console.log('>Auth: 设置用户缓存参数')
        // 用户登录 Login_user(usertoken)
        Cookies.set(LoginTokenID, token)
        Cookies.set(UserID, userid)
        Cookies.set(UserType, usertype)
        return
    }

    function Logout_user() {
        console.log('>Auth: 清空用户缓存参数')
        // 取消登录 Logout_user
        Cookies.remove(LoginTokenID)
        Cookies.remove(UserID)
        Cookies.remove(UserType)
        return
    }

    // 暴露出这些属性和方法
    export default {
        AuthUser,
        Login_user,
        Logout_user,
        LoginTokenID,
        AuthUserData,
        isAdmin
    }
</script>