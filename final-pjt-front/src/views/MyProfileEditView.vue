<template>
  <div>
    <h1>MyProfileEdit Page</h1>
    <form @submit.prevent="changePassword">
      <label for="currentPassword">기존 비밀번호: </label>
      <input type="password" id="currentPassword" v-model="currentPassword" required><br>

      <label for="newPassword">새로운 비밀번호: </label>
      <input type="password" id="newPassword" v-model="newPassword" required><br>

      <label for="confirmPassword">비밀번호 확인: </label>
      <input type="password" id="confirmPassword" v-model="confirmPassword" required><br>

      <button type="submit">수정</button>
    </form>
    <hr>
    <form @submit.prevent="changeUserInfo">
      <label for="mbti">MBTI: </label>
      <input type="text" id="mbti" v-model="mbti" :placeholder="mbti || 'MBTI를 입력하세요'" required><br>
      <button type="submit">수정</button>
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

<style>
/* 필요한 스타일을 추가해주세요. */
</style>
