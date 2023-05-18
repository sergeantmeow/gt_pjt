<template>
  <div>
    <h1>회원권 신청</h1>
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
    <div v-if="mbtiNullError" class="error-message">
      MBTI를 넣어주세요. 
      <br>
      MBTI를 모르시다면?
      <br>
      <a href="https://www.16personalities.com/ko/%EB%AC%B4%EB%A3%8C-%EC%84%B1%EA%B2%A9-%EC%9C%A0%ED%98%95-%EA%B2%80%EC%82%AC">검사하러가기</a>
    </div>
    <div v-if="mbtiWrongError" class="error-message">
      정상적인 MBTI를 넣어주세요. MBTI를 모르시다면?
      <br>
      <a href="https://www.16personalities.com/ko/%EB%AC%B4%EB%A3%8C-%EC%84%B1%EA%B2%A9-%EC%9C%A0%ED%98%95-%EA%B2%80%EC%82%AC">검사하러가기</a>
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
      mbtiNullError: false,
      mbtiWrongError: false,
    }
  },
  methods: {
    signUp() {
      const mbtiList = ['INTJ', 'INTP', 'INFJ','INFP','ISTJ','ISTP','ISFJ','ISFP','ENTJ','ENTP','ENFJ','ENFP','ESTJ','ESTP','ESFJ','ESFP']
      const upperMBTI = this.mbti.toUpperCase()
      this.passwordsMatchError = false
      this.mbtiNullError = false
       this.mbtiWrongError = false
      if (this.password1 !== this.password2) {
        this.passwordsMatchError = true; // 비밀번호 불일치 오류 플래그 설정
        return; // 함수 종료
      }
      if (upperMBTI == null){
        this.mbtiNullError = true;
      }else if(mbtiList.includes(upperMBTI) == false){
          this.mbtiWrongError = true;
      }else{
        const payload = {
          username : this.username,
          password1 : this.password1,
          password2 : this.password2,
          mbti : upperMBTI
        }
        this.$store.dispatch('signUp', payload)
      }
    }
  }
}
</script>

<style>
.error-message {
  color: red;
}
</style>