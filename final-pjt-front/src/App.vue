<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <nav>
      <div v-if="isLogin">
      {{ userName }} 님 안녕하세요
      <button @click="logout">로그아웃</button>
      </div>
      <div v-else>
        로그인되지 않았습니다.
        <button @click="goToLogInPage">로그인</button>
        <button @click="goToSignUpPage">회원가입</button> |
      </div>
      <router-link :to="{ name: 'MovieListView'}">Movie</router-link> |
      <router-link :to="{ name: 'ArticleView' }">Articles</router-link>
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
    userName() {
      return this.$store.getters.userName; // 사용자 이름 가져오기
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
  color: #2c3e50;
  margin-top: 60px;
}
</style>
