<template>
  <div id="app">
    <img id="header_image" src="./assets/header_image.jpg">
    <nav id="top_navbar" class="navbar navbar-expand-md">
      <div class="container-fluid">
        <a href="/" class="text-decoration-none">
          <img alt="VCR Logo" src="./assets/vcr_img.png" class="logo_img">
          <!-- <a id="service_name" class="navbar-brand align-middle" href="#">SOME LIKE IT 90'S</a> -->
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-md-0">
            <li class="nav-item">
              <a class="nav-link active align-middle" aria-current="page" href="#">
                <router-link :to="{ name: 'MovieListView'}" class="app_nav fs-5 text-decoration-none">Movie</router-link>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link active align-middle" aria-current="page" href="#">
                <router-link :to="{ name: 'ArticleView' }" class="app_nav fs-5 text-decoration-none">Community</router-link>
              </a>
            </li>
          </ul>
          <div class="d-flex" >
            <div v-if="isLogin">
              <router-link :to="{ name: 'MyProfileView' }" class="app_nav text-decoration-none">
                {{ currentUser.username }}
              </router-link>
              님 안녕하세요. 
              <button id="logout_btn" @click="logout" class="btn">로그아웃</button>
              </div>
              <div v-else>
                로그인되지 않았습니다.
                <button id="login_btn" @click="goToLogInPage" class="btn">로그인</button> | 
                <button id="join_btn" @click="goToSignUpPage" class="btn">회원가입</button> 
            </div>
            <!-- <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button> -->
          </div>
        </div>
      </div>
    </nav>
    <router-view/>
    <div id="footer">
      SSAFY pjt Website created by 정진욱, 안대현
    </div>
  </div>
</template>


<script>
export default {
  computed: {
    isLogin() {
      return this.$store.getters.isLogin; // 로그인 여부 확인
    },
    currentUser() {
      return this.$store.getters.currentUser; // 사용자 이름 가져오기
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
    },
    goToSignUpPage() {
      if (this.$route.name !== 'SignUpView') {
        this.$router.push({ name: 'SignUpView' });
      }
    },
    goToLogInPage() {
      if (this.$route.name !== 'LogInView') {
        this.$router.push({ name: 'LogInView' });
      }
    },
  }
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #bfbfbf;
  background-image: url("/src/assets/blue-gradient.jpg");
  background-repeat: repeat-y;
  font-family: 'DungGeunMo';
}
#header_image{
  width : 100%;
}
#service_name{
  color: #bfbfbf
}

#logout_btn{
  background-color: #261639;
  border: solid 1px #ff2679;
  color: #ff2679;
  /* font-weight: bold; */
}
#logout_btn:hover{
  background-color: #352c41;;
  color: #ff9ec3;
}
#login_btn{
  background-color: #261639;
  border: solid 1px #ff2679;
  color: #ff2679;
  /* font-weight: bold; */
}
#login_btn:hover{
  background-color: #352c41;;
  color: #ff9ec3;
}
#join_btn{
  background-color: #261639;
  border: solid 1px #ff2679;
  color: #ff2679;
  /* font-weight: bold; */
}
#join_btn:hover{
  background-color: #352c41;;
  color: #ff9ec3;
}

.logo_img{
  height: 50px;
}

#top_navbar {
  background-color: #261639;
}

.app_nav{
  color: #ff2679
}
.app_nav:hover{
  color: #ff9ec3;
}

.navbar-toggler{
  color:#ff2679;
  border: solid 1px 	#bfbfbf;
}
.navbar-toggler:focus{
  box-shadow: none;
}
.navbar-toggler-icon{
  background-image: url('/src/assets/hamburg_icon.png');
}

.title-mg-ct {
  margin-top: 5px;
  margin-bottom: 0px;
  color: #ff2679;
}
#footer{
  background-color: #261639;
  padding-top: 8px;
  padding-bottom: 8px;
  font-family: 'DungGeunMo' ;
}

@font-face{
  font-family : 'DungGeunMo';
  src: url('./assets/DungGeunMo.ttf') format('woff');
  font-weight: 400;
}
</style>
