<template>
  <div>
    <h1>MyProfileEdit Page</h1>
    <form @submit.prevent="updateProfile">
      <label for="currentPassword">기존 비밀번호: </label>
      <input type="password" id="currentPassword" v-model="currentPassword" required><br>

      <label for="newPassword">새로운 비밀번호: </label>
      <input type="password" id="newPassword" v-model="newPassword" required><br>

      <label for="confirmPassword">비밀번호 확인: </label>
      <input type="password" id="confirmPassword" v-model="confirmPassword" required><br>

      <label for="mbti">MBTI: </label>
      <input type="text" id="mbti" v-model="mbti" required><br>

      <button type="submit">저장</button>
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
  mounted() {
    this.getUserProfile(this.$route.params.username)
  },
  methods: {
    getUserProfile(username) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${username}/`,
      })
      .then((response) => {
        this.user = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
    },
    updateProfile() {
      // 비밀번호 일치 확인
      if (this.newPassword !== this.confirmPassword) {
        console.error('새로운 비밀번호와 비밀번호 확인이 일치하지 않습니다.');
        return;
      }

      const { id, username } = this.user;
      const updatedData = {
        id,
        username,
        currentPassword: this.currentPassword,
        newPassword: this.newPassword,
        mbti: this.mbti
      };
      

      axios({
        method: 'put',
        url: `${API_URL}/accounts/edit/${username}/`,
        headers: {
        Authorization: `Token ${this.$store.state.user.token}`,
      },
        data: updatedData
      })
      .then(response => {
        console.log('프로필이 업데이트되었습니다.', response.data);
      })
      .catch(error => {
        console.error('프로필 업데이트 중 오류가 발생했습니다.', error);
      });
    }
  }
};
</script>

<style>
/* 필요한 스타일을 추가해주세요. */
</style>
