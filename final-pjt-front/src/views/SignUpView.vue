<template>
  <div>
    <h2 class="title-mg-ct">SignUp</h2>
    <div class="container sign-color fw-bold">
      <div class="row justify-content-center">
        <div class="col-md-4">
        <form @submit.prevent="signUp" class="mt-4">
          <div class="form-group">
          <label for="username">username</label>
          <input type="text" id="username" v-model="username" class="form-control">
          </div>
          <div class="form-group">
          <label for="password1"> password</label>
          <input type="password" id="password1" v-model="password1" class="form-control">
          </div>
          <div class="form-group">
          <label for="password2"> password confirmation</label>
          <input type="password" id="password2" v-model="password2" class="form-control">
          </div>
          <div class="form-group">
          <label for="mbti"> mbti</label>
          <input type="text" id="mbti" v-model="mbti" class="form-control">
          </div>
          <div class="signup-link">
          <a href="https://www.16personalities.com/ko/%EB%AC%B4%EB%A3%8C-%EC%84%B1%EA%B2%A9-%EC%9C%A0%ED%98%95-%EA%B2%80%EC%82%AC" target="_blank">MBTI 유형 검사하기</a><br>
          <input type="submit" value="신청" class="btn btn-signup fw-bold">
          </div>
        </form>
        <div class="signup-link">
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
            올바른 MBTI를 넣어주세요. MBTI를 모르시다면?
            <br>
            <a href="https://www.16personalities.com/ko/%EB%AC%B4%EB%A3%8C-%EC%84%B1%EA%B2%A9-%EC%9C%A0%ED%98%95-%EA%B2%80%EC%82%AC">검사하러가기</a>
            </div>
          </div>
        </div>
      </div>
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
      let upperMBTI = null
      if(this.mbti != null){
        upperMBTI = this.mbti.toUpperCase()
      }
      this.passwordsMatchError = false
      this.mbtiNullError = false
      this.mbtiWrongError = false
      if (this.password1 !== this.password2) {
        this.passwordsMatchError = true; // 비밀번호 불일치 오류 플래그 설정
        return; // 함수 종료
      }
      if (this.mbti == null){
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
  color: #bfbfbf;
}

.btn-signup {
  background-color: #261639;
  color: #bfbfbf;
}

.btn-signup:hover {
  background-color: #7c6891;
}

.sign-color{
  color : #bfbfbf;
}

.signup-link {
  padding: 5px;
}

.signup-link a {
  text-decoration: none;
  color: #ff2679
}

.signup-link a:hover {
  text-decoration: underline;
  color: #ff9ec3
}
</style>