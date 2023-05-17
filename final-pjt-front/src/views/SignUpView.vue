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
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const mbti = this.mbti

      if (password1 !== password2) {
        this.passwordsMatchError = true; // 비밀번호 불일치 오류 플래그 설정
        return; // 함수 종료
      }

      const payload = {
        username, password1, password2, mbti
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