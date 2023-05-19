<template>
  <div>
    <h1>OtherProfile Page</h1>
    <template v-if="user">
      <p>사용자 이름: {{ user.username }}</p>
      <p>사용자 MBTI: {{ user.mbti }}</p>
      <p>가입일: {{ user.date_joined }}</p>
      <p>최근 로그인: {{ user.last_login }}</p>
    </template>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'OtherProfileView',
  data() {
    return {
      user : null
    }
  },
  created(){
      this.getUserProfile(this.$route.params.username);
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
  }
};
</script>

<style>

</style>