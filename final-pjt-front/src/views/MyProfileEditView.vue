<template>
  <div class="container fw-bold">
    <h2 class="title-mg-ct">회원정보 수정</h2>
    <form @submit.prevent="changePassword" class="row justify-content-center mt-4">
      <div class="col-md-6">
        <label for="currentPassword">기존 비밀번호: </label>
        <input type="password" id="currentPassword" v-model="currentPassword" required class="form-control"><br>

        <label for="newPassword">새로운 비밀번호: </label>
        <input type="password" id="newPassword" v-model="newPassword" required class="form-control"><br>

        <label for="confirmPassword">비밀번호 확인: </label>
        <input type="password" id="confirmPassword" v-model="confirmPassword" required class="form-control"><br>

        <button type="submit" class="btn btn-primary">수정</button>
      </div>
    </form>
    <hr>
    <form @submit.prevent="changeUserInfo" class="row justify-content-center mt-4">
      <div class="col-md-6">
        <label for="mbti">MBTI: </label>
        <input type="text" id="mbti" v-model="mbti" :placeholder="mbti || 'MBTI를 입력하세요'" required class="form-control"><br>
        <button type="submit" class="btn btn-primary mb-4">수정</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MyProfileEditView',
  data() {
    return {
      currentPassword: '',
      newPassword: '',
      confirmPassword: '',
      mbti: '',
    };
  },
  created() {
    this.mbti = this.$store.getters.currentUser.mbti || '';
  },
  methods: {
    changePassword() {
      // 비밀번호 일치 확인
      if (this.newPassword !== this.confirmPassword) {
        alert('새로운 비밀번호와 비밀번호 확인이 일치하지 않습니다.');
        return;
      }

      const updatedData = {
        new_password1 : this.newPassword,
        new_password2 : this.confirmPassword
      };
      

      axios({
        method: 'post',
        url: `${API_URL}/accounts/password/change/`,
        headers: {
        Authorization: `Token ${this.$store.state.user.token}`,
      },
        data: updatedData
      })
      .then(() => {
        alert('비밀번호가 변경되었습니다.')
        this.currentPassword = ''
        this.newPassword = ''
        this.confirmPassword=  ''
      })
      .catch(error => {
        console.error('비밀번호 업데이트 중 오류가 발생했습니다.', error);
      });
    },
    changeUserInfo() {
      const mbtiList = ['INTJ', 'INTP', 'INFJ','INFP','ISTJ','ISTP','ISFJ','ISFP','ENTJ','ENTP','ENFJ','ENFP','ESTJ','ESTP','ESFJ','ESFP']
      let upperMBTI = this.mbti.toUpperCase()
      if (mbtiList.indexOf(upperMBTI) === -1) {
        alert('올바른 mbti를 입력해주세요')
        this.mbti = ''
        return
      }
      const updatedData = {
        mbti: upperMBTI
      };

      axios({
        method: 'patch',
        url: `${API_URL}/accounts/edit/`,
        headers: {
        Authorization: `Token ${this.$store.state.user.token}`,
      },
        data: updatedData
      })
      .then(() => {
        alert('mbti가 변경되었습니다.')
        const payload = updatedData
        this.$store.dispatch('updateUser', payload)
        this.mbti = this.$store.getters.currentUser.mbti || '';
      })
      .catch(error => {
        console.error('유저정보 업데이트 중 오류가 발생했습니다.', error);
      });
    }
  }
};
</script>

<style scoped>
.btn-primary {
  color: #bfbfbf;
  background-color: #4f3d63;
  border-color: #4f3d63;
}

.btn-primary:hover {
  color: #ff2679;
  background-color: #4f3d63;
  border-color: #4f3d63;
}
</style>
