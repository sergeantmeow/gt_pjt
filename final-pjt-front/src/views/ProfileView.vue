<template>
  <div>
    <h1>Profile Page</h1>
    <p>사용자 이름: {{ user.username }}</p>
    <p>사용자 MBTI: {{ user.mbti }}</p>
    <!-- <p>사용자 회원가입한 날: {{ user.date_joined }}</p> -->
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  data() {
    return {
      user : null
    }
  },
  computed: {
    currentUser() {
      return this.$store.getters.currentUser;
    },
  },
  created(){
    if (this.$route.params.username !== this.currentUser.username) {
      this.getUserProfile(this.$route.params.username);
    } else {
      this.user = this.currentUser;
    }
  },
  methods: {
    getUserProfile(username) {
      axios({
        method: 'get',
        url: `${API_URL}/profile/${username}/`,
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
