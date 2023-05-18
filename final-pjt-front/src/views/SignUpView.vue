<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2"><br>
      
      <label for="mbti"> mbti : </label>
      <input type="text" id="mbti" v-model="mbti"><br>
      <a href="https://www.16personalities.com/ko/%EB%AC%B4%EB%A3%8C-%EC%84%B1%EA%B2%A9-%EC%9C%A0%ED%98%95-%EA%B2%80%EC%82%AC" target="_blank">MBTI 유형 검사하기</a><br>
      <input type="submit" value="SignUp">
    </form>
    <div v-if="passwordsMatchError" class="error-message">
      비밀번호가 일치하지 않습니다.
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      mbti: null,
      passwordsMatchError: false, // 비밀번호 불일치 오류 플래그
    }
  },
  methods: {
    signUp() {
      if (this.password1 !== this.password2) {
        this.passwordsMatchError = true; // 비밀번호 불일치 오류 플래그 설정
        return; // 함수 종료
      }

      const payload = {
        username : this.username,
        password1 : this.password1,
        password2 : this.password2,
        mbti : this.mbti
      }

      this.$store.dispatch('signUp', payload)

    }
  }
}
</script>

<style>
.error-message {
  color: red;
}
</style>