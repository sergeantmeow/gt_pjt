<template>
  <div>
    <h1>OtherProfile Page</h1>
    <template v-if="user">
      <p>이름: {{ user.username }}</p>
      <p>MBTI: {{ user.mbti }}</p>
      <p>가입일: {{ user.date_joined }}</p>
      <p>최근 로그인: {{ user.last_login }}</p>
      <hr>
      <UserArticle :username="user.username" />
      <hr>
      <UserComment :username="user.username" />
      <p>팔로워 : {{ user.followers.length }}</p>
      <div v-if="isNotAuthor">
      <button @click="followUser">팔로잉</button>
      </div>
    </template>
  </div>
</template>

<script>
import axios from 'axios'
import UserArticle from '@/components/UserArticle'
import UserComment from '@/components/UserComment'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'OtherProfileView',
  components: {
    UserArticle, UserComment
  },
  data() {
    return {
      user : null
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    },
    currentUser(){
      return this.$store.getters.currentUser
    },
    isNotAuthor() {
      return this.isLogin && this.user?.username != this.currentUser.username
    },
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
    followUser() {
      const id = this.user.id
      axios({
        method: 'post',
        url: `${API_URL}/accounts/follow/${id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.user.token}`
        }
      })
      .then(() => {
        this.getUserProfile(this.$route.params.username);
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