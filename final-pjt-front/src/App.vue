<template>
  <div id="app">
    <img id="header_image" src="./assets/header_image.jpg">
    <nav id="top_navbar" class="navbar navbar-expand-md">
      <div class="container-fluid">
        <a href="" class="text-decoration-none fw-bold">
          <img alt="VCR Logo" src="./assets/vcr.png" class="logo_img">
          <a id="service_name" class="navbar-brand" href="#">SOME LIKE IT 90'S</a>
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">
                <router-link :to="{ name: 'MovieListView'}" class="app_nav text-decoration-none fw-bold">Movie</router-link>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">
                <router-link :to="{ name: 'ArticleView' }" class="app_nav text-decoration-none fw-bold">Community</router-link>
              </a>
            </li>
            <!-- <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Dropdown
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">Something else here</a></li>
              </ul>
            </li> -->
          </ul>
          <div class="d-flex" >
            <div v-if="isLogin">
              <router-link :to="{ name: 'MyProfileView' }" class="app_nav fw-bold text-decoration-none">
                {{ currentUser.username }}
              </router-link>
              님 안녕하세요. 
              <button @click="logout" class="btn btn-info">로그아웃</button>
              </div>
              <div v-else>
                로그인되지 않았습니다.
                <button @click="goToLogInPage" class="btn btn-info">로그인</button> | 
                <button @click="goToSignUpPage" class="btn btn-info">회원가입</button> 
            </div>
            <!-- <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button> -->
          </div>
        </div>
      </div>
    </nav>
    <router-view/>
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
      this.$router.push({ name: 'SignUpView' });
    },
    goToLogInPage() {
      this.$router.push({ name: 'LogInView' });
    }
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
}
#header_image{
  width : 100%;
}
#service_name{
  color: #bfbfbf
}

.logo_img{
  height: 80px;
}

#top_navbar {
  background-color: #261639;
}

.app_nav{
  color: #ff2679
}

</style>
